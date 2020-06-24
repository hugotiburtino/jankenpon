import random
from jankenpon.tools import hinder_invalid_input, get_computer_name

MOVES = ["rock", "paper", "scissors"]


class Player:
    """
    Abstract class of player

    The only really implemented method is set_name, which works only
    for computer players. The human player overrides this method.
    ...

    Attribute
    ----------
    name : str
    """

    name = ""

    def __init__(self):
        """
        Calls the set_name method
        """
        self.set_name()

    def set_name(self):
        """
        Sets the name of the player
        """
        self.name = get_computer_name()

    def get_name(self):
        """
        Getter for name
        """
        return self.name

    def move(self):
        """
        Makes a move in the round
        """

    def bad_luck(self, their_move):
        """
        Only works for the BadLuckPlayer
        """

    def learn(self, my_move, their_move):
        """
        Method that stores the moves of a round, in order that the player
        can use this knowledge the next round
        """

    def tactic(self):
        """
        Tells the tactic of the player
        """
        return ""


class HumanPlayer(Player):
    """
    Class of the Human Player
    """

    def __init__(self):
        pass

    def set_name(self):
        """
        Ask for the user name and stores it
        """
        print("What is your name?")
        self.name = input().strip()
        if self.name == "":
            self.name = "Player 1"

    def move(self):
        """
        Gets the move choice of the user and returns it
        ...
        Returns
        -------
        str
           The move of the user
        """
        checkspelling = "Move not valid. Please check the spelling."
        move = hinder_invalid_input(checkspelling, MOVES)
        return move


class RandomPlayer(Player):
    """
    Class of the player that simply randomly plays
    """

    def move(self):
        """
        Returns a random choice from the list of moves
        """
        return random.choice(MOVES)

    def tactic(self):
        return "playing randomly"


class ReflectPlayer(Player):
    """
    Class of the player that imitates its opponents last move.
    For example, if at round 1 the oppenent played 'rock', this
    player is going to play 'rock' at round 2.

    ...

    Attribute
    ---------
    nextmove : str
        The next move based on what this player learned from the
        previous round
    """

    def __init__(self):
        """
        Gets its name and initializes the nextmove attribute.
        """
        super().__init__()
        self.nextmove = "I don't know"

    def move(self):
        """
        Returns the move of the player. If it is on the round 1, that means,
        it cannot imitate the last move of its opponent, than it makes a
        random move.
        """
        if self.nextmove == "I don't know":
            return random.choice(MOVES)
        return self.nextmove

    def learn(self, my_move, their_move):
        """
        Sets nextmove attribute as equal to what the opponent played in the
        current round
        """
        self.nextmove = their_move

    def tactic(self):
        return "imitating opponent's last move"


class InteligentReflectPlayer(Player):
    """
    Class of the inteligent reflect player.

    It assumes that the opponent is going to repeat his/her/its last move
    and tries to beat it. For example, if at round 1 the oppenent played
    'rock', this player is going to play 'paper' at round 2.

    Attribute
    ---------
    nextmove : str
        The next move based on what this player learned from the
        previous round
    """

    def __init__(self):
        """
        Gets its name and initializes the nextmove attribute.
        """
        super().__init__()
        self.nextmove = "I don't know"

    def move(self):
        """
        Returns the move of the player.
        If it is on the round 1, that means, it cannot imitate the last
        move of its opponent, then it makes a random move.
        """
        if self.nextmove == "I don't know":
            return random.choice(MOVES)
        return self.nextmove

    def learn(self, my_move, their_move):
        """
        Sets nextmove attribute to beat what the opponent played in the
        current round
        """
        if their_move == "rock":
            self.nextmove = "paper"
        elif their_move == "scissors":
            self.nextmove = "rock"
        elif their_move == "paper":
            self.nextmove = "scissors"

    def tactic(self):
        return "thinking that the opponent will repeat their last move"


class BadLuckPlayer(Player):
    """
    Class of the Bad Luck Player

    It always looses, unless the opponent is also a BadLuckPlayer. In this
    case, it is even more funny to see.

    Attribute
    ---------
    nextmove : str
        The next move based on what this player learned from the
        previous round
    """

    def __init__(self):
        """
        Gets its name and initializes the nextmove attribute.
        """
        super().__init__()
        self.nextmove = random.choice(MOVES)

    def move(self):
        """
        Returns the move(str) of the player
        """
        return self.nextmove

    def bad_luck(self, their_move):
        """
        Simply chooses what is going to loose, according to the opponent's
        current move
        """
        if their_move == "paper":
            self.nextmove = "rock"
        elif their_move == "rock":
            self.nextmove = "scissors"
        elif their_move == "scissors":
            self.nextmove = "paper"

    def tactic(self):
        return "having bad luck"


class CyclePlayer(Player):
    """
    Class of the Cycle Player

    It just rotates the moves. For example, 1st round rock, 2nd round scissors,
    and 3rd paper.

    Attribute
    ---------
    index : int
        The index in the moves list
    """

    def __init__(self):
        """
        Gets its name and initializes the index attribute.
        """
        super().__init__()
        self.index = random.randint(0, 2)

    def move(self):
        """
        Returns the move(str) of the player based on the index in the array
        """
        if self.index > 2:
            self.index = 0
        return MOVES[self.index]

    def learn(self, my_move, their_move):
        """
        Increment the index with one in order to not repeat the move
        """
        self.index += 1

    def tactic(self):
        return "not repeating any of his own moves"


class RockPlayer(Player):
    """
    Class of the Player that always plays rock
    """

    def move(self):
        """
        Return the move 'rock'
        """
        return "rock"

    def tactic(self):
        return 'always playing "rock"'
