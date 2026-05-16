from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from agents.weather_agent   import weather_agent
from agents.budget_agent    import budget_agent
from agents.transport_agent import transport_agent

orchestrator = Agent(
    name="travel_orchestrator",
    model=LiteLlm(model="groq/llama-3.3-70b-versatile"),
    description="Main travel intelligence coordinator.",
    instruction="""
    You coordinate weather_agent, budget_agent and transport_agent.
    Delegate to the right agents based on the user query.
    Combine all results into one final travel report.
    """,
    sub_agents=[weather_agent, budget_agent, transport_agent]
)