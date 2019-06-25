
import argparse
import numpy as np

from parameters import core_argparser, MODEL_MAP
from environment import ttt_env

class rl_main():
    def __init__(self, e, a1, a2):
        self.env = e
        self.agent1 = a1
        self.agent2 = a2
        self.mc_count = 0
        self.q_count = 0
        self.draw_count = 0

    def choose_move(self, agent, state):
        open_tiles = self.env.empty_spaces()
        open_actions = [-1] * 9

        for tile in open_tiles:
            open_actions[tile] = agent.qtable[state,tile]

        action = np.argmax(open_actions)
        return action

    def test_vs_q(self, num_games):

        for n in range(num_games):

            rand = np.random.randint(0, 2)
            if rand == 0:
                self.X = self.agent1
                self.O = self.agent2
                status = self.play()
                if status == 'X':
                    self.mc_count += 1
                elif status == 'O':
                    self.q_count += 1
                else:
                    self.draw_count += 1
            else:
                self.X = self.agent2
                self.O = self.agent1
                status = self.play()
                if status == 'X':
                    self.q_count += 1
                elif status == 'O':
                    self.mc_count += 1
                else:
                    self.draw_count += 1
        
        print("Played {} games".format(num_games))
        print("MC won {}, Q won {}, they drew {}".format(self.mc_count, self.q_count, self.draw_count))

    def play(self):
    
        turn = 'X'
        done = False
        state = self.env.reset()

        while True:

            if turn == 'X':
                action = self.choose_move(self.X, state)
                next_turn = 'O'
            elif turn == 'O':
                action = self.choose_move(self.O, state)
                next_turn = 'X'

            new_state, reward, status, done = self.env.step(action)

            if done:
                break

            # End of turn
            state = new_state
            turn = next_turn

        self.env.reset()

        return status

def main(args):

    print("Model: {}".format(args.model))

    env = ttt_env()
    agent = MODEL_MAP[args.model](env)
    agent.learn()
    
    q_agent = MODEL_MAP['qlearn'](env)
    q_agent.learn()

    tester = rl_main(env, agent, q_agent)
    tester.test_vs_q(args.num_games)

if __name__ == '__main__':
    ARGPARSER = argparse.ArgumentParser(parents=[core_argparser()])
    ARGPARSER.add_argument(
        '--num_games',
        type=int,
        default=10000,
        help='number of games for agents to play (default: 10,000'
    )
    PARAMS = ARGPARSER.parse_args()
    main(PARAMS)