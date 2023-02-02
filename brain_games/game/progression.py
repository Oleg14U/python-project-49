from brain_games.game.even import yours_name
import random


def create_geometric_progression():
    begin = random.randint(1, 150)
    q = random.randint(1, 5)
    return [str(begin + i * q) for i in range(10)]


def game(name):
    print("What number is missing in the progression?")
    for i in range(3):
        progression = create_geometric_progression()
        question = random.randint(0, 9)
        result = progression[question]
        progression.remove(result)
        progression.insert(question, '..')
        print("Question: " + ' '.join(progression))
        answer = input("Your answer: ")
        if (answer.isdigit() is True and int(answer) == int(result)):
            print("Correct!")
        else:
            print(f"{answer}  is wrong answer ;(. Correct answer was {result}")
            return f"Let's try again, {name}!"
    return f"Congratulations, {name}!"

