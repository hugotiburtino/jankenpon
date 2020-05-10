#!/usr/bin/env python3
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
import time
from jankenpon.resources import (HANDS, SORRY_YES_NO)
from jankenpon.player_classes import (Player, HumanPlayer,
                                      RockPlayer, CyclePlayer,
                                      BadLuckPlayer, InteligentReflectPlayer,
                                      ReflectPlayer, RandomPlayer, MOVES)
from jankenpon.tools import hinder_invalid_input, beats
from jankenpon.menu import Menu

OPPONENTS = [BadLuckPlayer(), InteligentReflectPlayer(),
             ReflectPlayer(), CyclePlayer(),
             RandomPlayer(), RockPlayer()]

class Game:
    
    menu = Menu()

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0
        self.reveal_strategy_mode = False
        self.menu.show_intro()
        self.set_game(self.menu.choose_game())

    def set_game(self, game_type):
        if game_type == 'human_vs_computer':
            self.p1 = HumanPlayer()
            self.p2 = random.choice(OPPONENTS)
            self.game_hum_vs_comp()
        else:
            self.p1 = random.choice(OPPONENTS)
            self.p2 = random.choice(OPPONENTS)
            self.game_comp_vs_comp()

    def play_game(self):
        print("\n     Game start!\n")
        # TODO: reintroduce this feature
        # if self.p1.get_name() == self.p2.get_name():
        #      self.p2.name = self.p1.get_name() + ' Bad Twin'
        for round in range(3):
            print('\x1b[6;37;41m' + f" X---- ROUND {round+1} ----X "
                  + '\x1b[0m')
            if type(self.p1) == HumanPlayer:
                print('\x1b[33m'+'r'+'\x1b[0m'+'ock, ' + '\x1b[33m' +
                  'p'+'\x1b[0m' + 'aper or '+'\x1b[33m' +
                  's'+'\x1b[0m' + 'cissors?')
            else:
                time.sleep(4)
            self.play_round()

    def game_hum_vs_comp(self):
        self.play_game()
        self.get_who_won()
        print("\n    Game over!\n")
        print('Do you want to play again? (yes or no)')
        play_again = hinder_invalid_input(SORRY_YES_NO, 'yes no')
        if play_again == 'yes':
            print('Do you want to know your opponent\'s strategy? (yes or no)')
            reveal_mode = hinder_invalid_input(SORRY_YES_NO, 'yes no')
            if reveal_mode == 'yes':
                self.reveal_strategy_mode = True
            else:
                self.reveal_strategy_mode = False
            self.p2 = random.choice(OPPONENTS)
            self.game_hum_vs_comp()
        else:
            self.__init__(None, None)

    def game_comp_vs_comp(self):
        self.play_game()
        self.get_who_won()
        print("\n   Game over!\n\n" +
              'Do you want to watch another match? (yes or no)')
        otherMatch = hinder_invalid_input(SORRY_YES_NO, 'yes no')
        if otherMatch == 'yes':
            self.p1 = random.choice(OPPONENTS)
            self.p2 = random.choice(OPPONENTS)
            self.game_comp_vs_comp()
        else:
            self.__init__(None, None)

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
        if strategy1 == '' and self.reveal_strategy_mode is False:
            print('\x1b[31m' + f"{self.p1.get_name()}" + '\x1b[0m' +
                  f": {move1} {image1}" +
                  '\x1b[34m' + f"{self.p2.get_name()}" + '\x1b[0m' +
                  f": {move2} {image2}")
        elif strategy1 == '' and self.reveal_strategy_mode is True:
            print('\x1b[31m' + f"{self.p1.get_name()}" + '\x1b[0m' +
                  f" {strategy1}: {move1} {image1}" +
                  '\x1b[34m' + f"{self.p2.get_name()}" + '\x1b[0m' +
                  f" {strategy2}: {move2} {image2}")
        else:
            print('\x1b[31m' + f"{self.p1.get_name()}" + '\x1b[0m' +
                  f" {strategy1}: {move1} {image1}" +
                  '\x1b[34m' + f"{self.p2.get_name()}" + '\x1b[0m' +
                  f" {strategy2}: {move2} {image2}")
        if beats(move1, move2) is True:
            self.score_p1 += 1
        elif beats(move2, move1) is True:
            self.score_p2 += 1
        else:
            pass
        print('\n\x1b[31m' + f"{self.p1.get_name()}" + '\x1b[0m' +
              f": {self.score_p1} point(s) X " +
              '\x1b[34m' + f"{self.p2.get_name()}" + '\x1b[0m' +
              f": {self.score_p2} point(s)")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def get_who_won(self):
        if self.score_p1 > self.score_p2:
            print('\n\x1b[31m' + f'{self.p1.get_name()} has won!' + '\x1b[0m')
        if self.score_p1 < self.score_p2:
            print('\n\x1b[34m' + f'{self.p2.get_name()} has won!' + '\x1b[0m')
        if self.score_p1 == self.score_p2:
            print('\n\x1b[1m' + 'It is a tie!' + '\x1b[0m')
        self.score_p1 = 0
        self.score_p2 = 0