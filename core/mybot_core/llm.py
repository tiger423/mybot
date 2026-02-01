from openai import OpenAI
from mybot_core.tools_schema import TOOLS_SCHEMA

_client = OpenAI()

def call_llm(messages):
    return _client.responses.create(
        model="gpt-5.2",
        input=messages,
        tools=TOOLS_SCHEMA,
        max_output_tokens=1200,
    )
