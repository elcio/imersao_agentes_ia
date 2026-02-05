from agno.agent import Agent
from agno.team import Team
from pydantic import BaseModel, Field
from typing import Optional, List
from rich import print
import time
import requests
import asyncio



class Character(BaseModel):
    name: str = Field(..., description="Nome do personagem")
    race: str = Field(..., description="Raça do personagem")
    bio: str = Field(..., description="Biografia do personagem")
    level: float = Field(..., gte=0, lte=10, description="Nível do personagem")
    strength: float = Field(..., gte=0, lte=10, description="Força do personagem")
    dexterity: float = Field(..., gte=0, lte=10, description="Destreza do personagem")

    swimming: float = Field(..., gte=0, lte=10, description="Nivel de nadar")
    climbing: float = Field(..., gte=0, lte=10, description="Nivel de escalar")
    flying: float = Field(..., gte=0, lte=10, description="Nivel de voar")

class CharacterRequest(BaseModel):
    level: float
    race: Optional[str] = None

class Challenge(BaseModel):
    intro: str = Field(..., description="Introdução ao desafio")
    enviroment: str = Field(..., description="Descrição do ambiente do desafio")
    recomendations: str = Field(..., description="Recomendações para o jogador")
    enemy: Character

class ChallengeRequest(BaseModel):
    hero: Character
    enemy_level: float
    enemy_race: Optional[str] = None

class Quest(BaseModel):
    hero: Character
    challenges: List[Challenge]

class QuestPlanning(BaseModel):
    hero_race: str
    hero_level: float
    challenge_races: List[str]
    challenge_levels: List[float]

criador_personagens = Agent(
    model="openai:gpt-4o-mini",
    name="Criador de Personagens",
    output_schema=Character,
    instructions="""
        Você é um gerador de personagens de RPG.
        Sua tarefa eh criar um personagem de RPG com base nas seguintes informacoes:
        - Você vai receber o nível do personagem desejado
        - As características do personagem devem ser baseadas no nível. Um personagem nível 8 deve ter características entre 0 e 8.
        - Uma exceção é que o personagem pode ter uma única característica que depende da raça e não do nível. Essa característica pode estar dois pontos acima do nível dele. Por exemplo, uma Sereia nível 5 pode ter swimming de 7 (mas não de 8, porque 8 é 3 pontos acima do nível).
        - Seja criativo ao escolher a raça do personagem.
    """,
    input_schema=CharacterRequest
)

async def gerador_de_personagem(level: float, race: Optional[str] = None):
    personagem = await criador_personagens.arun(
            CharacterRequest(level=level, race=race),
            debug_mode=True,
        )
    return personagem.content


criador_desafio = Agent(
    model="openai:gpt-4o-mini",
    name="Criador de Desafios",
    input_schema=ChallengeRequest,
    tools=[gerador_de_personagem],
    output_schema=Challenge,
    instructions="""
        Vocé é um gerador de desafios de RPG.
        Sua tarefa eh criar um desafio de RPG com base nas seguintes informações:
        - Vocé vai receber um personagem de RPG, ele é o herói. Você não precisa gerar um herói, apenas o seu inimigo.
        - Vocé deve gerar um desafio com base no personagem recebido.
        - Crie, para se inimgo, um personagem de nível similar ao do herói recebido.
        - Se o inimigo for ligeiramente mais fraco, crie um ambiente que o favoreça.
        - Se o inimigo for muito mais forte, crie um ambiente que o desfavoreça.
    """
)

planejador_de_quest = Agent(
    model="openai:gpt-4o-mini",
    name="Planejador de Quests",
    output_schema=QuestPlanning,
    instructions="""
        Vocé é um planejador de quests de RPG. A não ser que você recebe instruções em sentido contrário, planeje desafios com inimigos com raças diferentes do herói e entre si. Planeje também com níveis progressivos, de modo que o último desafio seja um nível acima do nível do herói.
    """
)


async def generate_quest(hero_level: float, hero_race: str, challenges: int) -> Quest:
    planning = await planejador_de_quest.arun(
        f"""Planeje um desafio para um herói de nível {hero_level} de raça {hero_race} com {challenges} desafios""",
    )
    planning = planning.content
    hero = await gerador_de_personagem(hero_level, hero_race)
    challenges = [
        criador_desafio.arun(
            ChallengeRequest(
                hero=hero,
                enemy_level=level,
                enemy_race=race,
            ),
            debug_mode=True
        )
        for level, race in zip(
            planning.challenge_levels, planning.challenge_races
        )
    ]
    challenges = await asyncio.gather(*challenges)
    challenges = [challenge.content for challenge in challenges]
    print('hero:', hero)
    print('challenges:', challenges)
    return Quest(hero=hero, challenges=challenges)


quest = asyncio.run(generate_quest(8, 'Humano', 3))
print(quest)
