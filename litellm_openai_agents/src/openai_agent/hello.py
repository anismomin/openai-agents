from __future__ import annotations

import os
import asyncio
from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel

set_tracing_disabled(disabled=True)

MODEL = "gemini/gemini-2.0-flash"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


@function_tool
def get_weather(city: str)->str:
    print(f"[debug] getting weather for {city}")
    return f"The weather in {city} is sunny."


def main(model: str, api_key: str):
  agent = Agent(
      name="Assistant",
      instructions="You only respond in haikus.",
      model=LitellmModel(model=model, api_key=api_key),
      tools=[get_weather]
  )

  result = Runner.run_sync(agent, "What's the weather in Karachi?")
  
  print(result.final_output)


main(model=MODEL, api_key=GEMINI_API_KEY)

