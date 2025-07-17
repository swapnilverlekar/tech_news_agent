"""
NewsAggregatorBuilder agent is the root agent responsible for generating a sustainability article 
that summarizes green tech trends, ESG sentiment, visual insights, and posts it to Notion.
"""

from google.adk.agents import SequentialAgent
from .sub_agents.FetchContentParallelAgent import fetch_content_parallel_agent
from .sub_agents.InsightBuilderSequentialAgent import insight_builder_sequential_agent
from .sub_agents.PostToNotionAgent import post_on_notion_agent

root_agent = SequentialAgent(
    name="NewsAggregatorBuilder",
    sub_agents=[
        fetch_content_parallel_agent,
        insight_builder_sequential_agent,
        post_on_notion_agent
    ],
    description=(
        "A multi-agent pipeline that fetches sustainability-related news, analyzes impact and ESG sentiment, "
        "builds a formatted article with charts, and publishes the final summary to a Notion page."
    ),
)
