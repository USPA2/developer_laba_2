from src.cli import greet_user
def run_game(game_function, game_description, name):
    print(game_description)
    for _ in range(3):
        question, correct_answer = game_function()
        print(f'Question: {question}')
        user_answer = int(input('Your answer: '))
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")