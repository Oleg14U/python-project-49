from brain_games.game.even import yours_name
import random


def random_nember():
    return random.randint(1, 20)


def operators():
    operators = ("+", "*")
    return operators[random.randint(0, 1)]


def game(name):
    print("What is the result of the expression?")
    for i in range(0, 3):
        num_one = random_nember()
        num_two = random_nember()
        operator = operators()
        result = 0
        print("Question: " + str(num_one) + " " + operator + " " + str(num_two))
        answer = input("Your answer: ")
        if (operator == "+"):
            result = num_one + num_two
        else:
            result = num_one * num_two
        if (answer.isdigit() is True and int(answer) == result):
            print("Correct!")
        else:
            print(f"{answer}  is wrong answer ;(. Correct answer was {result}")
            return f"Let's try again, {name}!"
    return f"Congratulations, {name}!"

