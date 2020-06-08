# tools.py
"""
Module with useful tools that are used by different classes
"""

from jankenpon.resources import OPPONENT_NAMES

opponent_name_index = 0

def get_computer_name():
    """
    Gets computer player's name and make it rotate, so that the computer
    name never be repeated.

    -------
    Returns
    str
       The name of the opponent, chosen from a list, according to the 
       current index
    """
    global opponent_name_index
    opponent_name_index += 1
    return OPPONENT_NAMES[opponent_name_index % len(OPPONENT_NAMES)]

def interpret_abbreviation(user_input):
    """
    Get shortcut and returns the real value
    -------
    Returns
    str
       The option of the user as a complete string
    """
    if user_input == 'r':
        user_input = 'rock'
    if user_input == 's':
        user_input = 'scissors'
    if user_input == 'p':
        user_input = 'paper'
    if user_input == 'y':
        user_input = 'yes'
    if user_input == 'n':
        user_input = 'no'
    if user_input == 'q':
        user_input = 'quit'
    if user_input == 'exit':
        user_input = 'quit'
    if user_input == 'e':
        user_input = 'quit'
    return user_input

def hinder_invalid_input(prompt_message, possibilities):
    """
    Forces the user to enter a valid option

    ----------
    Parameters
        prompt_message : str
            The message that the user gets while he/she don't enter a 
            valid option
        possibilities: [str]
            The options that the user has
    """
    while True:
        user_input = input().lower()
        user_input = interpret_abbreviation(user_input)
        if user_input in possibilities:
            return user_input
        else:
            print(prompt_message)

def beats(one, two):
    """
    Evaluates what moves beats what

    -------
    Returns
    bool
        true if the move one beats the move two
    """
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))