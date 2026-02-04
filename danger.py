import os
from agno.learn import LearningMachine
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from rich import print
from typing import Any, Callable, Dict
from agno.tools import tool

db = SqliteDb("danger.sqlite")

with open('instructions.txt', 'r') as f:
    instructions = f.read()


def validate_cmd(function_name: str, function_call: Callable,
                 arguments: Dict[str, Any]):
    command = arguments['cmd']
    if ';' in command:
        return False
    if '&' in command:
        return False
    if '$(' in command:
        return False
    if '`' in command:
        return False
    if ' and ' in command:
        return False
    if ' or ' in command:
        return False
    if '>' in command:
        return False
    allowed = ['ls', 'cat', 'date', 'echo', 'ps', 'pwd', 'whoami']
    if command.split()[0] not in allowed:
        confirm = input(f'Are you sure you want to run {command}? (yes/no) ')
        if confirm != 'yes':
            return False
    result = function_call(**arguments)
    return result


@tool(tool_hooks=[validate_cmd], stop_after_tool_call=True)
def run_cmd(cmd):
    return os.popen(cmd).read()


agent = Agent(
    name="Vivi",
    model="openai:gpt-4o-mini",
    db=db,
    add_history_to_context=True,
    num_history_runs=5,
    tools=[run_cmd],
    update_memory_on_run=True,
    instructions='''Você é um assistente pessoal virtual que tem acesso ao computador do usuário. Você pode interagir com o computador executando comandos shell.''',
)


if __name__ == "__main__":
    user_id = input('E-mail: ') or 'elcio@visie.com.br'
    agent.cli_app(stream=True, debug_mode=True, user_id=user_id)
