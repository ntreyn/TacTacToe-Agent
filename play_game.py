#!/usr/bin/env python

import numpy as np
import random
from environment import ttt_env
from player import human_player
from agent import computer_agent

class play_game:
    def __init__(self):
        self.turn = 'X'
        self.env = ttt_env()
        print(len(self.env.state_space))

    def play(self):

        X_reward = 0
        O_reward = 0
        move_count = 0

        while True:
            move_count += 1
            print("Move", move_count)
            self.env.render()

            if self.turn == 'X':
                action = self.X.turn(self.env)
                next_turn = 'O'
            elif self.turn == 'O':
                action = self.O.turn(self.env)
                next_turn = 'X'

            new_state, X_reward, O_reward, done = self.env.step(action, self.turn)

            print(new_state)

            if done:
                break

            # End of turn
            self.turn = next_turn

        self.env.render()

        print("Gameover")
        if X_reward == 1:
            self.X.wins()
        elif O_reward == 1:
            self.O.wins()
        else:
            print("Draw")

        self.env.reset()

    def choose_mode(self):
        while True:
            print("Pick a mode: \n(1) Human vs. Human\n(2) Human vs. Computer\n(3) Computer vs. Computer")
            mode = input()

            if mode == '1':
                print("Player 1")
                name = input("What is your name? ")
                while True:
                    mark = input("Choose your mark (X / O): ")
                    if mark == 'X':
                        self.X = human_player(name, mark)
                        print("Player 2")
                        name = input("What is your name? ")
                        mark = 'O'
                        print("Your mark is 'O'")
                        self.O = human_player(name, mark)
                        break
                    elif mark == 'O':
                        self.O = human_player(name, mark)
                        print("Player 2")
                        name = input("What is your name? ")
                        mark = 'X'
                        print("Your mark is 'X'")
                        self.X = human_player(name, mark)
                        break
                    else:
                        print("Invalid mark, please try again")

            elif mode == '2':
                print("Human player")
                name = input("What is your name? ")
                while True:
                    mark = input("Choose your mark (X / O): ")
                    if mark == 'X':
                        self.X = human_player(name, mark)
                        self.O = computer_agent('Alexander', 'O')
                        break
                    elif mark == 'O':
                        self.O = human_player(name, mark)
                        self.X = computer_agent('Caesar', 'X')
                        break
                    else:
                        print("Invalid mark, please try again")
            elif mode == '3':
                self.X = computer_agent('Caesar', 'X')
                self.O = computer_agent('Alexander', 'O')
                break
            else:
                print("Invalid mode, please try again")

            break

def main():
    game = play_game()
    game.choose_mode()
    game.play()

if __name__ == "__main__":
    main()
