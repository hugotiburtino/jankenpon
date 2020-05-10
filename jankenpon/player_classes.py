import random
from jankenpon.tools import hinder_invalid_input, get_computer_name

MOVES = ['rock', 'paper', 'scissors']

class Player:

    name = ''

    def __init__(self):
        self.set_name()

    def set_name(self):
        self.name = get_computer_name()

    def get_name(self):
        return self.name

    def move(self):
        pass

    def bad_luck(self, their_move):
        pass

    def learn(self, my_move, their_move):
        pass

    def tactic(self):
        return ''


class HumanPlayer(Player):

    def set_name(self):
        print('What is your name?')
        self.name = input().strip()
        if self.name == '':
            self.name = 'Player 1'

    def move(self):
        checkspelling = 'Move not valid. Please check the spelling.'
        myMove = hinder_invalid_input(checkspelling, MOVES)
        return myMove


class RandomPlayer(Player):
    def move(self):
        return random.choice(MOVES)

    def tactic(self):
        return 'playing randomly'


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
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
        super().__init__()
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
        super().__init__()
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
        super().__init__()
        self.index = random.randint(0, 2)

    def move(self):
        if self.index > 2:
            self.index = 0
        return MOVES[self.index]

    def learn(self, my_move, their_move):
        self.index += 1

    def tactic(self):
        return 'not repeating any of his own moves'


class RockPlayer(Player):
    def move(self):
        return 'rock'

    def tactic(self):
        return 'always playing "rock"'