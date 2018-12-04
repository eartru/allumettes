from random import randint

class IA(object):

    def __init__(self, is_smart=False):

        self.is_smart = is_smart

    def take_decision(self):
        if self.is_smart:
            return self._take_smart_decision()
        return self._take_dumb_decision()

    def _take_dumb_decision(self):
        return randint(1, 3)

    def _take_smart_decision(self):
        raise Exception("TODO")
