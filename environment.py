from gym import spaces
import numpy as np
import random

class ttt_env:
    def __init__(self):
        self.num_tiles = 9
        self.action_size = 9
        self.state_size = 19683 # 3^9
        """
            3^9 does not accuracy describe the number of actually possible states
            however, for now, the computation for determining states is simpler
        """
        self.reset()
        self.generate_states()

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

        self.board[action - 1] = player
        new_state = self.get_state()
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

        return new_state, X_reward, O_reward, self.done

    def render(self):
        print('-------------')
        for row in range(0, 9, 3):
            rowString = '| ' + self.board[row] + ' | ' + self.board[row + 1] + ' | ' + self.board[row + 2] + ' |'
            print(rowString)
            print('-------------')

    def empty_spaces(self):
        return [(i + 1) for i, s in enumerate(self.board) if s == ' ']

    def sample_action(self):
        return random.choice(self.empty_spaces())

    def generate_states(self):
        state = [' '] * 9
        self.state_space = {}
        self.state_count = 0
        self.recursive_states(state, 0)

    def recursive_states(self, list, ind):
        if ind == 9:
            state = tuple(list)
            self.state_space[state] = self.state_count
            self.state_count += 1
            return
        else:
            l0 = list
            l0[ind] = ' '
            self.recursive_states(list, ind + 1)
            l1 = list
            l1[ind] = 'X'
            self.recursive_states(l1, ind + 1)
            l2 = list
            l2[ind] = 'O'
            self.recursive_states(l2, ind + 1)
            return

    def get_state(self):
        """
            ' ' --> 0
            'X' --> 1
            'O' --> 2
        """
        """
        values = list()

        for tile in self.board:
            if tile == ' ':
                values.append(0)
            elif tile == 'X':
                values.append(1)
            elif tile == 'O':
                values.append(2)
        """
        return self.state_space[tuple(self.board)]


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
