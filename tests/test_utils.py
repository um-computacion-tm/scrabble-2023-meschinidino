import unittest
from game.scrabble import ScrabbleGame
from game.board import Board
from game.tile import Tile
from game.utils import *
from game.square import Square


class MyTestCase(unittest.TestCase):
    def test_word_score(self):
        game = ScrabbleGame(1)
        board = Board()
        letters = []
        board.place_tile(7, 7, Tile('A', 1))
        board.place_tile(7, 8, Tile('R', 1))
        board.place_tile(7, 9, Tile('B', 1))
        board.place_tile(7, 10, Tile('O', 1))
        board.place_tile(7, 11, Tile('L', 1))
        for i in range(5):
            letters.append(board.get_square(7, 7 + i))
        self.assertEqual(6, word_score(letters))

    def test_word_score_multipliers(self):
        board = Board()
        board.grid[7][7].set_multiplier(2)
        board.grid[7][8].set_word_multiplier(2)
        letters = []
        board.place_tile(7, 7, Tile('A', 1))
        board.place_tile(7, 8, Tile('R', 1))
        board.place_tile(7, 9, Tile('B', 1))
        board.place_tile(7, 10, Tile('O', 1))
        board.place_tile(7, 11, Tile('L', 1))
        for i in range(5):
            letters.append(board.get_square(7, 7 + i))
        self.assertEqual(16, word_score(letters))

    def test_word_list_scores(self):
        words = [[Tile("C", 1),
                  Tile("A", 1),
                  Tile("S", 1),
                  Tile("A", 1)],

                 [Tile("C", 1),
                  Tile("A", 1),
                  Tile("S", 1),
                  Tile("A", 1)],

                 [Tile("C", 1),
                  Tile("A", 1),
                  Tile("S", 1),
                  Tile("A", 1)]]
        self.assertEqual(list_word_score(words), 12)

    def test_word_validity(self):
        game = Board()
        self.assertTrue(check_word_dictionary([Tile('A', 1),
                                               Tile('R', 1),
                                               Tile('B', 1),
                                               Tile('O', 1),
                                               Tile('L', 1)]))

    def test_board_empty(self):
        board = Board()
        self.assertTrue(is_board_empty(board))

if __name__ == '__main__':
    unittest.main()
