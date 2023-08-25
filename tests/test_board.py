import unittest
from game.board import Board
from game.tile import Tile


class TestBoard(unittest.TestCase):
    def test_board_size(self):
        board = Board(15, 15)
        self.assertEqual(board.rows, 15)
        self.assertEqual(board.columns, 15)

    def test_board_place_tile(self):
        board = Board(15, 15)
        board.place_tile(7, 7, Tile('A', 1))
        self.assertEqual(board.grid[7][7].letter, Tile('A', 1))

    def test_board_score(self):
        board = Board(15, 15)
        letters = []
        board.place_tile(7, 7, Tile('A', 1))
        board.place_tile(7, 8, Tile('R', 1))
        board.place_tile(7, 9, Tile('B', 1))
        board.place_tile(7, 10, Tile('O', 1))
        board.place_tile(7, 11, Tile('L', 1))
        for i in range(5):
            letters.append(board.get_tile(7, 7 + i))
        self.assertEqual(5, board.word_score(letters))

    def test_board_score_multipliers(self):
        board = Board(15, 15)
        board.grid[7][7].set_multiplier(2)
        board.grid[7][8].set_word_multiplier(2)
        letters = []
        board.place_tile(7, 7, Tile('A', 1))
        board.place_tile(7, 8, Tile('R', 1))
        board.place_tile(7, 9, Tile('B', 1))
        board.place_tile(7, 10, Tile('O', 1))
        board.place_tile(7, 11, Tile('L', 1))
        for i in range(5):
            letters.append(board.get_tile(7, 7 + i))
        self.assertEqual(12, board.word_score(letters))

    def board_test_score_2(self):
        board = Board(15, 15)
        board.grid[7][7].set_multiplier(2)
        board.place_tile(7, 7, Tile('A', 1))
        self.assertEqual(board.get_tile(7, 7), Tile('A', 1))
        self.assertEqual(board.grid[7][7].get_multiplier(), 2)


if __name__ == '__main__':
    unittest.main()
