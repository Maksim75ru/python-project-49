import prompt

SCORE = 3


def games_result(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
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
            print(f'"{user_answer}" is wrong answer ;(. Correct answer was {correct_answer}.')
            print(f"Let's try again, {name}")
            break

    if count == 3:
        print(f'Congratulations, {name}')
