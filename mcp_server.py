import requests
from fastmcp import FastMCP
from enum import Enum

mcp = FastMCP('MyShinningTools')

class Assuntos(Enum):
    sites = 'sites'
    sistemas = 'sistemas'
    ousourcing = 'ousourcing'
    treinamento = 'treinamento'
    outros = 'outros'

@mcp.tool
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


if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=9000)
