# -*- coding: utf-8 -*-

from random import randint
from game.utils import timing
from colorama import Fore
from colorama import Style


class RandomIA(object):

    '''
        Simple IA  which returns only random number between 1 and 3
        Cannot return a number higher than the number of matches left
        left on the board.
    '''

    @timing
    def take_decision(self, nb_match):
        max_ = 3 if nb_match >= 3 else nb_match
        return randint(1, max_)

    def __str__(self):
        return 'Random IA'


class MathIA(object):
    '''
        Simple IA which returns the perfect number according the number
        of matches left on the board. The Solution to win this game is to left
        a total of matches equals to a multiple of 4 + 1 on the board so your
        opponent can never win. The flaw is when your opponent knows this trick
        and is the first to play you can't do anything so this IA returns 1 in
        this condition.
    '''

    @timing
    def take_decision(self, nb_match):
        for i in range(1, 4):
            nb_match_left = nb_match - i
            if nb_match_left % 4 == 1:
                return i
        return 1

    def __str__(self):
        return 'Math IA'


class MinMaxIA(object):

    '''
        This IA will retun the value of the node which has this higher weight.
        The weight of the node the probability to win.
    '''

    @timing
    def take_decision(self, nb_match):
        root = Node(nb_match)
        root.make_children()
        print('{}{}{} Nodes were visited {}'.format(
            Fore.RED, Style.BRIGHT, root.visited_node_count, Style.RESET_ALL
        ))
        return root.get_max_node().value

    def __str__(self):
        return 'Min Max IA'


class GraphMinMaxIA(object):

    '''
        This IA will retun the value of the referenced node which has this
        higher weight. The weight of the node the probability to win.
    '''

    @timing
    def take_decision(self, nb_match):
        root = ReferencedNode(nb_match)
        root.make_children()
        return nb_match - root.get_max_node().match_left


class Node(object):

    '''
        This object is the representation of a Min Max tree, for a given
        number of matches.
        params:
            - visited_node: number of node created/visited to find a solution
            - children: list of direct descendant of the current node
            - weight: probability to win at the current node, aggegation of the
                      weight of all the node's children
            - depth: generation of node
                     also number of parent of the current node
            - match_left: represention of number of matches left on
                          the board at the current node
    '''

    visited_node_count = 1
    weight = 0

    def __init__(self, match_left, depth=0, value=0):
        self.children = []
        self.value = value
        self.depth = depth
        self.match_left = match_left
        if match_left == 0:
            self.weight = 1 if self.depth % 2 == 0 else -1

    def make_children(self):

        '''
            Recursive function that creates all the nodes, links them to
            their parents and aggregate their weight
        '''
        i = 1
        while i < 4 and (self.match_left - i >= 0):
            node = Node(self.match_left - i, self.depth + 1, i)
            node.make_children()
            self.children.append(node)
            self.weight += node.weight
            self.visited_node_count += node.visited_node_count
            i += 1

    def get_max_node(self):
        max_node = None
        for node in self.children:
            if not max_node:
                max_node = node
            if node.weight > max_node.weight:
                max_node = node

        return max_node


references = dict()


class ReferencedNode(object):

    """
        Graph representation of the Min Max Tree, aggregate all path's length to
        go from x to y and give them a weight of 1 if they're odd or -1 if not.

        params
            - children: list of direct descendant of the current node
            - match_left: represention of number of matches left on
                          the board at the current node
            - routes: list of path's length to go from match_left to 0
    """

    def __init__(self, match_left):
        self.children = []
        self.match_left = match_left
        self.routes = []
        if match_left == 0:
            self.routes.append(1)

    def make_children(self):
        i = 1
        while i < 4 and (self.match_left - i >= 0):
            node = references.get(self.match_left - i, None)
            if not node:
                node = ReferencedNode(self.match_left - i)
                references[self.match_left - i] = node
                node.make_children()
                node.make_route()

            self.children.append(node)
            i += 1

    def make_route(self):
        for child in self.children:
            for route in child.routes:
                self.routes.append(1 + route)

    def get_weight(self):
        self.weight = 0
        for route in self.routes:
            if route % 2 == 0:
                self.weight += 1
            else:
                self.weight -= 1
        return self.weight

    def get_max_node(self):
        max_node = None
        for node in self.children:
            if not max_node:
                max_node = node
            if node.get_weight() > max_node.get_weight():
                max_node = node

        return max_node
