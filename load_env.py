import os
from pathlib import Path

from dotenv import load_dotenv

CURRENT_DIR = Path(__file__).parent
SECRETS_DIR = os.path.join(CURRENT_DIR, "secrets")

BARD_ENV = os.path.join(SECRETS_DIR, ".env.bard")
LANGCHAIN_ENV = os.path.join(SECRETS_DIR, ".env.langchain")
OPENAI_ENV = os.path.join(SECRETS_DIR, ".env.openai")


def load_bard_env() -> None:
    """
    Bard .env 를 로드
    :return:
    """
    load_dotenv(dotenv_path=BARD_ENV)


def load_multi_dotenv() -> None:
    """
    Multiple .env 를 로드
    :return:
    """
    load_dotenv(dotenv_path=LANGCHAIN_ENV)
    load_dotenv(dotenv_path=OPENAI_ENV)
