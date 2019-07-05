
import argparse

from qlearner import qlearner
from mclearner import mclearner
from dqn import DQN

MODEL_MAP = {
    'qlearn': qlearner,
    'mclearn': mclearner,
    'dqn': DQN
}

def core_argparser():
    argparser = argparse.ArgumentParser(add_help=False)
    argparser.add_argument(
        '-m', '--model',
        default='qlearn',
        type=str,
        help='load model name'
    )
    argparser.add_argument(
        '-n', '--num_episodes',
        default=100000,
        type=int,
        help='num training episodes (default: 100,000'
    )
    argparser.add_argument(
        '-g', '--gamma', 
        type=float, 
        default=0.9, 
        help='discount (default: 0.9)'
    )
    argparser.add_argument(
        '-a', '--alpha', 
        type=float, 
        default=0.1, 
        help='step size (default: 0.1)'
    )
    argparser.add_argument(
        '-e', '--epsilon', 
        type=float, 
        default=0.05, 
        help='exploration chance (default: 0.05)'
    )
    argparser.add_argument(
        '-l', '--learning_rate', 
        type=float, 
        default=0.0001, 
        help='learning rate (default: 0.0001'
    )
    argparser.add_argument(
        '-r', '--render', 
        action='store_true',
        help='render game'
    )
    argparser.add_argument(
        '--im_reward', 
        action='store_true',
        help='intermediate rewards'
    )
    argparser.add_argument(
        '--device',
        default='cpu',
        type=str,
        help='cpu or cuda (default: cpu)'
    )

    return argparser