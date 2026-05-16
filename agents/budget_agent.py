from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from tools.budget_tool import get_flight_estimate, get_exchange_rate

budget_agent = Agent(
    name="budget_agent",
    model=LiteLlm(model="groq/llama-3.3-70b-versatile"),
    description="Estimates minimum travel budget from Germany.",
    instruction="""
    You are a budget specialist.
    ALWAYS call get_flight_estimate tool first. Never guess numbers.
    Always show costs in EUR only.
    Show exact breakdown: flight, hotel, food, activities, total.
    If user asks for another currency, call get_exchange_rate tool.
    Do not mention weather, transport or anything else. Just budget. Then stop.
    """,
    tools=[get_flight_estimate, get_exchange_rate]
)