from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from rich import print
from kbase import knowledge as visie_kb
from kbase2 import knowledge as agente_kb
from agno.team import Team

db = SqliteDb("agent.sqlite")

agent = Agent(
    name="Gepete",
    db=db,
    add_history_to_context=True,
    num_history_runs=5,
    knowledge=visie_kb,
    instructions="""Você é um agente especializado que deve SEMPRE consultar a base de conhecimentos. Se a informação que o usuário busca não estiver na base de conhecimentos, não responda, mesmo que você saiba a resposta."""
)


agent2 = Agent(
    name="Agente2",
    db=db,
    add_history_to_context=True,
    num_history_runs=5,
    knowledge=agente_kb,
    instructions="""Você é um agente especializado que deve SEMPRE consultar a base de conhecimentos. Se a informação que o usuário busca não estiver na base de conhecimentos, não responda, mesmo que você saiba a resposta."""
)


team = Team(
    model="openai:gpt-4o-mini",
    members=[agent, agent2],
    respond_directly=True,
    determine_input_for_members=False,
    instructions="""
    Consulte os membros do time para obter respostas, mas não avise o usuário.
    Se ele perguntar sobre tecnologia, desenvolvimento de software, sites, e-commerce ou sobre a Visie, consulte o Gepete.
    Se ele perguntar sobre cinema, consulte o Agente 2.
    """
)


if __name__ == "__main__":
    team.cli_app(stream=True, debug_mode=True)
