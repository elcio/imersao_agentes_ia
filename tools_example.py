from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.learn import LearningMachine
from rich import print
from kbase import knowledge
from agno.tools.yfinance import YFinanceTools
from agno.tools.hackernews import HackerNewsTools

db = SqliteDb("agent.sqlite")

agent = Agent(
    name="FinancialAdvisor",
    model="openai:gpt-4o-mini",
    db=db,
    add_history_to_context=True,
    num_history_runs=5,
    tools=[YFinanceTools(), HackerNewsTools()],
    instructions="""Você é um agente que ajuda fazer pesquisa sobre investimentos. Ao receber um ticker procure por notícias que impactam o valor da ação e também pelo valor atual e outras informações sobre a ação. Devolva um relatório muito breve ao usuário com um prognóstico de futuro.""",
)


if __name__ == "__main__":
    user_id = input('E-mail: ') or 'elcio@visie.com.br'
    agent.cli_app(stream=True, debug_mode=True, user_id=user_id)
