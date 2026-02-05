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
    result = function_call(**arguments)
    return result


def validate_safe_cmd(function_name: str, function_call: Callable,
                      arguments: Dict[str, Any]):
    command = arguments['cmd']
    allowed = ['ls', 'cat', 'date', 'echo', 'ps', 'pwd', 'whoami']
    if command.split()[0] not in allowed:
        return False
    result = function_call(**arguments)
    return result


@tool(tool_hooks=[validate_cmd, validate_safe_cmd])
def run_safe_cmd(cmd):
    """Run a command that starts with ls, cat, date, echo, ps, pwd or whoami"""
    return os.popen(cmd).read()

@tool(requires_confirmation=True, tool_hooks=[validate_cmd])
def run_cmd(cmd):
    """Run any shell command, asking for user confirmation"""
    return os.popen(cmd).read()


agent = Agent(
    name="Danger",
    model="openai:gpt-4o-mini",
    db=db,
    add_history_to_context=True,
    num_history_runs=5,
    tools=[run_safe_cmd, run_cmd],
    update_memory_on_run=True,
    instructions='''Você é um assistente pessoal virtual que tem acesso ao computador do usuário. Você pode interagir com o computador executando comandos shell. Prefira, quando possível, executar comandos considerados seguros, usando a tool run_safe_cmd.''',
)


if __name__ == "__main__":
    user_id = input('E-mail: ') or 'elcio@visie.com.br'
    agent.cli_app(stream=True, debug_mode=True, user_id=user_id)
