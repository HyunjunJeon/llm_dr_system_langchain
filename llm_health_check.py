from llms import get_openai, get_bard


def bard_health_check() -> bool:
    response = get_bard().invoke("health_check: Hi")
    if response is not None:
        return True
    return False


def openai_health_check() -> bool:
    response = get_openai().invoke("health_check: Hi")
    if response is not None:
        return True
    return False


if __name__ == "__main__":
    print(bard_health_check())
