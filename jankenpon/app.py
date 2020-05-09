#!/usr/bin/env python3
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
import time
import sys
from jankenpon.resources import (HANDS, HOW_TO_PLAY, MENU_IMAGE, MENU_OPTIONS, 
                       MENU_OPTIONS_PROMPT, SORRY_YES_NO, INTRO,
                       OPPONENT_NAMES, HOW_TO_PLAY)
from jankenpon.player_classes import (Player, HumanPlayer,
                            RockPlayer, CyclePlayer,
                            BadLuckPlayer, InteligentReflectPlayer,
                            ReflectPlayer, RandomPlayer, MOVES)
from jankenpon.tools import hinder_invalid_input, beats


class Game:
    def __init__(self, p1, p2):
        print(INTRO)
        self.point_P1 = 0
        self.point_P2 = 0
        self.my_name = ''
        self.computer_name = ''
        self.opon = 0
        self.oponents = [BadLuckPlayer(), InteligentReflectPlayer(),
                         ReflectPlayer(), CyclePlayer(),
                         RandomPlayer(), RockPlayer()]
        self.revealStrategyMode = False
        self.chooseGame()

    def chooseGame(self):
        self.game_option = hinder_invalid_input(MENU_OPTIONS_PROMPT , MENU_OPTIONS)

        if self.game_option == '1':
            self.p1 = HumanPlayer()
            self.p2 = random.choice(self.oponents)
            self.get_player_name()
            self.get_computer_name()
            self.game_hum_vs_comp()

        elif self.game_option == '2':
            self.p1 = random.choice(self.oponents)
            self.p2 = random.choice(self.oponents)
            self.game_comp_vs_comp()

        elif self.game_option == '3':
            print(HOW_TO_PLAY)
            self.chooseGame()

        elif self.game_option in ['q', 'quit', 'exit', 'e']:
            print('Bye bye!')
            sys.exit()

        else:
            self.chooseGame()

    def get_player_name(self):
        print('What is your name?')
        self.my_name = input()
        if self.my_name == '':
            self.my_name = 'Player 1'

    def get_computer_name(self):
        if self.opon == len(OPPONENT_NAMES) - 1:
            self.opon = 0
        else:
            self.opon += 1
        self.computer_name = OPPONENT_NAMES[self.opon]

    def play_game_hum(self):
        print("\n     Game start!\n")
        for round in range(3):
            print('\x1b[6;37;41m' + f" X---- ROUND {round+1} ----X "
                  + '\x1b[0m')
            print('\x1b[33m'+'r'+'\x1b[0m'+'ock, ' + '\x1b[33m' +
                  'p'+'\x1b[0m' + 'aper or '+'\x1b[33m' +
                  's'+'\x1b[0m' + 'cissors?')
            self.play_round()

    def game_hum_vs_comp(self):
        self.play_game_hum()
        self.get_who_won()
        print("\n    Game over!\n")
        print('Do you want to play again? (yes or no)')
        play_again = hinder_invalid_input(SORRY_YES_NO, 'yes no')
        if play_again == 'yes':
            print('Do you want to know your opponent\'s strategy? (yes or no)')
            reveal_mode = hinder_invalid_input(SORRY_YES_NO, 'yes no')
            if reveal_mode == 'yes':
                self.revealStrategyMode = True
            else:
                self.revealStrategyMode = False
            self.get_computer_name()
            self.p2 = random.choice(self.oponents)
            self.game_hum_vs_comp()
        else:
            self.__init__(Player(), Player())

    def play_game_com(self):
        print("\n   Game start!")
        self.my_name = random.choice(OPPONENT_NAMES)
        self.computer_name = random.choice(OPPONENT_NAMES)
        if self.my_name == self.computer_name:
            self.computer_name = self.my_name + ' Bad Twin'
        for round in range(3):
            print('\n\x1b[6;37;41m' + f" X---- ROUND {round+1} ----X "
                  + '\x1b[0m\n')
            time.sleep(4)
            self.play_round()

    def game_comp_vs_comp(self):
        self.play_game_com()
        self.get_who_won()
        print("\n   Game over!\n\n" +
              'Do you want to watch another match? (yes or no)')
        otherMatch = hinder_invalid_input(SORRY_YES_NO, 'yes no')
        if otherMatch == 'yes':
            self.p1 = random.choice(self.oponents)
            self.p2 = random.choice(self.oponents)
            self.game_comp_vs_comp()
        else:
            self.__init__(Player(), Player())

    def play_round(self):
        move1 = self.p1.move()
        self.p2.bad_luck(move1)
        move2 = self.p2.move()
        image1 = ''
        image2 = ''
        if move1 == MOVES[0]:
            image1 = HANDS[0]
        elif move1 == MOVES[1]:
            image1 = HANDS[1]
        elif move1 == MOVES[2]:
            image1 = HANDS[2]
        if move2 == MOVES[0]:
            image2 = HANDS[0]
        elif move2 == MOVES[1]:
            image2 = HANDS[1]
        elif move2 == MOVES[2]:
            image2 = HANDS[2]
        strategy1 = self.p1.tactic()
        strategy2 = self.p2.tactic()
        if strategy1 == '' and self.revealStrategyMode is False:
            print('\x1b[31m' + f"{self.my_name}" + '\x1b[0m' +
                  f": {move1} {image1}" +
                  '\x1b[34m' + f"{self.computer_name}" + '\x1b[0m' +
                  f": {move2} {image2}")
        elif strategy1 == '' and self.revealStrategyMode is True:
            print('\x1b[31m' + f"{self.my_name}" + '\x1b[0m' +
                  f" {strategy1}: {move1} {image1}" +
                  '\x1b[34m' + f"{self.computer_name}" + '\x1b[0m' +
                  f" {strategy2}: {move2} {image2}")
        else:
            print('\x1b[31m' + f"{self.my_name}" + '\x1b[0m' +
                  f" {strategy1}: {move1} {image1}" +
                  '\x1b[34m' + f"{self.computer_name}" + '\x1b[0m' +
                  f" {strategy2}: {move2} {image2}")
        if beats(move1, move2) is True:
            self.point_P1 += 1
        elif beats(move2, move1) is True:
            self.point_P2 += 1
        else:
            pass
        print('\n\x1b[31m' + f"{self.my_name}" + '\x1b[0m' +
              f": {self.point_P1} point(s) X " +
              '\x1b[34m' + f"{self.computer_name}" + '\x1b[0m' +
              f": {self.point_P2} point(s)")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def get_who_won(self):
        if self.point_P1 > self.point_P2:
            print('\n\x1b[31m' + f'{self.my_name} has won!' + '\x1b[0m')
        if self.point_P1 < self.point_P2:
            print('\n\x1b[34m' + f'{self.computer_name} has won!' + '\x1b[0m')
        if self.point_P1 == self.point_P2:
            print('\n\x1b[1m' + 'It is a tie!' + '\x1b[0m')
        self.point_P1 = 0
        self.point_P2 = 0