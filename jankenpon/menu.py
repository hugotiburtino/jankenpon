# menu.py

import sys
import random
from jankenpon.resources import (HOW_TO_PLAY, MENU_OPTIONS, 
                                 MENU_OPTIONS_PROMPT, INTRO)
from jankenpon.tools import hinder_invalid_input


class Menu:

    def show_intro(self):
        print(INTRO)

    def choose_game(self):
        self.game_choice = hinder_invalid_input(MENU_OPTIONS_PROMPT, 
                                                MENU_OPTIONS)

        if self.game_choice == '1':
            return 'human_vs_computer'

        elif self.game_choice == '2':
            return 'computer_vs_computer'

        elif self.game_choice == '3':
            print(HOW_TO_PLAY)
            self.choose_game()

        elif self.game_choice in ['q', 'quit', 'exit', 'e']:
            print('Bye bye!')
            sys.exit()

        else:
            self.choose_game()