import numpy as np
import random

from collections import defaultdict

class mclearner:
    def __init__(self, e, args):
        self.env = e

    def train(self):
        
        state_size = self.env.state_size
        action_size = self.env.action_size

        self.qtable = np.zeros((state_size, action_size))

        returns_sum = defaultdict(float)
        returns_count = defaultdict(float)

        total_episodes = 500000
        max_steps = 10
        gamma = 0.9

        epsilon = 1.0
        max_epsilon = 1.0
        min_epsilon = 0.1
        decay_rate = 0.00001

        for episode in range(total_episodes):

            print(episode, epsilon, end='\r')
            # print(epsilon, end='\r')
            state = self.env.reset()
            episode_results = []
            step = 0
            status = 'P'

            for step in range(max_steps):

                exp_exp_tradeoff = random.uniform(0,1)

                if exp_exp_tradeoff > epsilon:
                    action = self.act(state)
                else:
                    action = self.env.sample_action()

                new_state, reward, status, done = self.env.step(action)

                episode_results.append((state, action, reward))
                state = new_state

                if done:
                    break

            sa_in_episode = set([(s, a) for s, a, _ in episode_results])
            
            for state, action in sa_in_episode:
                sa_pair = (state, action)

                reverse_state = self.env.reverse_state_space[state]
                if reverse_state[1] != status:
                    continue

                first_idx = next(i for i, x in enumerate(episode_results) if x[0] == state and x[1] == action)
                G = sum([x[2] * (gamma ** i) for i, x in enumerate(episode_results[first_idx:])])

                returns_sum[sa_pair] += G
                returns_count[sa_pair] += 1.0
                self.qtable[state][action] = returns_sum[sa_pair] / returns_count[sa_pair]

            epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode)

        self.env.reset()
        print()
    
    def act(self, state):
        open_tiles = self.env.empty_spaces()
        open_actions = [-1] * 9

        for tile in open_tiles:
            open_actions[tile] = self.qtable[state,tile]

        action = np.argmax(open_actions)
        return action
        