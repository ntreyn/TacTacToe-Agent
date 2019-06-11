import numpy as np
import random

class learner:
    def __init__(self, e):
        self.env = e

    def learn(self):
        state_size = self.env.state_size
        action_size = self.env.action_size

        self.qtable = np.zeros((state_size, action_size))

        total_episodes = 100000
        max_steps = 10
        learning_rate = 0.7
        gamma = 0.9

        epsilon = 1.0
        max_epsilon = 1.0
        min_epsilon = 0.3
        decay_rate = 0.0001

        for episode in range(total_episodes):

            print(episode, end='\r')

            state = self.env.reset()
            step = 0
            done = False
            turn = 'X'
            reward = 0

            for step in range(max_steps):

                exp_exp_tradeoff = random.uniform(0,1)

                if exp_exp_tradeoff > epsilon:

                    open_tiles = self.env.empty_spaces()
                    open_actions = [-1] * 9

                    for tile in open_tiles:
                        open_actions[tile - 1] = self.qtable[state,tile - 1]

                    action = np.argmax(open_actions) + 1

                else:
                    action = self.env.sample_action()

                new_state, reward, status, done = self.env.step(action, turn)

                open_tiles = self.env.empty_spaces()
                open_actions = [0] * 9

                for tile in open_tiles:
                    open_actions[tile - 1] = self.qtable[state,tile - 1]

                self.qtable[state, action - 1] = self.qtable[state, action - 1] + learning_rate * (reward + gamma * np.max(open_actions) - self.qtable[state, action - 1])

                state = new_state

                if done:
                    break

                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'

            epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode)

        self.env.reset()
