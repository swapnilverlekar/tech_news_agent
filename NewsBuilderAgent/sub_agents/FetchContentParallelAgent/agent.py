"""
FetchContentParallelAgent

This agent runs multiple fetchers in parallel to collect:
- Latest sustainable tech news
- Carbon impact analysis
- ESG-related social sentiment
"""

from google.adk.agents import ParallelAgent
from .sub_agents.GreenTechNewsFetcherAgent import green_tech_news_fetcher_agent
from .sub_agents.CarbonImpactAnalyzerAgent import carbon_impact_analyzer_agent
from .sub_agents.SocialESGSentimentAgent import social_esg_sentiment_agent

fetch_content_parallel_agent = ParallelAgent(
    name="FetchContentParallelAgent",
    description="Gathers sustainability news, carbon impact metrics, and ESG sentiment using parallel sub-agents.",
    sub_agents=[
        green_tech_news_fetcher_agent,
        carbon_impact_analyzer_agent,
        social_esg_sentiment_agent
    ]
)
