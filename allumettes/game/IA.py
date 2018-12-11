from random import randint
from game.utils import timing


class DumbIA(object):

    @timing
    def take_decision(self, nb_match):
        max_ = 3 if nb_match >= 3 else nb_match
        return randint(1, max_)

    def __str__(self):
        return 'DumbIA'


class MinMaxIA(object):

    @timing
    def take_decision(self, nb_match):
        root = Node(nb_match)
        root.make_children()
        return root.get_max_node().value

    def __str__(self):
        return 'MinMaxIA'


class Node(object):

    children = None
    weight = 0

    def __init__(self, match_left, depth=0, value=0):
        self.children = []
        self.value = value
        self.depth = depth
        self.match_left = match_left
        if match_left == 0:
            self.weight = 1 if self.depth % 2 == 0 else -1

    def make_children(self):
        i = 1
        while i < 4 and (self.match_left - i >= 0):
            node = Node(self.match_left - i, self.depth + 1, i)
            node.make_children()
            self.children.append(node)
            self.weight += node.weight
            i += 1

    def get_max_node(self):
        max_node = None
        for node in self.children:
            if not max_node:
                max_node = node
            if node.weight > max_node.weight:
                max_node = node

        return max_node
