from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
import os
from dotenv import load_dotenv
from agno.tools.yfinance import YFinanceTools

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

web_agent=Agent(
    name="Web Agent",
    role="Search the Web for information",
    model=Groq(id="qwen/qwen3-32b"),
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources",
    show_tool_calls=True,
    markdown=True
)

finance_agent=Agent(
    name="Finance Agent",
    role="Get financial information",
    model=Groq(id="qwen/qwen3-32b"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True)],
    instructions="Use tables to display data",
    show_tool_calls=True,
    markdown=True
)

agent_team=Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="qwen/qwen3-32b"),
    instructions=["Always include the sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True
)
agent_team.print_response("Analyse companies like Tesla,Nvidia,Apple and suggest which to be best for long term investment.")