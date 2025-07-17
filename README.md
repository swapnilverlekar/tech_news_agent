# 🌿 Sustainable Tech News Aggregator & Insight Engine
A multi-agent system built using Google ADK (Agent Development Kit) to automatically fetch, analyze, and publish weekly summaries of clean tech innovations, ESG sentiment, and carbon impact trends. The final articles are auto-formatted and published to a Notion page using MCP (Model Context Protocol).

## 🚀 Project Highlights
- ✅ Aggregates real-time news on sustainability, ESG, clean energy, and carbon neutrality

- 🧠 Analyzes carbon impact and public ESG sentiment

- 📊 Generates visual summaries (ESG score charts, sentiment graphs)

- 📝 Composes well-structured Markdown articles

- 📥 Publishes directly to Notion using Notion MCP Server

## 💡 Motivation
As climate-tech and sustainable investing continue to grow, there's a need for automated, high-quality summaries that keep readers, professionals, and businesses informed. This project demonstrates how multi-agent systems can intelligently monitor sustainability news and transform unstructured data into digestible insights.

## 🧱 Architecture Overview

    A[NewsAggregatorBuilder (Root Sequential Agent)]
    A --> B[FetchContentParallelAgent]
    B --> B1[GreenTechNewsFetcherAgent]
    B --> B2[CarbonImpactAnalyzerAgent]
    B --> B3[SocialESGSentimentAgent]
    A --> C[InsightBuilderSequentialAgent]
    C --> C1[CompanyHighlightBuilderAgent]
    C --> C2[VisualSummaryGeneratorAgent]
    C --> C3[FinalArticleComposerAgent]
    A --> D[PostOnNotionAgent]

## 🧠 Agent Breakdown
|Agent|	Type|	Role|
|---|---|---|
|NewsAggregatorBuilder|	Sequential|	Orchestrates the entire pipeline|
|FetchContentParallelAgent|	Parallel|	Fetches news, ESG data, and sentiment in parallel|
|GreenTechNewsFetcherAgent|	Leaf|	Searches latest clean tech news using google_search|
|CarbonImpactAnalyzerAgent|	Leaf|	Evaluates environmental impact and ESG metrics from articles|
|SocialESGSentimentAgent|	Leaf|	Scrapes Reddit/Twitter sentiment on ESG topics|
|InsightBuilderSequentialAgent|	Sequential|	Builds company highlights, visuals, and final summary|
|CompanyHighlightBuilderAgent|	Leaf|	Identifies notable companies/projects and writes summaries|
|VisualSummaryGeneratorAgent|	Leaf|	Outputs JSON-ready data for visualizing ESG scores/sentiments|
|FinalArticleComposerAgent|	Leaf|	Combines all content into one formatted article|
|PostOnNotionAgent|	Leaf|	Posts the final article to a Notion page using MCP protocol|

## 🛠️ Tech Stack
- Google ADK – Agent orchestration and execution

- Gemini 2.0 Flash / Pro – For all agent reasoning and summarization

- Google Search Tool – News gathering

- MCP Toolset + Notion MCP Server – Article publishing to Notion

- Python 3.10+

## 📦 Project Structure

```
sustainable_news_agents/
└── NewsAggregatorBuilder/
    ├── __init__.py
    ├── agent.py                  # Root Sequential Agent
    └── sub_agents/
        ├── FetchContentParallelAgent/
        │   └── sub_agents/
        │       ├── GreenTechNewsFetcherAgent/
        │       ├── CarbonImpactAnalyzerAgent/
        │       └── SocialESGSentimentAgent/
        ├── InsightBuilderSequentialAgent/
        │   └── sub_agents/
        │       ├── CompanyHighlightBuilderAgent/
        │       ├── VisualSummaryGeneratorAgent/
        │       └── FinalArticleComposerAgent/
        └── PostOnNotionAgent/
```

## 🧪 Setup & Execution

### 1. Clone the Repository
```
git clone https://github.com/yourusername/sustainable-news-agents.git
cd sustainable-news-agents
```
### 2. Setup Python Environment
```
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Configure Environment
Set your Notion credentials in a .env or export:

```
export NOTION_API_KEY="your_notion_integration_secret"
```
### 4. Run MCP Server Locally
```
npx -y @notionhq/notion-mcp-server
```
### 5. Run the Main Agent
```
from sustainable_news_agents.NewsAggregatorBuilder.agent import news_aggregator_root_agent
output = news_aggregator_root_agent.run()
print(output)
```

## 📖 Example Output
```
🌿 Weekly Green Tech & ESG Insights

## 🏢 Top Highlights
- Tesla invests in solid-state battery technology...
- Enpal scales rooftop solar access in Germany...

## 🌱 ESG Impact
- Enpal expected to cut ~2.1M tons CO2 over next 5 years...
- Tesla’s battery division rates high in environmental transparency...

## 📊 Visual Summary
- [ESG Score Chart here]
- [Sentiment Pie Chart here]

## 🔍 Social Sentiment
- "Tesla" – Highly Positive (Trending on Twitter)
- "Carbon Credit" – Mixed (Skepticism on Reddit)

✅ POST IS COMPLETED to Notion
```

## 🤝 Contributing
We welcome PRs, discussions, and improvements!

Fork the repo

Create a new branch (feature/agent-name)

Submit a pull request

## 📄 License
MIT License © 2025 Swapnil Verlekar

📬 Contact
Swapnil Verlekar
For collaboration, drop a message or open an issue!

