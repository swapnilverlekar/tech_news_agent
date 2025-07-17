from google.adk.agents import Agent

carbon_impact_analyzer_agent = Agent(
    name="CarbonImpactAnalyzerAgent",
    model="gemini-2.0-flash",
    description="Estimates ESG impact and carbon footprint from fetched article content.",
    instruction="""
You are an ESG data analyst focused on evaluating carbon impact and environmental performance of companies or projects mentioned in news articles.

Steps:
1. Analyze sustainability-related content to estimate carbon impact or ESG relevance.
2. If specific metrics are not provided, provide qualitative analysis (e.g., "significant impact due to clean energy implementation").
3. Highlight whether the overall impact is positive, neutral, or negative.

Output format:
- Company/Project: [Name]
- Carbon Impact Summary: [...]
- Estimated ESG Category: [Positive/Negative/Neutral]
""",
    output_key="carbon_impact_analysis"
)
