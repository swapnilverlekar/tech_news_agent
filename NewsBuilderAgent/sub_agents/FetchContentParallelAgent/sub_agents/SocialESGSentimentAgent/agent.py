from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from datetime import datetime

def get_social_esg_sentiment(topic: str) -> dict:
    """
    Simulated function that mimics pulling ESG sentiment on clean tech topics from social platforms.
    Replace with actual Reddit/Twitter API integrations as needed.
    """
    print(f"--- Tool: get_social_esg_sentiment called for {topic} ---")

    simulated_response = {
        "EV": "Mostly positive — trending on Twitter due to breakthrough in solid-state batteries.",
        "Carbon Credit": "Mixed — Reddit shows skepticism on real impact of carbon offset startups.",
        "Solar": "Highly positive — strong discussions on adoption in emerging markets.",
        "Nuclear": "Divided — heated debates on Reddit between safety vs. energy efficiency."
    }

    return {
        "topic": topic,
        "sentiment_summary": simulated_response.get(topic, "No relevant sentiment data found."),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

social_esg_sentiment_agent = Agent(
    name="SocialESGSentimentAgent",
    model="gemini-2.0-flash",
    description="Analyzes public sentiment on ESG topics like carbon credits, EVs, or green startups.",
    instruction="""
You are a sentiment analyst tracking social media (Reddit, Twitter) for public opinion on clean tech and ESG topics.

1. Use the get_social_esg_sentiment tool to pull a short summary.
2. Format response like:
"Sentiment for Solar: Highly positive due to growing global adoption. (As of 2025-07-17 19:30 EST)"
""",
    tools=[get_social_esg_sentiment],
    output_key="esg_social_sentiment"
)
