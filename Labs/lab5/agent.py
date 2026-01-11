import os
from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient
from .tools import analyze_numbers

# ---------------------------
#  Provider config
# ---------------------------

base_url = os.getenv("API_BASE_URL")
api_key = os.getenv("API_KEY")
model_id = os.getenv("MODEL", "openai/gpt-oss-20b")

if not api_key:
    raise RuntimeError("API_KEY is not set.")

client = OpenAIChatClient(
    base_url=base_url,
    api_key=api_key,
    model_id=model_id,
)

# ---------------------------
#  Agent definition
# ---------------------------

agent = ChatAgent(
    chat_client=client,
    name="number-analyzer-agent",
    instructions="""
        You are a helpful agent that analyzes lists of numbers.
        
        You have a tool called `analyze_numbers` that can calculate statistics 
        (count, min, max, sum, average) for a given list of numbers.

        If the user provides a list of numbers, use the tool to analyze them 
        and then summarize the results in a friendly way.
    """,
    tools=[
        analyze_numbers,
    ],
)