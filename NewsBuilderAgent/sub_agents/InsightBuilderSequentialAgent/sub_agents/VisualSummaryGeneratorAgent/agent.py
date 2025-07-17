from google.adk.agents import Agent

visual_summary_generator_agent = Agent(
    name="VisualSummaryGeneratorAgent",
    model="gemini-2.0-flash",
    description="Prepares data for visual summaries like ESG score charts or sector impact graphs.",
    instruction="""
You are a data summarizer responsible for preparing visual-ready summaries.

Steps:
1. From previous outputs, extract measurable elements (e.g., ESG score, mention counts, sentiment).
2. Format as JSON array for plotting.

Example Output:
{
  "esg_scores": {
    "Tesla": 82,
    "Plug Power": 74,
    "First Solar": 89
  },
  "sentiment_distribution": {
    "Positive": 62,
    "Neutral": 25,
    "Negative": 13
  }
}
""",
    output_key="visual_data_summary"
)
