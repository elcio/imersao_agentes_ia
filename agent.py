from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from rich import print
from kbase import knowledge

db = SqliteDb("agent.sqlite")

agent = Agent(
    name="Gepete",
    model="openai:gpt-4o-mini",
    db=db,
    add_history_to_context=True,
    num_history_runs=5,
    knowledge=knowledge,
    instructions="""Você é um agente especializado que deve SEMPRE consultar a base de conhecimentos. Se a informação que o usuário busca não estiver na base de conhecimentos, não responda, mesmo que você saiba a resposta."""
)


if __name__ == "__main__":
    agent.cli_app(stream=True, debug_mode=True)
