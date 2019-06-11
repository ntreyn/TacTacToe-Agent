from gym import spaces
import numpy as np
import random

class ttt_env:

    """
    1   2   3
    4   5   6
    7   8   9

    1: [1,2,3], [1,4,7], [1,5,9]
    2: [1,2,3], [2,5,8]
    3: [1,2,3], [3,6,9], [3,5,7]
    4: [1,4,7], [4,5,6]
    5: [2,5,8], [4,5,6], [1,5,9], [3,5,7]
    6: [3,6,9], [4,5,6]
    7: [1,4,7], [7,8,9], [3,5,7]
    8: [2,5,8], [7,8,9]
    9: [3,6,9], [7,8,9], [1,5,9]
    """

    def __init__(self):
        self.num_tiles = 9
        self.action_size = 9
        self.state_size = 19683 * 2 # 3^9 * 2
        """
            3^9 does not accuracy describe the number of actually possible states
            however, for now, the computation for determining states is simpler
        """
        self.streaks = [ [1,2,3], [1,4,7], [1,5,9], [2,5,8], [3,6,9], [3,5,7], [4,5,6], [7,8,9] ]
        self.generate_states()
        self.reset()

    def reset(self):
        self.board = [' '] * self.num_tiles
        self.done = False
        return self.get_state('X')

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

        reward = self.get_reward(action, player)

        self.board[action - 1] = player
        new_state = self.get_state(player)
        status = self.check_status()

        if status == 'D' or status == 'X' or status == 'O':
            self.done = True

        return new_state, reward, status, self.done

    def get_reward(self, action, player):

        # Block streak(s) of 1
        # +1 per streak

        # Block streak(s) of 2
        # +11 per streak

        # Create streak(s) of 1
        # +2 per streak

        # Create streak(s) of 2
        # +5 per streak

        # Create streak of 3
        # +100
        reward = 0

        for streak in self.streaks:
            if action in streak:
                sums = self.streak_contains(streak)
                if sums[' '] == 3:
                    # Create streak(s) of 1
                    # +2 per streak
                    reward += 2

                elif sums[' '] == 2:
                    if sums[player] == 1:
                        # If friendly streak
                        # Create streak(s) of 2
                        # +5 per streak
                        reward += 5
                    else:
                        # Else
                        # Block streak(s) of 1
                        # +1 per streak
                        reward += 1

                elif sums[' '] == 1:
                    if sums[player] == 2:
                        # If friendly streak
                        # Create streak of 3
                        # +100
                        reward += 100
                    elif sums[player] == 1:
                        # Else if mixed streak
                        # +0
                        continue
                    else:
                        # Else if opponent streak
                        # Block streak(s) of 2
                        # +11 per streak
                        reward += 11
                else:
                    print("Error: action for full streak")
                    exit()

        return reward

    def streak_contains(self, streak):

        sums = {}
        sums['X'] = 0
        sums['O'] = 0
        sums[' '] = 0

        for space in streak:
            tile = self.board[space - 1]
            if tile == 'X':
                sums['X'] += 1
            elif tile == 'O':
                sums['O'] += 1
            else:
                sums[' '] += 1

        return sums

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
            board_state = tuple(list)
            state_X = board_state, 'X'
            state_O = board_state, 'O'
            self.state_space[state_X] = self.state_count
            self.state_count += 1
            self.state_space[state_O] = self.state_count
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

    def get_state(self, player):
        return self.state_space[tuple(self.board), player]


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
