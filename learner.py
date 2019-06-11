

class learner:
    def __init__(self, a1, a2, e):
        self.agent1 = a1
        self.agent2 = a2
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
        min_epsilon = 0.01
        decay_rate = 0.001

        for episode in range(total_episodes):

            state = self.env.reset()
            step = 0
            done = False
            turn = 'X'

            for step in range(max_steps):

                """
                    Add turns, update same qtable for both agents
                """

                exp_exp_tradeoff = random.uniform(0,1)

                if exp_exp_tradeoff > epsilon:
                    open_tiles = self.env.empty_spaces()
                    open_actions = []

                    for tile in open_tiles:
                        open_actions.append(self.qtable[state,tile - 1])

                    action = np.argmax(open_actions)

                else:
                    action = self.env.sample_action()

                new_state







            epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode)
