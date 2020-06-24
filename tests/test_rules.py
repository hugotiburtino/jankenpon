import unittest

from jankenpon.tools import beats

class TestAccordanceToRules(unittest.TestCase):

    def test_beats(self):
        self.assertTrue(beats("rock", "scissors"))
        self.assertTrue(beats("paper", "rock"))
        self.assertTrue(beats("scissors", "paper"))
        self.assertFalse(beats("scissors", "scissors"))
        self.assertFalse(beats("paper", "paper"))
        self.assertFalse(beats("rock", "rock"))
        self.assertFalse(beats("scissors", "rock"))
        self.assertFalse(beats("paper", "scissors"))
        self.assertFalse(beats("rock", "paper"))
        

if __name__ == "__main__":
    unittest.main()
