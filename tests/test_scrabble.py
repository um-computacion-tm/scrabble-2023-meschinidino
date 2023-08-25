import unittest
from game.scrabble import ScrabbleGame


class TestScrabble(unittest.TestCase):
    def test_scrabble(self):
        game = ScrabbleGame(1)
        self.assertIsNotNone(game.board)
        self.assertIsNotNone(game.tilebag)
        self.assertEqual(len(game.players), 1)


if __name__ == '__main__':
    unittest.main()
