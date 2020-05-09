#!/usr/bin/env python3
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
import time
import sys
from resources import (HANDS, HOW_TO_PLAY, MENU_IMAGE, MENU_OPTIONS, 
                       MENU_OPTIONS_PROMPT, SORRY_YES_NO, INTRO,
                       OPPONENT_NAMES, HOW_TO_PLAY)

MOVES = ['rock', 'paper', 'scissors']

def alternative_choices(option):
        if option == 'r':
            option = 'rock'
        if option == 's':
            option = 'scissors'
        if option == 'p':
            option = 'paper'
        if option == 'y':
            option = 'yes'
        if option == 'n':
            option = 'no'
        return option


def valid_option(prompt, possibilities):
    while True:
        option = input().lower()
        option = alternative_choices(option)
        if option in possibilities:
            return option
        else:
            print(prompt)


class Player:
    def move(self):
        pass

    def bad_luck(self, their_move):
        pass

    def learn(self, my_move, their_move):
        pass

    def tactic(self):
        pass


class HumanPlayer(Player):
    def move(self):
        checkspelling = 'Move not valid. Please check the spelling.'
        myMove = valid_option(checkspelling, MOVES)
        return myMove

    def tactic(self):
        return ''


class RandomPlayer(Player):
    def move(self):
        return random.choice(MOVES)

    def tactic(self):
        return 'playing randomly'


class ReflectPlayer(Player):
    def __init__(self):
        self.nextmove = "I don't Know"

    def move(self):
        if self.nextmove == "I don't Know":
            return random.choice(MOVES)
        else:
            return self.nextmove

    def learn(self, my_move, their_move):
        self.nextmove = their_move

    def tactic(self):
        return 'imitating opponent\'s last move'


class InteligentReflectPlayer(Player):
    def __init__(self):
        self.nextmove = "I don't Know"

    def move(self):
        if self.nextmove == "I don't Know":
            return random.choice(MOVES)
        else:
            return self.nextmove

    def learn(self, my_move, their_move):
        if their_move == 'rock':
            self.nextmove = 'paper'
        elif their_move == 'scissors':
            self.nextmove = 'rock'
        elif their_move == 'paper':
            self.nextmove = 'scissors'

    def tactic(self):
        return 'thinking that the opponent will repeat their last move'


class BadLuckPlayer(Player):
    def __init__(self):
        self.nextmove = random.choice(MOVES)

    def move(self):
        return self.nextmove

    def bad_luck(self, their_move):
        if their_move == 'paper':
            self.nextmove = 'rock'
        elif their_move == 'rock':
            self.nextmove = 'scissors'
        elif their_move == 'scissors':
            self.nextmove = 'paper'

    def tactic(self):
        return 'having bad luck'


class CyclePlayer(Player):
    def __init__(self):
        self.index = random.randint(0, 2)

    def move(self):
        if self.index > 2:
            self.index = 0
        return MOVES[self.index]

    def learn(self, my_move, their_move):
        self.index += 1

    def tactic(self):
        return 'not repeating any of his own MOVES'


