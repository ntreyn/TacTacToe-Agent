
import argparse

from qlearner import qlearner
from mclearner import mclearner

MODEL_MAP = {
    'qlearn': qlearner,
    'mclearn': mclearner
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
        type=float, default=0.0001, 
        help='learning rate (default: 0.0001'
    )

    return argparser