

import random
import prompt


def welcome():
    print('Welcome to the Brain Games!')


def yours_name():
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    return name


def is_even_number(num):
    return num % 2 == 0


def logic_answer(answer, num):
    if (is_even_number(num) is True and answer == "yes"):
        return True
    elif (is_even_number(num) is False and answer == "no"):
        return True


def game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        num = random.randint(1, 100)
        print(f"Question: {num}")
        answer = input("Your answer: ")
        result = False
        result = logic_answer(answer, num)
        if (result is True):
            print("Correct!")
        else:
            print(f"{answer}  is wrong answer ;(. Correct answer was {result}")
            return f"Let's try again, {name}!"
    return f"Congratulations, {name}!"

