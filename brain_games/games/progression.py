from random import randint


GAME_DESCRIPTION = 'What number is missing in the progression?'
MIN_NUMBER_STEP = 1
MAX_NUMBER_STEP = 5
START_NUMBER = randint(1, 20)
STOP_NUMBER = randint(60, 100)
LENGTH = 10


def generate_progression(start, stop, step):
    progression = list(range(start, stop, step))[:LENGTH]
    return progression


def generate_game():
    step = randint(MIN_NUMBER_STEP, MAX_NUMBER_STEP)
    progression = generate_progression(START_NUMBER, STOP_NUMBER, step)
    index = randint(0, len(progression) - 1)
    correct_answer = progression[index]
    progression[index] = '..'
    question = ' '.join(str(i) for i in progression)
    return question, str(correct_answer)