class RockPlayer(Player):
    def move(self):
        return 'rock'

    def tactic(self):
        return 'always playing "rock"'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        print(INTRO)
        self.point_P1 = 0
        self.point_P2 = 0
        self.myName = ''
        self.ComputerName = ''
        self.opon = 0
        self.oponents = [BadLuckPlayer(), InteligentReflectPlayer(),
                         ReflectPlayer(), CyclePlayer(),
                         RandomPlayer(), RockPlayer()]
        self.revealStrategyMode = False
        self.chooseGame()

    def chooseGame(self):
        self.game_option = valid_option(MENU_OPTIONS_PROMPT , MENU_OPTIONS)

        if self.game_option == '1':
            self.p1 = HumanPlayer()
            self.p2 = random.choice(self.oponents)
            self.getPlayerName()
            self.getComputerName()
            self.game_humVscomp()

        elif self.game_option == '2':
            self.p1 = random.choice(self.oponents)
            self.p2 = random.choice(self.oponents)
            self.game_compVscomp()

        elif self.game_option == '3':
            print(HOW_TO_PLAY)
            self.chooseGame()

        elif self.game_option in ['q', 'quit', 'exit', 'e']:
            print('Bye bye!')
            sys.exit()

        else:
            self.chooseGame()

    def getPlayerName(self):
        print('What is your name?')
        self.myName = input()
        if self.myName == '':
            self.myName = 'Player 1'

    def getComputerName(self):
        if self.opon == len(OPPONENT_NAMES) - 1:
            self.opon = 0
        else:
            self.opon += 1
        self.ComputerName = OPPONENT_NAMES[self.opon]

    def play_game_hum(self):
        print("\n     Game start!\n")
        for round in range(3):
            print('\x1b[6;37;41m' + f" X---- ROUND {round+1} ----X "
                  + '\x1b[0m')
            print('\x1b[33m'+'r'+'\x1b[0m'+'ock, ' + '\x1b[33m' +
                  'p'+'\x1b[0m' + 'aper or '+'\x1b[33m' +
                  's'+'\x1b[0m' + 'cissors?')
            self.play_round()

    def game_humVscomp(self):
        self.play_game_hum()
        self.WhoWon()
        print("\n    Game over!\n")
        print('Do you want to play again? (yes or no)')
        play_again = valid_option(SORRY_YES_NO, 'yes no')
        if play_again == 'yes':
            print('Do you want to know your opponent\'s strategy? (yes or no)')
            reveal_mode = valid_option(SORRY_YES_NO, 'yes no')
            if reveal_mode == 'yes':
                self.revealStrategyMode = True
            else:
                self.revealStrategyMode = False
            self.getComputerName()
            self.p2 = random.choice(self.oponents)
            self.game_humVscomp()
        else:
            self.__init__(Player(), Player())

    def play_game_com(self):
        print("\n   Game start!")
        self.myName = random.choice(OPPONENT_NAMES)
        self.ComputerName = random.choice(OPPONENT_NAMES)
        if self.myName == self.ComputerName:
            self.ComputerName = self.myName + ' Bad Twin'
        for round in range(3):
            print('\n\x1b[6;37;41m' + f" X---- ROUND {round+1} ----X "
                  + '\x1b[0m\n')
            time.sleep(4)
            self.play_round()

    def game_compVscomp(self):
        self.play_game_com()
        self.WhoWon()
        print("\n   Game over!\n\n" +
              'Do you want to watch another match? (yes or no)')
        otherMatch = valid_option(SORRY_YES_NO, 'yes no')
        if otherMatch == 'yes':
            self.p1 = random.choice(self.oponents)
            self.p2 = random.choice(self.oponents)
            self.game_compVscomp()
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
            print('\x1b[31m' + f"{self.myName}" + '\x1b[0m' +
                  f": {move1} {image1}" +
                  '\x1b[34m' + f"{self.ComputerName}" + '\x1b[0m' +
                  f": {move2} {image2}")
        elif strategy1 == '' and self.revealStrategyMode is True:
            print('\x1b[31m' + f"{self.myName}" + '\x1b[0m' +
                  f" {strategy1}: {move1} {image1}" +
                  '\x1b[34m' + f"{self.ComputerName}" + '\x1b[0m' +
                  f" {strategy2}: {move2} {image2}")
        else:
            print('\x1b[31m' + f"{self.myName}" + '\x1b[0m' +
                  f" {strategy1}: {move1} {image1}" +
                  '\x1b[34m' + f"{self.ComputerName}" + '\x1b[0m' +
                  f" {strategy2}: {move2} {image2}")
        if beats(move1, move2) is True:
            self.point_P1 += 1
        elif beats(move2, move1) is True:
            self.point_P2 += 1
        else:
            pass
        print('\n\x1b[31m' + f"{self.myName}" + '\x1b[0m' +
              f": {self.point_P1} point(s) X " +
              '\x1b[34m' + f"{self.ComputerName}" + '\x1b[0m' +
              f": {self.point_P2} point(s)")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def WhoWon(self):
        if self.point_P1 > self.point_P2:
            print('\n\x1b[31m' + f'{self.myName} has won!' + '\x1b[0m')
        if self.point_P1 < self.point_P2:
            print('\n\x1b[34m' + f'{self.ComputerName} has won!' + '\x1b[0m')
        if self.point_P1 == self.point_P2:
            print('\n\x1b[1m' + 'It is a tie!' + '\x1b[0m')
        self.point_P1 = 0
        self.point_P2 = 0


if __name__ == '__main__':
    game = Game(Player(), Player())
