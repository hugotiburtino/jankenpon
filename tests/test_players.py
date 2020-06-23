# test_players.py

import unittest

from jankenpon.player_classes import ReflectPlayer, InteligentReflectPlayer, CyclePlayer


class TestReflectPlayer(unittest.TestCase):

    rp = ReflectPlayer()

    def test_learn(self):
        self.rp.learn("paper", "rock")
        self.assertEqual(self.rp.move(), "rock")
        self.rp.learn("scissors", "paper")
        self.assertEqual(self.rp.move(), "paper")
        self.rp.learn("paper", "scissors")
        self.assertEqual(self.rp.move(), "scissors")


class TestInteligentReflectPlayer(unittest.TestCase):

    irp = InteligentReflectPlayer()

    def test_learn(self):
        self.irp.learn("rock", "rock")
        self.assertEqual(self.irp.move(), "paper")
        self.irp.learn("rock", "paper")
        self.assertEqual(self.irp.move(), "scissors")
        self.irp.learn("paper", "scissors")
        self.assertEqual(self.irp.move(), "rock")


class TestCyclePlayer(unittest.TestCase):

    cp = CyclePlayer()

    def test_moves_rotation(self):
        moves = [self.cp.move()]
        self.cp.learn("", "rock")
        moves.append(self.cp.move())
        self.cp.learn("", "rock")
        moves.append(self.cp.move())
        self.assertEqual(sorted(["rock", "paper", "scissors"]), sorted(moves))


if __name__ == "__main__":
    unittest.main()
