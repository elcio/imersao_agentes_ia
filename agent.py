from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.learn import LearningMachine
from rich import print
from kbase import knowledge
from agno.tools.wikipedia import WikipediaTools
from tools import envia_contato, manifesto, lista_blog

db = SqliteDb("agent.sqlite")

with open('instructions.txt', 'r') as f:
    instructions = f.read()

agent = Agent(
    name="Vivi",
    model="openai:gpt-4o-mini",
    db=db,
    add_history_to_context=True,
    num_history_runs=5,
    knowledge=knowledge,
    tools=[WikipediaTools(), envia_contato, manifesto, lista_blog],
    learning=LearningMachine(
        knowledge=knowledge,
        learned_knowledge=True,
    ),
    instructions=instructions,
)


if __name__ == "__main__":
    user_id = input('E-mail: ') or 'elcio@visie.com.br'
    agent.cli_app(stream=True, debug_mode=True, user_id=user_id)
