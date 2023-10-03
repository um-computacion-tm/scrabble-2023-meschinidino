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
        game = ScrabbleGame(1)
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
        self.assertEqual(8, word_score(letters))

    def test_word_list_scores(self):
        game = ScrabbleGame(1)
        board = Board()
        board.grid[7][7].set_multiplier(2)
        board.grid[7][8].set_word_multiplier(2)
        word1 = []
        word2 = []
        words = []
        board.place_tile(7, 7, Tile('A', 1))
        board.place_tile(7, 8, Tile('R', 1))
        board.place_tile(7, 9, Tile('B', 1))
        board.place_tile(7, 10, Tile('O', 1))
        board.place_tile(7, 11, Tile('L', 1))
        board.place_tile(8, 7, Tile('Z', 1))
        board.place_tile(9, 7, Tile('U', 1))
        board.place_tile(10, 7, Tile('L', 1))
        for i in range(5):
            word1.append(board.get_square(7, 7 + i))
        for i in range(5):
            word2.append(board.get_square(7 + i, 7))
        words.append(word1)
        words.append(word2)
        self.assertEqual(list_word_score(words), 13)


if __name__ == '__main__':
    unittest.main()
