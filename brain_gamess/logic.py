import prompt
from .cli import welcome_user

SCORE = 3


def games_result(game):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game.DESCRIPTION)
    count = 0

    for i in range(SCORE):
        question, correct_answer = game.get_task()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            count += 1
        else:
            print(f'"{user_answer}" is wrong answer ;(.'
                  f' Correct answer was {correct_answer}.')
            print(f"Let's try again, {name}!")
            break

    if count == 3:
        print(f'Congratulations, {name}!')
