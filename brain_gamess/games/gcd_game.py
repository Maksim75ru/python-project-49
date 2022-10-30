from random import randint

LOWER_LIMIT = 1
UPPER_LIMIT = 100
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_task():
    first_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    second_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = f'{first_number} {second_number}'
    correct_answer = str(get_gcd(first_number, second_number))
    return question, correct_answer


def get_gcd(first_num, second_num):
    big_num = max(first_num, second_num)
    small_num = min(first_num, second_num)
    while big_num % small_num != 0:
        big_num, small_num = small_num, big_num % small_num
    return small_num
