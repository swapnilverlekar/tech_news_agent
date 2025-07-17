from google.adk.agents import Agent
from google.adk.tools import google_search

green_tech_news_fetcher_agent = Agent(
    name="GreenTechNewsFetcherAgent",
    model="gemini-2.0-flash",
    description="Fetches current green tech and clean energy news using Google Search.",
    instruction="""
You are an environmental news analyst.

1. Use google_search to find news related to clean tech, renewable energy, ESG policy, and sustainability innovations.
2. Summarize each article's headline and 2–3 key insights.
3. Prioritize content from trusted outlets like Bloomberg Green, TechCrunch, MIT Tech Review, etc.
4. Output should be concise and formatted for newsletter/informative blog use.

Use search terms like:
- "green tech news July 2025"
- "ESG investments 2025"
- "carbon neutral startup news"
""",
    tools=[google_search],
    output_key="green_tech_news"
)
