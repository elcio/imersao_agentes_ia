from agno.agent import Agent
from agno.team import Team
from pydantic import BaseModel, Field
from typing import Optional, List
from rich import print
from agno.tools.dalle import DalleTools
import time
import requests


desenhista = Agent(
    model='openai:gpt-4o-mini',
    tools=[DalleTools()],
    instructions="Você é um gerador de imagens para um jogo de RPG. Você vai receber descrições de personagens e deve gerar uma imagem de corpo inteiro do personagem. Ele deve estar de pé. O fundo da imagem deve ser preto."
)

def gerar_imagem_personagem(bio: str) -> str:
    """Gera uma imagem de um personagem de RPG e devolve o nome do arquivo"""
    resp = desenhista.run(bio, debug_mode=True)
    filename = f'img/output_{time.time()}.png'
    if resp.images:
        try:
            with open(filename, 'wb') as f:
                if resp.images[0].content:
                    f.write(resp.images[0].content)
                elif resp.images[0].url:
                    f.write(requests.get(resp.images[0].url).content)
                else:
                    raise TypeError('Nenhuma imagem encontrada')
        except TypeError:
            print(resp.images[0])
            raise
    return filename

class Character(BaseModel):
    name: str = Field(..., description="Nome do personagem")
    race: str = Field(..., description="Raça do personagem")
    bio: str = Field(..., description="Biografia do personagem")
    image: str = Field(..., description="Caminho do arquivo da imagem do personagem")
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
    intro: str
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
        - Devolta em branco o campo image.
    """,
    input_schema=CharacterRequest
)

def gerador_de_personagem(level: float, race: Optional[str] = None):
    personagem = criador_personagens.run(
            CharacterRequest(level=level, race=race),
            debug_mode=True,
        ).content
    personagem.image = gerar_imagem_personagem(personagem.bio)
    return personagem


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


def generate_quest(hero_level: float, hero_race: str, challenges: int) -> Quest:
    planning = planejador_de_quest.run(
        f"""Planeje um desafio para um herói de nível {hero_level} de raça {hero_race} com {challenges} desafios""",
    ).content
    hero = gerador_de_personagem(hero_level, hero_race)
    challenges = [
        criador_desafio.run(
            ChallengeRequest(
                hero=hero,
                enemy_level=level,
                enemy_race=race,
            ),
            debug_mode=True
        ).content
        for level, race in zip(
            planning.challenge_levels, planning.challenge_races
        )
    ]
    print('hero:', hero)
    print('challenges:', challenges)
    return Quest(hero=hero, challenges=challenges)


quest = generate_quest(8, 'Humano', 3)
print(quest)
