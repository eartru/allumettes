from random import randint


class IA(object):

    def __init__(self, is_smart=True):

        self.is_smart = is_smart

    def take_decision(self, nb_match):
        if self.is_smart:
            return self._take_smart_decision(nb_match)
        return self._take_dumb_decision()

    def _take_dumb_decision(self):
        return randint(1, 3)

    def _take_smart_decision(self, nb_match):
        root = Node(nb_match)
        root.make_children()
        return root.max()


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
        for i in range(1, 4):
            if self.match_left - i >= 0:
                node = Node(self.match_left - i, self.depth + 1, i)
                node.make_children()
                self.children.append(node)
                self.weight += node.weight

    def max(self):
        max_node = None
        for node in self.children:
            if not max_node:
                max_node = node
            if node.weight > max_node.weight:
                max_node = node

        return max_node.value

