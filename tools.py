import requests
from enum import Enum
from agno.tools import tool
from feedparser import parse
import time


class Assuntos(Enum):
    sites = 'sites'
    sistemas = 'sistemas'
    ousourcing = 'ousourcing'
    treinamento = 'treinamento'
    outros = 'outros'

def envia_contato(nome:str, sobrenome:str, email:str, celular:str,
                  assunto: Assuntos, mensagem: str) -> bool:
    """
    Envia um contato para a Visie.
    """
    url = 'https://m.visie.com.br/form/submit?formId=82'
    data = {
        'mauticform[nome]': nome,
        'mauticform[sobrenome]': sobrenome,
        'mauticform[email_corporativo]': email,
        'mauticform[numero_de_telefone]': celular,
        'mauticform[nome_da_empresa]': '',
        'mauticform[como_a_visie_pode_te_ajud1]': assunto,
        'mauticform[mensagem]': mensagem,
        'mauticform[formId]': '82',
        'mauticform[return]': 'https://visie.com.br/',
        'mauticform[formName]': 'contatosite',
        'mauticform[messenger]': '1',
    }
    response = requests.post(url, data=data)
    return True

@tool(stop_after_tool_call=True)
def manifesto():
    """Devolve o manifesto ágil"""
    return """
# Manifesto para Desenvolvimento Ágil de Software

Estamos descobrindo maneiras melhores de desenvolver
software, fazendo-o nós mesmos e ajudando outros a
fazerem o mesmo. Através deste trabalho, passamos a valorizar:

Indivíduos e interações mais que processos e ferramentas
Software em funcionamento mais que documentação abrangente
Colaboração com o cliente mais que negociação de contratos
Responder a mudanças mais que seguir um plano

Ou seja, mesmo havendo valor nos itens à direita,
valorizamos mais os itens à esquerda.
    """


@tool(cache_results=True, cache_dir="cache", cache_ttl=300)
def lista_blog() -> list:
    """Devolve uma lista dos últimos posts do blog da Visie"""
    time.sleep(5)
    posts = parse('https://visie.com.br/feed/')
    return [
            {
                'title': post['title'],
                'link': post['link'],
                'summary': post['summary'],
            }
            for post in posts['entries']
        ]


