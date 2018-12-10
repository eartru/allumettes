from random import randint


class IA(object):

    def __init__(self, is_smart=True):

        self.is_smart = is_smart
        self.build_tree

    def take_decision(self, nb_match):
        if self.is_smart:
            return self._take_smart_decision(nb_match)
        return self._take_dumb_decision()

    def _take_dumb_decision(self):
        return randint(1, 3)

    def _take_smart_decision(self, nb_match):
        node = Node(nb_match)
        best_node = None
        for node_ in node.children:
            if not best_node:
                best_node = node_
            if node_.weight > best_node.weight:
                best_node = node_

        return best_node.value

    def build_tree(self, nb_match):
        self.tree = Tree(nb_match)


class Tree(object):
    def __init__(self, nb_match):
        self.nb_match = nb_match


class Node(object):

    children = None
    match_left = 0
    weight = 0

    def __init__(self, value, depth=0):
        self.children = []
        self.value = value
        self.depth = depth
        if value == 0:
            self.weight = 1 if self.depth % 2 == 0 else -1
        else:
            self.make_children()

    def make_children(self):
        for i in range(1, 4):
            if self.value - i >= 0:
                node = Node(self.value - i, self.depth + 1)
                self.children.append(node)
                self.weight += node.weight
