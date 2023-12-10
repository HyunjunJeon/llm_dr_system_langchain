from llms import get_openai, get_bard


def bard_health_check() -> bool:
    """
    Google Bard 의 상태를 간단한 Prompt 호출을 통해 체크
    :return:
    """
    response = get_bard().invoke("health_check: Hi")
    if response is not None:
        return True
    return False


def openai_health_check() -> bool:
    """
    OpenAI 의 상태를 간단한 Prompt 호출을 통해 체크
    :return:
    """
    response = get_openai().invoke("health_check: Hi")
    # if response is not None:
    #     return True
    return False


if __name__ == "__main__":
    print(bard_health_check())
