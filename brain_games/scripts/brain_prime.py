from brain_games.scripts.brain_calc import random_nember
from brain_games.scripts.brain_even import welcome
from brain_games.scripts.brain_even import yours_name


def prime_number(num):
    k = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k = k + 1
    if (k <= 0):
        return "yes"
    else:
        return "no"


def game(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    for i in range(0, 3):
        num = random_nember()
        print(f"Question: {num}")
        result = prime_number(num)
        answer = input("Your answer: ")
        if (answer == result):
            print("Correct!")
        else:
            print(f"{answer}  is wrong answer ;(. Correct answer was {result}")
            return f"Let's try again, {name}!"
    return f"Congratulations, {name}!"


def main():
    welcome()
    print(game(yours_name()))


if __name__ == '__main__':
    main()
