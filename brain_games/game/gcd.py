from brain_games.game.calc import random_nember

def greatest_common_divisor(a, b):
    while a != 0 and b != 0:
        if (a > b):
            a = a % b
        else:
            b = b % a
    return (a + b)


def game(name):
    print("Find the greatest common divisor of given numbers.")
    for i in range(0, 3):
        num1 = random_nember()
        num2 = random_nember()
        print(f"Question: {num1} {num2}")
        answer = input("Your answer: ")
        result = greatest_common_divisor(num1, num2)
        if (answer.isdigit() is True and int(answer) == result):
            print("Correct!")
        else:
            print(f"{answer}  is wrong answer ;(. Correct answer was {result}")
            return f"Let's try again, {name}!"
    return f"Congratulations, {name}!"


