import requests
import json
from rich import print

url = 'http://127.0.0.1:8000/agents/danger/runs'
data = {
    'message': 'apague o arquivo hacker/novo_arquivo.txt',
    'stream': 'false',
    'session_id': 'teste'
}

response = requests.post(url, data=data)

data = response.json()

data['tools'][0]['confirmed'] = True

tools = json.dumps(data['tools'])

url = f'http://127.0.0.1:8000/agents/danger/runs/{data["run_id"]}/continue'

data = {
    'tools': tools,
    'stream': 'false',
    'session_id': 'teste'
}

response = requests.post(url, data=data)

data = response.json()

print(data)
