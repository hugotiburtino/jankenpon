# app.py

"""
This program runs a game of 'Rock Paper Scissors' between two players,
and reports both player's scores each round as well as the possible winner
"""

import random
import time
from jankenpon.resources import HANDS, SORRY_YES_NO
from jankenpon.player_classes import (
    HumanPlayer,
    RockPlayer,
    CyclePlayer,
    BadLuckPlayer,
    InteligentReflectPlayer,
    ReflectPlayer,
    RandomPlayer,
    MOVES,
)
from jankenpon.tools import hinder_invalid_input, beats
from jankenpon.menu import Menu

OPPONENTS = [
    BadLuckPlayer,
    InteligentReflectPlayer,
    ReflectPlayer,
    CyclePlayer,
    RandomPlayer,
    RockPlayer,
]


class Game:
    """
    Class that manages the game
    ...
    Attributes
    ----------
    menu : Menu
        an object that manages the menu

    """

    menu = Menu()

    def __init__(self, p1, p2):
        """
        Magic function that starts the game setting players and values 
        to default.
        """
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0
        self.reveal_strategy_mode = False

    def intro(self):
        self.menu.show_intro()
        self.set_game(self.menu.choose_game())
        self.run_game()

    def set_game(self, game_type):
        """
        Sets the the first player as human or computar, randomizes the second
        player and runs the game.

        ...

        Parameters
        ----------
        game_type : str
            The type of game.
            Options: human vs computer or computer vs computer
        """

        if game_type == "human_vs_computer":
            self.p1 = HumanPlayer()
            self.p1.set_name()
        else:
            self.p1 = random.choice(OPPONENTS)()
        self.p2 = random.choice(OPPONENTS)()

    def run_game(self):
        """
        Calls the stages of the game: 
        play, get winner and display the game over panel.
        """
        self.play_game()
        self.get_who_won()
        self.show_gameover()

    def play_game(self):
        """
        Shows the name and round number and calls the play round function
        """
        print("\n     Game start!\n")
        if self.p1.get_name() == self.p2.get_name():
            self.p2.name = self.p1.get_name() + " Bad Twin"
        for round in range(3):
            print("\x1b[6;37;41m" + f" X---- ROUND {round+1} ----X " + "\x1b[0m")
            if isinstance(self.p1, HumanPlayer):
                print(
                    "\x1b[33m"
                    + "r"
                    + "\x1b[0m"
                    + "ock, "
                    + "\x1b[33m"
                    + "p"
                    + "\x1b[0m"
                    + "aper or "
                    + "\x1b[33m"
                    + "s"
                    + "\x1b[0m"
                    + "cissors?"
                )
            else:
                time.sleep(4)
            self.play_round()

    def play_round(self):  # TODO: refactor this method, too long
        """
        Core of the game. Takes the moves of the players, apply the rule to 
        get the score, and display the ASCII arts as well as the names and 
        score. At the end, make the computer player(s) learn from this round.
        """
        move1 = self.p1.move()
        self.p2.bad_luck(move1)
        move2 = self.p2.move()
        image1 = HANDS[MOVES.index(move1)]
        image2 = HANDS[MOVES.index(move2)]
        strategy1 = self.p1.tactic()
        strategy2 = self.p2.tactic()
        if strategy1 == "" and self.reveal_strategy_mode is False:
            print(
                "\x1b[31m"
                + f"{self.p1.get_name()}"
                + "\x1b[0m"
                + f": {move1} {image1}"
                + "\x1b[34m"
                + f"{self.p2.get_name()}"
                + "\x1b[0m"
                + f": {move2} {image2}"
            )
        elif strategy1 == "" and self.reveal_strategy_mode is True:
            print(
                "\x1b[31m"
                + f"{self.p1.get_name()}"
                + "\x1b[0m"
                + f" {strategy1}: {move1} {image1}"
                + "\x1b[34m"
                + f"{self.p2.get_name()}"
                + "\x1b[0m"
                + f" {strategy2}: {move2} {image2}"
            )
        else:
            print(
                "\x1b[31m"
                + f"{self.p1.get_name()}"
                + "\x1b[0m"
                + f" {strategy1}: {move1} {image1}"
                + "\x1b[34m"
                + f"{self.p2.get_name()}"
                + "\x1b[0m"
                + f" {strategy2}: {move2} {image2}"
            )
        if beats(move1, move2) is True:
            self.score_p1 += 1
        elif beats(move2, move1) is True:
            self.score_p2 += 1
        else:
            pass
        print(
            "\n\x1b[31m"
            + f"{self.p1.get_name()}"
            + "\x1b[0m"
            + f": {self.score_p1} point(s) X "
            + "\x1b[34m"
            + f"{self.p2.get_name()}"
            + "\x1b[0m"
            + f": {self.score_p2} point(s)"
        )
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def get_who_won(self):
        """
        Gets the winner from the score and displays him/her. 
        It also reset the score.
        """
        if self.score_p1 > self.score_p2:
            print("\n\x1b[31m" + f"{self.p1.get_name()} has won!" + "\x1b[0m")
        if self.score_p1 < self.score_p2:
            print("\n\x1b[34m" + f"{self.p2.get_name()} has won!" + "\x1b[0m")
        if self.score_p1 == self.score_p2:
            print("\n\x1b[1m" + "It is a tie!" + "\x1b[0m")
        self.score_p1 = 0
        self.score_p2 = 0

    def show_gameover(self):
        """
        Shows the "game over" message and, if the user was playing,
        asks if the user wants to play again and if she/he
        wants to know to strategy of the opponent next time.
        If the game was computer vs computer, asks if the user wants
        to see another game.
        """
        print("\n    Game over!\n")
        if isinstance(self.p1, HumanPlayer):
            print("Do you want to play again? (yes or no)")
            play_again = hinder_invalid_input(SORRY_YES_NO, "yes no")
            if play_again == "yes":
                print("Do you want to know your opponent's strategy? (yes or no)")
                reveal_mode = hinder_invalid_input(SORRY_YES_NO, "yes no")
                if reveal_mode == "yes":
                    self.reveal_strategy_mode = True
                else:
                    self.reveal_strategy_mode = False
                self.p2 = random.choice(OPPONENTS)()
                self.run_game()
            else:
                self.__init__(None, None)
                self.intro()
        else:
            print("Do you want to watch another match? (yes or no)")
            see_another_match = hinder_invalid_input(SORRY_YES_NO, "yes no")
            if see_another_match == "yes":
                self.p1 = random.choice(OPPONENTS)()
                self.p2 = random.choice(OPPONENTS)()
                self.run_game()
            else:
                self.__init__(None, None)
                self.intro()
