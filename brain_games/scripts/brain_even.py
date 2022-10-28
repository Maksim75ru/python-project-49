#!/usr/bin/env python3

import prompt
from random import randint


LOWER_LIMIT = 0
UPPER_LIMIT = 100


def check_even():
    count = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        random_number = randint(LOWER_LIMIT, UPPER_LIMIT)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')
        if random_number % 2 == 0 and user_answer == 'yes':
            print('Correct!')
            count += 1
        elif random_number % 2 != 0 and user_answer == 'no':
            print('Correct!')
            count += 1
        else:
            print(f'"{user_answer}" is wrong answer ;(. Correct answer was '
                  f'{"yes" if random_number % 2 == 0 else "no"}.')
            print(f"Let's try again, {name}")
            break
    if count == 3:
        print(f'Congratulations, {name}')


def main():
    print("Welcome to the Brain Games!")
    check_even()


if __name__ == '__main__':
    main()
