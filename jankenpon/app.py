# app.py

"""
This program runs a game of 'Rock Paper Scissors' between two players,
and reports both player's scores each round as well as the possible winner
"""

import random
import time
from jankenpon.player_classes import (
    HumanPlayer,
    RockPlayer,
    CyclePlayer,
    BadLuckPlayer,
    InteligentReflectPlayer,
    ReflectPlayer,
    RandomPlayer,
)
from jankenpon.tools import beats
from jankenpon.displayer import Displayer

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
    displayer : Displayer
        object that manages what the user sees

    """

    displayer = Displayer()

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
        self.displayer.show_intro()
        self.set_game(self.displayer.choose_game())
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
        self.endgame()

    def play_game(self):
        """
        Shows the name and round number and calls the play round function
        """
        print("\n     Game start!\n")
        if self.p1.get_name() == self.p2.get_name():
            self.p2.name = self.p1.get_name() + " Bad Twin"
        for match_round in range(3):
            self.displayer.show_round(match_round + 1)
            if isinstance(self.p1, HumanPlayer):
                self.displayer.show_move_options()
            else:
                time.sleep(4)
            self.play_round()

    def play_round(self):  # TODO: still refactor this method, too long
        """
        Core of the game. Takes the moves of the players, apply the rule to
        get the score, and display the ASCII arts as well as the names and
        score. At the end, make the computer player(s) learn from this round.
        """
        move1 = self.p1.move()
        self.p2.bad_luck(move1)
        move2 = self.p2.move()
        self.displayer.display_match(
            self.reveal_strategy_mode, self.p1, self.p2, move1, move2,
        )
        if beats(move1, move2) is True:
            self.score_p1 += 1
        elif beats(move2, move1) is True:
            self.score_p2 += 1
        self.displayer.show_score(self.p1, self.p2, self.score_p1, self.score_p2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def get_who_won(self):
        """
        Gets the winner from the score and displays him/her.
        It also reset the score.
        """
        self.displayer.show_winner(self.score_p1, self.score_p2, self.p1, self.p2)
        self.score_p1 = 0
        self.score_p2 = 0

    def endgame(self):
        """
        Shows the "game over" message and, if the user was playing,
        asks if the user wants to play again and if she/he
        wants to know to strategy of the opponent next time.
        If the game was computer vs computer, asks if the user wants
        to see another game.
        """
        print("\n    Game over!\n")
        if isinstance(self.p1, HumanPlayer):
            choices = self.displayer.show_gameover_hum()
            if choices["playagain"] is True:
                self.reveal_strategy_mode = choices["reveal_mode"]
                self.p2 = random.choice(OPPONENTS)()
                self.run_game()
            else:
                self.__init__(None, None)
                self.intro()
        else:
            if self.displayer.show_gameover_comp() == "yes":
                self.p1 = random.choice(OPPONENTS)()
                self.p2 = random.choice(OPPONENTS)()
                self.run_game()
            else:
                self.__init__(None, None)
                self.intro()
