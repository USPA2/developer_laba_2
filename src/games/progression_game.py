import random

def generate_progression(length, start, step):
    return [start + i * step for i in range(length)]

def generate_progression_answer():
    length = random.randint(5, 10)
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    progression = generate_progression(length, start, step)
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    return ' '.join(map(str, progression)), correct_answer