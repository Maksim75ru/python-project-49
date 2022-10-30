from random import randint


LOWER_LIMIT = 1
UPPER_LIMIT = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_task():
    number = randint(LOWER_LIMIT, UPPER_LIMIT)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = number
    return question, correct_answer


def is_even(num):
    return num % 2 == 0
