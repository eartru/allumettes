from game import IA
from game.Game import IAFight
from colorama import Fore
from colorama import Style

IA = {
    1: IA.RandomIA,
    2: IA.MathIA,
    3: IA.MinMaxIA
}


def main():
    nb_matches = 0
    first_ia = None
    second_ia = None

    print(
        "\n{}{}--------------------------\n"
        "| Welcome in the IA Arena |\n"
        "--------------------------\n{}"
        .format(Fore.CYAN, Style.BRIGHT, Style.RESET_ALL))
    while nb_matches <= 0:
        try:
            nb_matches = int(input("How many matches do you want ?\n"))
        except Exception:
            pass

    while not first_ia:
        try:
            selection = int(input(
                "Pick your first IA\n"
                "    1: Random IA\n"
                "    2: Math IA\n"
                "    3: Min Max IA\n"
            ))
            first_ia = IA.get(selection)
        except Exception:
            pass

    while not second_ia:
        try:
            selection = int(input(
                "Pick your second IA\n"
                "    1: Random IA\n"
                "    2: Math IA\n"
                "    3: Min Max IA\n"
            ))
            second_ia = IA.get(selection)
        except Exception:
            pass

    print('\n{}------ Starting now ------{}\n'.format(
        Fore.CYAN, Style.RESET_ALL
    ))

    ia_fight = IAFight(first_ia(), second_ia(), nb_matches)
    ia_fight.fight()


if __name__ == "__main__":
    main()
