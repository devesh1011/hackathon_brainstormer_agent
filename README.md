# Hackathon Brainstormer Agent (Google ADK)

## Overview

This project implements a multi-agent AI system using the **Google Agent Development Kit (ADK)** to help users brainstorm project ideas for hackathons. Given a URL to a hackathon's webpage, the agent scrapes relevant details and then suggests tailored project ideas based on the hackathon's theme, requirements, and suggested technologies.

The primary goal is to automate the initial, often time-consuming, phase of hackathon participation: understanding the rules and coming up with relevant ideas.

## Features

* **URL-Based Input:** Simply provide the URL of the hackathon's main page.
* **Automated Scraping:** Extracts key details like themes, rules, 'What to Build' sections, judging criteria, and tech stacks using Firecrawl.
* **Contextual Ideation:** Generates 3 distinct project ideas specifically aligned with the scraped hackathon context.
* **Markdown Output:** Presents the brainstormed ideas in a clean, readable Markdown format.
* **Multi-Agent Architecture:** Built using Google ADK, demonstrating sequential agent workflows and state management.
* **Leverages LLMs:** Utilizes Google's Gemini models via ADK for scraping interpretation (potentially via Firecrawl's LLM extraction) and idea generation.

## How It Works (Architecture)

This project employs a multi-agent approach orchestrated by the Google ADK framework:

1. **`hackathon_brainstormer_agent` (Root Agent):** 
    -   This is likely configured as a `SequentialAgent` in ADK.
    -   It manages the overall workflow, taking the initial URL input and passing state between sub-agents.

2. **`hackathon_scraper_agent` (Sub-Agent 1):** 
    -   Receives the hackathon URL from the root agent.
    -   Uses the `firecrawl_tool` (which wraps the `FirecrawlScrapeWebsiteTool` or uses `firecrawl-py` directly) to access the URL.
    -   Instructs the tool to scrape the webpage, focusing on extracting relevant hackathon details (theme, requirements, rules, tech, criteria). It might use Firecrawl's clean Markdown output or its LLM-based extraction feature.
    -   The extracted context is saved into the agent state (e.g., `state["generated_hackathon_details"]`).

3. **`brainstormer_agent` (Sub-Agent 2):** 
    -   Receives the `generated_hackathon_details` from the previous agent's state.
    -   Analyzes this context using a Gemini LLM.
    -   Generates exactly three distinct and relevant project ideas based*only*on the provided details.
    -   Formats these ideas clearly using Markdown, including titles, concepts, and alignment notes.
    -   Outputs the final formatted Markdown string.
