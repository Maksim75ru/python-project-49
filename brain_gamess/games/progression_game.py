from random import randint


LOWER_LIMIT = 1
UPPER_LIMIT = 100
DESCRIPTION = 'What number is missing in the progression?'


def get_task():
    elements = get_progression(LOWER_LIMIT, UPPER_LIMIT)
    length_elements = len(elements)
    hide_elem = randint(0, length_elements)
    correct_answer = str(elements[hide_elem - 1])
    elements[hide_elem - 1] = '..'
    question = ' '.join(str(i) for i in elements)
    return question, correct_answer


def get_progression(start_num: int, finish_num: int):
    min_amount_elements = 5
    max_amount_elements = 9
    amount_elements = randint(min_amount_elements, max_amount_elements)

    first_elem = randint(start_num, finish_num)
    step = randint(start_num, finish_num)
    progression = [first_elem]
    for i in range(amount_elements):
        progression.append(progression[-1] + step)
    return progression
