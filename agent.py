import numpy as np
import random

class computer_agent():
    def __init__(self, n, m, e):
        self.name = n
        self.mark = m
        self.env = e

    def turn(self, env):
        move = env.sample_action()
        print(self.name + " chose " + str(move))
        return move

    def wins(self):
        print(self.name + " wins!")
