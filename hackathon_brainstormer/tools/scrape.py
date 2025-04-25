from google.adk.tools.langchain_tool import LangchainTool
from google.adk.tools.crewai_tool import CrewaiTool
from crewai_tools import ScrapeWebsiteTool

scrape_website_instance = ScrapeWebsiteTool()

scrape_website_tool = CrewaiTool(
    name="scrape_website_tool",
    description="extract and read the content of a specified website",
    tool=scrape_website_instance,
)
