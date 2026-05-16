import asyncio
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from agents.weather_agent   import weather_agent
from agents.budget_agent    import budget_agent
from agents.transport_agent import transport_agent

load_dotenv()

async def run_single_agent(agent, query: str) -> str:
    session_service = InMemorySessionService()
    runner = Runner(
        agent=agent,
        app_name="travel_intelligence",
        session_service=session_service
    )
    session = await session_service.create_session(
        app_name="travel_intelligence",
        user_id="user1"
    )
    response = runner.run(
        user_id="user1",
        session_id=session.id,
        new_message=types.Content(
            role="user",
            parts=[types.Part(text=query)]
        )
    )
    last_response = None
    for event in response:
        if event.content and event.content.parts:
            for part in event.content.parts:
                if hasattr(part, "text") and part.text:
                    last_response = part.text
    return last_response or "No response."


async def run_query(query: str) -> str:
    weather_result   = await run_single_agent(
        weather_agent,
        f"Get weather for the destination in this query: {query}"
    )
    budget_result    = await run_single_agent(
        budget_agent,
        f"Calculate budget for this travel query: {query}"
    )
    transport_result = await run_single_agent(
        transport_agent,
        f"Get local transport for the destination in this query: {query}"
    )

    return f"""🌤️ **WEATHER**
{weather_result}

✈️ **BUDGET**
{budget_result}

🚇 **LOCAL TRANSPORT**
{transport_result}"""


if __name__ == "__main__":
    queries = [
        "I'm traveling from Frankfurt to Tokyo for 5 days. What's the weather, budget and local transport?",
        "What's the minimum budget to travel from Germany to Iceland for 10 days?",
        "I want to travel from Germany to Morocco for 7 days. Give me weather, budget and local transport."
    ]
    for query in queries:
        print(f"\n🧳 Query: {query}")
        print("-" * 50)
        result = asyncio.run(run_query(query))
        print(result)
        print("=" * 50)