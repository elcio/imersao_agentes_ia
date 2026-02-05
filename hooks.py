from agno.exceptions import InputCheckError, CheckTrigger
from agno.run.agent import RunInput
from agno.agent import Agent
from agno.utils.log import logger
import re

def valida_cpf(cpf: str) -> bool:
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        return False

    numbers = [int(digit) for digit in cpf if digit.isdigit()]
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True


def detect_pii(run_input: RunInput, agent: Agent, debug_mode: bool):
    content = run_input.input_content
    cpfs = re.findall(r'\d{3}\.\d{3}\.\d{3}-\d{2}', content)
    for cpf in cpfs:
        if valida_cpf(cpf):
            content = content.replace(cpf, '******')
            if debug_mode:
                logger.debug(f'Masking CPF {cpf}')
        else:
            if debug_mode:
                logger.debug(f'Not a CPF {cpf}')
    run_input.input_content = content

