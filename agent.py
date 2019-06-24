import numpy as np
import random

class computer_agent():
    def __init__(self, n, m, e, l):
        self.name = n
        self.mark = m
        self.env = e
        self.learner = l

    def turn(self, state):
        # move = self.env.sample_action()

        open_tiles = self.env.empty_spaces()
        open_actions = [-1] * 9

        for tile in open_tiles:
            open_actions[tile] = self.learner.qtable[state,tile]

        action = np.argmax(open_actions)

        print(self.name + " chose " + str(action))
        return action

    def wins(self):
        print(self.name + " wins!")


class human_player:
    def __init__(self, n, m):
        self.name = n
        self.mark = m

    def turn(self, state):
        strmove = input(self.name + ", choose your move: ")
        print(self.name + " chose " + strmove)
        return int(strmove) - 1

    def wins(self):
        print(self.name + " wins!")
