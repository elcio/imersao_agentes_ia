from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.learn import LearningMachine
from rich import print
from kbase import knowledge
from agno.tools.wikipedia import WikipediaTools

db = SqliteDb("agent.sqlite")

agent = Agent(
    name="Gepete",
    model="openai:gpt-4o-mini",
    db=db,
    add_history_to_context=True,
    num_history_runs=5,
    knowledge=knowledge,
    tools=[WikipediaTools()],
    learning=LearningMachine(
        knowledge=knowledge,
        learned_knowledge=True,
    # update_memory_on_run=True,
    # enable_agentic_memory=True,
    ),
    instructions="""
    Você é um agente especializado que deve SEMPRE consultar a base de conhecimentos.

    Se a informação que o usuário busca não estiver na base de conhecimentos, busque na Wikipedia. Sempre aprenda com o conteúdo que você trouxer da Wikipedia. Extraia, se possível, pelo menos três fatos para aprender cada vez que fizer uma busca lá.

    Se não achar nada lá, não responda, mesmo que você saiba a resposta. Se o usuário te disser fatos, confie nele, a não ser que ele contradiga algo que está na base de conhecimento. Nossos usuários costumam estar bem informados, aprenda com eles.""",
)


if __name__ == "__main__":
    user_id = input('E-mail: ') or 'elcio@visie.com.br'
    agent.cli_app(stream=True, debug_mode=True, user_id=user_id)
