class Game(object):

    nb_matches = 16
    state = None

    def __init__(self, IA):
        self.IA = IA

    def player_removes(self, nb_matches):
        self.nb_matches -= nb_matches
        self.state = GameState(nb_matches, self.nb_matches, 'Le joueur')

    def ia_removes(self):
        nb_matches = self.IA.take_decision()
        self.nb_matches -= nb_matches
        self.state = GameState(nb_matches, self.nb_matches, 'IA')


class GameState(object):

    def __init__(self, matches_removed, matches_left, player):
        self.player = player
        self.matches_removed = matches_removed
        self.matches_left = matches_left
        self.game_ended = matches_left <= 0
