#!/usr/bin/env python

import numpy as np
import random
from environment import ttt_env
from player import human_player
from agent import computer_agent
from learner import learner

class play_game:
    def __init__(self):
        self.turn = 'X'
        self.env = ttt_env()
        self.learner = learner(self.env)
        self.learner.learn()
        self.X_count = 0
        self.O_count = 0
        self.draw_count = 0

    def play(self):

        self.turn = 'X'
        reward = 0
        move_count = 0
        done = False
        state = self.env.reset()

        while True:
            move_count += 1
            print("Move", move_count)
            self.env.render()

            if self.turn == 'X':
                action = self.X.turn(state)
                next_turn = 'O'
            elif self.turn == 'O':
                action = self.O.turn(state)
                next_turn = 'X'

            new_state, reward, status, done = self.env.step(action, self.turn)

            if done:
                break

            # End of turn
            state = new_state
            self.turn = next_turn

        self.env.render()

        print("Gameover")
        if status == 'X':
            self.X_count += 1
            self.X.wins()
        elif status == 'O':
            self.O_count += 1
            self.O.wins()
        else:
            self.draw_count += 1
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
                        self.O = computer_agent('Alexander', 'O', self.env, self.learner)
                        break
                    elif mark == 'O':
                        self.O = human_player(name, mark)
                        self.X = computer_agent('Caesar', 'X', self.env, self.learner)
                        break
                    else:
                        print("Invalid mark, please try again")
            elif mode == '3':
                self.X = computer_agent('Caesar', 'X', self.env, self.learner)
                self.O = computer_agent('Alexander', 'O', self.env, self.learner)
                break
            else:
                print("Invalid mode, please try again")
            break

def main():
    game = play_game()
    """
    game.choose_mode()
    for n in range(10000):
        game.play()
    """
    while True:
        game.choose_mode()
        game.play()
        temp = input("Would you like to play again? (y/n) ")
        if temp == 'n':
            break

    # print("X wins:", game.X_count)
    # print("O wins:", game.O_count)
    # print("Draws:", game.draw_count)

if __name__ == "__main__":
    main()
