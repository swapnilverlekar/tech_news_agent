import json
import os

from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

# ---- MCP Server and Notion Docs ----
# MCP: https://github.com/modelcontextprotocol/servers
# Notion MCP Server: https://github.com/makenotion/notion-mcp-server
# Notion OpenAPI: https://github.com/makenotion/notion-mcp-server/blob/main/scripts/notion-openapi.json

# ---- CONFIG ----
NOTION_API_KEY = "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"  # replace with secret manager in prod

if NOTION_API_KEY is None:
    raise ValueError("NOTION_API_KEY is not set")

NOTION_MCP_HEADERS = json.dumps(
    {"Authorization": f"Bearer {NOTION_API_KEY}", "Notion-Version": "2022-06-28"}
)

# ---- FINAL AGENT ----
post_on_notion_agent = Agent(
    name="PostOnNotionAgent",
    model="gemini-2.0-flash",
    description="Posts the final sustainability article to a specified Notion page using MCP protocol.",
    instruction="""
You are an assistant that posts sustainability articles to a Notion page using the MCP tool.

Inputs:
- The full article is stored in {final_formatted_article}
- The Notion page is located at: https://www.notion.so/Sustainability-Updates-2334e08db8a6809d9b03f7065611170f

Your task:
1. Extract a title from the first heading or opening sentence.
2. Format content using markdown-style headers and clean paragraphs.
3. Construct the correct JSON body for the POST request using Notion's block structure.
4. Use the MCP tool to submit the article to Notion.

JSON POST Template:
{
  "parent": { "type": "page_id", "page_id": "<NOTION_PAGE_ID>" },
  "properties": {
    "title": [{ "text": { "content": "<EXTRACTED_TITLE>" } }]
  },
  "children": [
    {
      "object": "block",
      "type": "paragraph",
      "paragraph": {
        "text": [{ "type": "text", "text": { "content": "<ARTICLE_BODY>" } }]
      }
    }
  ]
}

Output:
✅ POST IS COMPLETED to Notion
""",
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command="npx",
                args=["-y", "@notionhq/notion-mcp-server"],
                env={"OPENAPI_MCP_HEADERS": NOTION_MCP_HEADERS},
            )
        )
    ],
    output_key="notion_post_result"
)
