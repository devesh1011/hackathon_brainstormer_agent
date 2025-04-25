from google.adk.agents.sequential_agent import SequentialAgent
from .sub_agents import hackathon_scraper_agent, brainstormer_agent

hackathon_brainstormer_agent = SequentialAgent(
    name="hackathon_brainstormer",
    sub_agents=[hackathon_scraper_agent, brainstormer_agent],
    description="Analyzes a hackathon URL by scraping its details via a sub-agent, then brainstorms innovative project ideas tailored to the event's specific theme, requirements, judging criteria, and technologies",
)

root_agent = hackathon_brainstormer_agent
