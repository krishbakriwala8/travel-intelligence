from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from tools.transport_tool import get_local_transport

transport_agent = Agent(
    name="transport_agent",
    model=LiteLlm(model="groq/llama-3.3-70b-versatile"),
    description="Provides local transport information for any city.",
    instruction="""
    You are a transport specialist.
    ALWAYS call get_local_transport tool first.
    If tool returns verified_data — use that data exactly.
    If tool returns not_in_database — use your own knowledge for that city.
    Always show: best transport option, airport to city route and cost, daily cost, one tip.
    Never mention packing, weather or budget. Just transport. Then stop.
    """,
    tools=[get_local_transport]
)