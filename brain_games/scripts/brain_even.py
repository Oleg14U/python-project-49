from brain_games.game.even import welcome
from brain_games.game.even import yours_name
from brain_games.game.even import game


def main():
    welcome()
    print(game(yours_name()))


if __name__ == '__main__':
    main()
