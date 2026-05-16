from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from tools.weather_tool import get_weather

weather_agent = Agent(
    name="weather_agent",
    model=LiteLlm(model="groq/llama-3.3-70b-versatile"),
    description="Provides real live weather for any city.",
    instruction="""
    You are a weather specialist.
    ALWAYS call get_weather tool first. Never answer from memory.
    Report exactly: temperature, feels like, condition, humidity, wind speed.
    Add one short practical travel tip based on the weather.
    Do not mention budget, transport or anything else. Just weather. Then stop.
    """,
    tools=[get_weather]
)