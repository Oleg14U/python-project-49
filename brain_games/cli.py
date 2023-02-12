import prompt


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
