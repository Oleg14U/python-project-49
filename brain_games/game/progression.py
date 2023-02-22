from random import randint


DESCRIPTION = 'What number is missing in the progression?'
MIN_NUMBER_STEP = 1  # Min step
MAX_NUMBER_STEP = 5  # Max step
START_NUMBER = randint(1, 20)  # Initial number
STOP_NUMBER = randint(60, 100)  # End number
LENGTH = 10  # Amount of numbers


def generate_progression(start, stop, step):
    progression = list(range(start, stop, step))[:LENGTH]
    return progression


def generate_round():
    step = randint(MIN_NUMBER_STEP, MAX_NUMBER_STEP)
    progression = generate_progression(START_NUMBER, STOP_NUMBER, step)
    index = randint(0, len(progression) - 1)
    correct_answer = progression[index]
    progression[index] = '..'
    question = ' '.join(str(i) for i in progression)
    return question, str(correct_answer)
