from interface.window import Window
from game.Game import Game
from game.IA import IA


def main():
    game = Game(IA())
    window = Window(game=game)
    window.start(width=300, height=200)


if __name__ == "__main__":
    main()
