# displayer.py

import sys
import random
from jankenpon.resources import HOW_TO_PLAY, MENU_OPTIONS, MENU_OPTIONS_PROMPT, INTRO
from jankenpon.tools import hinder_invalid_input


class Displayer:
    """
    Class that displays messages and images to the user
    much like a View layer at MVC
    """

    def show_intro(self):
        """
        Displays the intro panel
        """
        print(INTRO)

    def choose_game(self):
        """
        Returns the type of game the user has choosen

        Returns
        -------
        str
           the kind of game, namely human vs computer or computer vs computer
        """
        self.game_choice = hinder_invalid_input(MENU_OPTIONS_PROMPT, MENU_OPTIONS)

        if self.game_choice == "1":
            return "human_vs_computer"

        elif self.game_choice == "2":
            return "computer_vs_computer"

        elif self.game_choice == "3":
            print(HOW_TO_PLAY)
            self.choose_game()

        elif self.game_choice in ["q", "quit", "exit", "e"]:
            print("Bye bye!")
            sys.exit()

        else:
            self.choose_game()

    def show_round(self, round_num):
        print("\x1b[6;37;41m" + f" X---- ROUND {round_num} ----X " + "\x1b[0m")

    def show_options(self):
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

    def display_match(
        self,
        reveal_strategy_mode,
        p1,
        p2,
        move1,
        move2,
        image1,
        image2,
        strategy1,
        strategy2,
    ):
        if strategy1 == "" and reveal_strategy_mode is False:
            print(
                "\x1b[31m"
                + f"{p1.get_name()}"
                + "\x1b[0m"
                + f": {move1} {image1}"
                + "\x1b[34m"
                + f"{p2.get_name()}"
                + "\x1b[0m"
                + f": {move2} {image2}"
            )
        elif strategy1 == "" and reveal_strategy_mode is True:
            print(
                "\x1b[31m"
                + f"{p1.get_name()}"
                + "\x1b[0m"
                + f" {strategy1}: {move1} {image1}"
                + "\x1b[34m"
                + f"{p2.get_name()}"
                + "\x1b[0m"
                + f" {strategy2}: {move2} {image2}"
            )
        else:
            print(
                "\x1b[31m"
                + f"{p1.get_name()}"
                + "\x1b[0m"
                + f" {strategy1}: {move1} {image1}"
                + "\x1b[34m"
                + f"{p2.get_name()}"
                + "\x1b[0m"
                + f" {strategy2}: {move2} {image2}"
            )

    def show_score(self, p1, p2, score_p1, score_p2):
        print(
            "\n\x1b[31m"
            + f"{p1.get_name()}"
            + "\x1b[0m"
            + f": {score_p1} point(s) X "
            + "\x1b[34m"
            + f"{p2.get_name()}"
            + "\x1b[0m"
            + f": {score_p2} point(s)"
        )

    def show_winner(self, score_p1, score_p2, p1, p2):
        if score_p1 > score_p2:
            print("\n\x1b[31m" + f"{p1.get_name()} has won!" + "\x1b[0m")
        elif score_p1 < score_p2:
            print("\n\x1b[34m" + f"{p2.get_name()} has won!" + "\x1b[0m")
        else:
            print("\n\x1b[1m" + "It is a tie!" + "\x1b[0m")
