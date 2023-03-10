from random import randint

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 10


def is_prime(num):
    if num <= 1:
        return False
    divider = 2
    while num % divider != 0:
        divider += 1
    return divider == num


def generate_game():
    num = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_prime(num) else 'no'
    return str(num), correct_answer
