import asyncio
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.models.lite_llm import LiteLlm   
from google.genai import types

load_dotenv()

def get_weather(city: str) -> dict:
    """Get the current weather for a city."""
    return {
        "city": city,
        "temperature_c": "22",
        "condition": "Sunny",
        "humidity": "60%"
    }

weather_agent = Agent(
    name="weather_agent",
    model=LiteLlm(model="groq/llama-3.1-8b-instant"),  
    instruction="You are a weather expert. Use get_weather tool to answer weather questions.",
    tools=[get_weather]
)

async def main():
    session_service = InMemorySessionService()

    runner = Runner(
        agent=weather_agent,
        app_name="test_app",
        session_service=session_service
    )

    session = await session_service.create_session(
        app_name="test_app",
        user_id="user1"
    )

    response = runner.run(
        user_id="user1",
        session_id=session.id,
        new_message=types.Content(
            role="user",
            parts=[types.Part(text="What is the weather in Tokyo?")]
        )
    )

    for event in response:
        if event.is_final_response():
            if event.content and event.content.parts:
                print("\n Agent Response:")
                print(event.content.parts[0].text)

asyncio.run(main())