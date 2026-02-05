from agno.agent import Agent
from agno.media import Image
from agno.tools.dalle import DalleTools
from rich import print
import requests

vidente = Agent(
    model='openai:gpt-4o-mini',
    tools=[DalleTools()],
    instructions="Se o usuário pedir para gerar uma imagem, use as ferramentas do DALL-E."
)

resp = vidente.run(
    'Essa imagem é uma foto ou é gerada por IA?',
    images=[
        Image(filepath='imagem.jpg')
    ],
)

print(resp.content)


# resp = vidente.run(
#     'Gere uma imagem com a seguinte descrição: "A imagem mostra um arco tradicional de estilo oriental, possivelmente um portal de entrada para um mercado ou templo. O arco é adornado com detalhes coloridos e inscrições em uma língua asiática. Ao fundo, é possível ver edifícios altos e uma área movimentada, indicando que está localizado em um ambiente urbano. A iluminação sugere que é durante o dia, com céu claro e ensolarado."',
# )
# 
# print(resp.content)
# 
# if resp.images:
#     try:
#         with open('output.png', 'wb') as f:
#             if resp.images[0].content:
#                 f.write(resp.images[0].content)
#             elif resp.images[0].url:
#                 f.write(requests.get(resp.images[0].url).content)
#             else:
#                 raise TypeError('Nenhuma imagem encontrada')
#     except TypeError:
#         print(resp.images[0])
