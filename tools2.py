import math
from agno.agent import Agent
from pydantic import BaseModel, Field
from rich import print


class BaskaraInput(BaseModel):
    a: float
    b: float
    c: float

class BaskaraOutput(BaseModel):
    x1: float|None
    x2: float|None

class BaskaraSolution(BaseModel):
    explanation: str = Field(description="Explicação muito breve do resultado")
    x1: float|None
    x2: float|None


def baskara(a: float, b: float, c: float) -> BaskaraOutput:
    """
    Calcula as raízes de uma equação do segundo grau.
    """
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return BaskaraOutput(x1=None, x2=None)
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return BaskaraOutput(x1=x1, x2=x2)

agent = Agent(
    model='openai:gpt-4o-mini',
    tools=[
        baskara
    ],
    input_schema=BaskaraInput,
    output_schema=BaskaraSolution,
    instructions="""
    Você é um assistente que calcula as raízes de uma equação do segundo grau.
    """
)

resp=agent.run(BaskaraInput(a=1, b=2, c=3), debug_mode=True)
resp=agent.run(BaskaraInput(a=4, b=0, c=-4), debug_mode=True)

print(resp.content)
