from colorama import Fore
from colorama import Style


class Game(object):

    nb_matches = 16
    state = None

    def __init__(self, IA):
        self.IA = IA

    def player_removes(self, nb_matches):
        self.nb_matches -= nb_matches
        self.state = GameState(nb_matches, self.nb_matches, 'IA')

    def ia_removes(self):
        nb_matches = self.IA.take_decision(self.state.matches_left)
        self.nb_matches -= nb_matches
        self.state = GameState(nb_matches, self.nb_matches, 'Le joueur')


class GameState(object):

    def __init__(self, matches_removed, matches_left, winner):
        self.winner = winner
        self.matches_removed = matches_removed
        self.matches_left = matches_left
        self.game_ended = matches_left <= 0


class IAFight(object):

    def __init__(self, first_IA, second_IA, nb_matches):
        self.IA = [first_IA, second_IA]
        self.first_IA = first_IA
        self.second_IA = second_IA
        self.nb_matches = nb_matches

    def fight(self):
        i = 0
        while self.nb_matches > 0:
            ia = self.IA[i % 2]
            nb_matches = ia.take_decision(self.nb_matches)
            print('{}IA {}: {} removed {}{}\n'.format(
                Fore.YELLOW, (i % 2 + 1), ia, nb_matches, Style.RESET_ALL
            ))
            self.nb_matches -= nb_matches
            i += 1
        print("\n\n{}{}Winner is IA {}: {}{}\n".format(
            Fore.GREEN, Style.BRIGHT,
            (i % 2 + 1), self.IA[i % 2], Style.RESET_ALL
        ))
