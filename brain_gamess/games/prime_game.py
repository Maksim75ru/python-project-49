from random import randint

LOWER_LIMIT = 1
UPPER_LIMIT = 100
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_task():
    number = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = number
    if get_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def get_prime(num):
    flag = True
    if num == 2:
        return flag
    index = 2
    de = num**0.5
    while index <= de:
        if num % index == 0:
            flag = False
        index += 1
    return flag
