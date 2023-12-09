import os

from langchain import hub
from langchain_core.runnables import RunnablePassthrough

from load_env import load_multi_dotenv

load_multi_dotenv()

print(os.getenv)

langchain_hub_project = "jhj-rascal/"

_base_input_data = {
    "inputs": RunnablePassthrough(),
    "history": RunnablePassthrough(),
}

_bard_prompt = hub.pull(langchain_hub_project + "base_bard_prompt")
_gpt35_prompt = hub.pull(langchain_hub_project + "base_gpt35_prompt")
_gpt4_prompt = hub.pull(langchain_hub_project + "base_gpt4_prompt")

base_bard_prompt = _base_input_data | _bard_prompt
base_gpt35_prompt = _base_input_data | _gpt35_prompt
base_gpt4_prompt = _base_input_data | _gpt4_prompt
