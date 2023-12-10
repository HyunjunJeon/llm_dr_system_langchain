import os

from langchain import hub
from langchain_core.runnables import RunnablePassthrough

from load_env import load_multi_dotenv

load_multi_dotenv()

langchain_hub_project = os.getenv("ORG_NAME_LANGCHAIN_HUB")

# LCEL: LangChain Expression Language
# https://python.langchain.com/docs/expression_language/

# Input Data 를 관리할 Chain 의 변수를 선언
# Langchain Hub 에서 선언한 Prompt 와 Input 해야할 값들을 맞춰서 선언
_base_input_data = {
    "inputs": RunnablePassthrough(),
}

# Langchain Hub 에서 Prompt 를 가져옴
_bard_prompt = hub.pull(langchain_hub_project + "base_bard_prompt")
_gpt35_prompt = hub.pull(langchain_hub_project + "base_gpt35_prompt")
_gpt4_prompt = hub.pull(langchain_hub_project + "base_gpt4_prompt")

# data 처리와 Prompt 를 엮어서 기본 체인을 완성
base_bard_chain = _base_input_data | _bard_prompt
base_gpt35_chain = _base_input_data | _gpt35_prompt
base_gpt4_chain = _base_input_data | _gpt4_prompt
