import os
from openai import OpenAI
from agent.prompts import build_prompt
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # 成本低 + 稳定
        messages=[
            {"role": "system", "content": "You are an expert build analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content


def run_agent(task: str) -> str:
    print("Step 1: Task received")

    prompt = build_prompt(task)

    print("Step 2: LLM reasoning...")
    result = call_llm(prompt)

    print("Step 3: Post-processing...")

    return result