## < Devfest - 2023 - Songdo > Hand-On: OpenAI 발 위기극복? Langchain 과 Bard 으로 구성하는 LLM DR 시스템 구축

--- 

### 파이썬 3.11.6

```
ROOT
├── README.md
├── __init__.py
├── llm_health_check.py         => LLM Health Check
├── llms.py                     => LLM 선언(Bard, OpenAI)
├── load_env.py                 => .env 환경변수로 로드
├── prompts.py                  => Prompt 선언 부(Langchain Hub)
├── requirements-local.txt
├── requirements.txt            
├── .env.sample                 => .env Sample
├── secrets                     => 실제 .env.{bard,openai,langchain} 보관
└── ui.py                       => Streamlit UI
```

--- 
[발표자료](https://docs.google.com/presentation/d/1hXb7HgDQvUDYqujnNAnkVu-ib073zgBxzdmoHTdI9eQ/edit?usp=sharing)
