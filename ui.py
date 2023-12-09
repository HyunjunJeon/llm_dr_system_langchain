import os

import streamlit as st
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.output_parsers import StrOutputParser

from llms import get_openai, get_bard
from load_env import load_multi_dotenv
from llm_health_check import openai_health_check, bard_health_check
from prompts import base_bard_prompt, base_gpt35_prompt, base_gpt4_prompt


# OpenAI Streamlit Chat Handling (Bard X)
class ChatMessageCallbackHandler(BaseCallbackHandler):
    message = ""
    message_box = None

    def on_llm_start(self, *args, **kwargs):
        self.message_box = st.empty()

    def on_llm_end(self, *args, **kwargs):
        save_message(self.message, "ai", "openai")

    def on_llm_new_token(self, token, *args, **kwargs):
        self.message += token
        self.message_box.markdown(self.message)


def save_message(content: str, role: str, llm_type: str = ""):
    st.session_state["messages"].append(
        {
            "content": content,
            "role": role,
            "llm_type": llm_type,
        }
    )


def get_chat_history():
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            if message["llm_type"] == "":
                st.markdown(message["content"])
            else:
                st.markdown(message["llm_type"] + "답변:  " + message["content"])


def streamlit_init():
    load_multi_dotenv()

    st.set_page_config(
        page_title="LLM DR",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title(
        "DevFest 2023 Song-do 😎 Langchain based LLM DR system with OpenAI GPT and Google Bard"
    )

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # 매번 헬스체크를 할 필요는....
    # if "bard_status" not in st.session_state:
    #     st.session_state["bard_status"] = bard_health_check()
    #
    # if "openai_status" not in st.session_state:
    #     # st.session_state["openai_status"] = openai_health_check()
    #     st.session_state["openai_status"] = False

    if len(st.session_state["messages"]) == 0:
        save_message(
            "안녕하세요. 저는 금융 기반 질문에만 대답하는 챗봇 OLA 입니다. 저에게 궁금하신게 있나요? ",
            "ai",
            "",
        )

    get_chat_history()


def get_llm(llm_type: str):
    return {
        "bard": get_bard(),
        "gpt35_turbo": get_openai(
            temperature=float(os.getenv("MODEL_TEMPERATURE")),
            model_name=os.getenv("GPT35_TURBO_MODEL"),
            streaming=True,
            callbacks=[ChatMessageCallbackHandler()],
        ),
        "gpt4_turbo": get_openai(
            temperature=float(os.getenv("MODEL_TEMPERATURE")),
            model_name=os.getenv("GPT4_TURBO_MODEL"),
            streaming=True,
            callbacks=[ChatMessageCallbackHandler()],
        ),
    }[llm_type]


def chatbot_main():
    if message := st.chat_input(""):
        save_message(message, "human")

        with st.chat_message("human"):
            st.markdown(message)

        # if not st.session_state["openai_status"]:
        if not openai_health_check():
            with st.chat_message("ai"):
                message_placeholder = st.empty()
                # if st.session_state["bard_status"]:
                if bard_health_check():
                    bard_chain = base_bard_prompt | get_llm("bard") | StrOutputParser()
                    response = bard_chain.invoke(message)
                    message_placeholder.markdown(response)
                    save_message(response, "ai", "bard")
        else:
            if message.startswith("#gpt4"):
                message = message.replace("#gpt4", "")
                with st.chat_message("ai"):
                    gpt4_chain = base_gpt4_prompt | get_llm("gpt4_turbo")
                    gpt4_chain.invoke(message)
            else:
                with st.chat_message("ai"):
                    gpt35_chain = base_gpt35_prompt | get_llm("gpt35_turbo")
                    gpt35_chain.invoke(message)


if __name__ == "__main__":
    streamlit_init()
    chatbot_main()
