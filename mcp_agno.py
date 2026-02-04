import asyncio
from agno.agent import Agent
from agno.tools.mcp import MCPTools
from agno.db.sqlite import SqliteDb
from agno.learn import LearningMachine
from rich import print
from kbase import knowledge
from agno.tools.wikipedia import WikipediaTools
from tools import manifesto, lista_blog

db = SqliteDb("agent.sqlite")

with open('instructions.txt', 'r') as f:
    instructions = f.read()


async def main():
    mcp = MCPTools(transport="streamable-http", url="http://127.0.0.1:9000/mcp")
    agent = Agent(
        name="Vivi",
        model="openai:gpt-4o-mini",
        db=db,
        add_history_to_context=True,
        num_history_runs=5,
        knowledge=knowledge,
        tools=[WikipediaTools(), manifesto, lista_blog, mcp],
        learning=LearningMachine(
            knowledge=knowledge,
            learned_knowledge=True,
        ),
        instructions=instructions,
    )
    user_id = input('E-mail: ') or 'elcio@visie.com.br'
    await agent.acli_app(stream=True, user_id=user_id)


asyncio.run(main())

