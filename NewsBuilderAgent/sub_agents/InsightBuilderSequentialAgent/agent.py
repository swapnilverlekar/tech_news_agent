"""
InsightBuilderSequentialAgent

This sequential agent processes the fetched data to:
- Highlight the most impactful companies/projects
- Generate visual summaries
- Compose a final article
"""

from google.adk.agents import SequentialAgent
from .sub_agents.CompanyHighlightBuilderAgent import company_highlight_agent
from .sub_agents.VisualSummaryGeneratorAgent import visual_summary_generator_agent
from .sub_agents.FinalArticleComposerAgent import final_article_composer_agent

insight_builder_sequential_agent = SequentialAgent(
    name="InsightBuilderSequentialAgent",
    description="Builds insightful article sections, visuals, and a merged, formatted final post.",
    sub_agents=[
        company_highlight_agent,
        visual_summary_generator_agent,
        final_article_composer_agent
    ]
)
