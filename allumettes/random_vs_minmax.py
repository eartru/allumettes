from game import IA
from game.Game import IAFight


def main():
    nb_matches = 0
    while nb_matches <= 0:
        try:
            nb_matches = int(input("How many matches do you want ?\n"))
        except Exception:
            pass

        ia_fight = IAFight(IA.DumbIA(), IA.MinMaxIA(), nb_matches)
        ia_fight.fight()


if __name__ == "__main__":
    main()
