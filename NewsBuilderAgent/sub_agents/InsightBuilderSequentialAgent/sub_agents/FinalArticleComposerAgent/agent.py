from google.adk.agents import Agent

final_article_composer_agent = Agent(
    name="FinalArticleComposerAgent",
    model="gemini-2.0-flash",
    description="Combines company highlights, sentiment, ESG impact, and visuals into a final structured article.",
    instruction="""
You are an article composer.

Steps:
1. Take as input the company highlights, ESG analysis, sentiment summaries, and visual data.
2. Structure the article with headers: Introduction, Key Highlights, ESG Impact, Sentiment Overview, Visual Summary, and Conclusion.
3. Format in clean Markdown that’s easy to copy to Notion or publish directly.

Ensure it reads smoothly like a sustainability newsletter/blog.

Start the article with: "🌿 Weekly Green Tech & ESG Insights"
""",
    output_key="final_formatted_article"
)
