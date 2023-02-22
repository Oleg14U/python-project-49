from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 10
OPERATORS = ['+', '-', '*']


def calculate(num_one, num_two, sign):
    if sign == '+':
        correct_answer = num_one + num_two
        return correct_answer
    elif sign == '-':
        correct_answer = num_one - num_two
        return correct_answer
    elif sign == '*':
        correct_answer = num_one * num_two
        return correct_answer


def generate_round():
    num_one = randint(MIN_NUMBER, MAX_NUMBER)
    num_two = randint(MIN_NUMBER, MAX_NUMBER)
    sign = choice(OPERATORS)
    question = f'{num_one} {sign} {num_two}'
    correct_answer = calculate(num_one, num_two, sign)
    return question, str(correct_answer)
