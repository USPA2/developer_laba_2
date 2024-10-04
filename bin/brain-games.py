from src.engine import run_game
from src.games.lcm_game import generate_numbers
from src.games.progression_game import generate_progression_answer
from src.cli import greet_user

def main():
    name = greet_user()
    run_game(generate_numbers, 'Find the smallest common multiple of given numbers.', name)
    run_game(generate_progression_answer, 'What number is missing in the progression?', name)

if __name__ == "__main__":
    main()