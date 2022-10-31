from random import randint, choice

LOWER_LIMIT = 1
UPPER_LIMIT = 100
DESCRIPTION = 'What is the result of the expression?'
SIGNS = ['+', '-', '*']


def get_task():
    first_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    second_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    sign = choice(SIGNS)
    question = f'{first_number} {sign} {second_number}'
    correct_answer = str(get_result(first_number, sign, second_number))
    return question, correct_answer


def get_result(first_num, sign, second_num):
    if sign == '+':
        result = first_num + second_num
    elif sign == '-':
        result = first_num - second_num
    else:
        result = first_num * second_num
    return result
