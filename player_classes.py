import random
from tools import alternative_choices, valid_option, beats

MOVES = ['rock', 'paper', 'scissors']

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
        return 'not repeating any of his own moves'


class RockPlayer(Player):
    def move(self):
        return 'rock'

    def tactic(self):
        return 'always playing "rock"'