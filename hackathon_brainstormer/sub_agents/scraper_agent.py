from google.adk.agents import LlmAgent
from ..tools import scrape_website_tool

hackathon_scraper_agent = LlmAgent(
    name="hackathon_scraper",
    description=(
        "An AI agent specialized in scraping and extracting key information from hackathon web pages. "
        "It takes a URL to a specific hackathon page as input. Its purpose is to analyze the content "
        "and return a consolidated text summary containing crucial details like the hackathon's theme, "
        "rules, 'What to Build' requirements, judging criteria, suggested tracks, technologies, "
        "and overall goals. This extracted context is intended for use by other agents to understand "
        "the hackathon's parameters, often for generating project ideas."
    ),
    model="gemini-2.5-flash-preview-04-17",
    instruction=(
        "You are an information gathering agent specializing in hackathons. Your primary tool is the `FirecrawlScrapeWebsiteTool`. "
        "Your task is to process an incoming request containing a hackathon URL. \n"
        "1. Receive the hackathon URL as input. \n"
        "2. Prepare to use the `FirecrawlScrapeWebsiteTool`. \n"
        "3. **Strategy Decision:** Determine the best way to use the tool for this task:\n"
        "    a. **Preferred Method (LLM Extraction):** If possible, use the tool's `extractor_options`. Define an `extractionPrompt` asking the tool's LLM to specifically find and structure the key hackathon details: Theme, Rules, Judging Criteria, 'What to Build'/Challenges/Requirements section, Suggested Technologies/APIs, and Overall Goal. Define a suitable `extractionSchema` (e.g., JSON format: `{'theme': '...', 'requirements': '...', 'criteria': '...', 'rules': '...', 'tech': '...', 'goal': '...'}`). Set `mode='llm-extraction'`. This often yields the cleanest, most relevant data directly.\n"
        "    b. **Alternative Method (Markdown):** If LLM extraction isn't suitable or fails, use the tool to get the main content as clean Markdown. Set `page_options={'onlyMainContent': True}` to exclude headers/footers. \n"
        "4. Invoke the `FirecrawlScrapeWebsiteTool` with the chosen URL and options. \n"
        "5. **Process the Output:**\n"
        "    a. If you used LLM Extraction: The tool should return structured data (like JSON). Verify its completeness based on the requested schema. Return this structured data directly.\n"
        "    b. If you received Markdown: Analyze the Markdown text. Extract and summarize the key information (Theme, Requirements, Criteria, Rules, Tech, Goal). Structure this summary clearly, perhaps using headings or a simple key-value format in your response text. \n"
        "6. Return *only* the extracted and structured hackathon information (either the JSON from LLM extraction or your summary of the Markdown). Do not add conversational filler."
    ),
    tools=[scrape_website_tool],
    output_key="generated_hackathon_details",
)
