from gym import spaces
import numpy as np
import random

class ttt_env:
    def __init__(self):
        self.num_tiles = 9
        self.reset()

    def reset(self):
        self.board = [' '] * self.num_tiles

        self.done = False


    def step(self, action, player):
        if self.done:
            print("Game already over")
            quit()
        if self.board[action - 1] != ' ':
            print("Invalid action:", action)
            quit()
        if player != 'X' and player != 'O':
            print("Invalid player:", player)
            quit()

        print(action)
        self.board[action - 1] = player
        status = self.check_status()

        if status == 'D':
            self.done = True
            X_reward = 0
            O_reward = 0
        elif status == 'X':
            self.done = True
            X_reward = 1
            O_reward = -1
        elif status == 'O':
            self.done = True
            X_reward = -1
            O_reward = 1
        else:
            X_reward = 0
            O_reward = 0

        return X_reward, O_reward, self.done

    def render(self):
        print('-------------')
        for row in range(3):
            rowString = '| ' + self.board[row] + ' | ' + self.board[row + 1] + ' | ' + self.board[row + 2] + ' |'
            print(rowString)
            print('-------------')

    def empty_spaces(self):
        return [(i + 1) for i, s in enumerate(self.board) if s == ' ']

    def sample_action(self):
        return random.choice(self.empty_spaces())

    def check_status(self):
        # Check for winner
        for p in ['X', 'O']:
            # Check columns
            for r in range(0, 3):
                if self.board[r] == p and self.board[r + 3] == p and self.board[r + 6] == p:
                    return p
            # Check rows
            for r in range(0, 9, 3):
                if [p] * 3 == [self.board[i] for i in range(r, r + 3)]:
                    return p
            # Check diagonals
            if self.board[0] == p and self.board[4] == p and self.board[8] == p:
                return p
            if self.board[2] == p and self.board[4] == p and self.board[6] == p:
                return p

        # Check for draw
        for i in range(self.num_tiles):
            if self.board[i] == ' ':
                # Still playing
                return 'P'

        # Draw
        return 'D'
