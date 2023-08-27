import unittest
from game.board import Board, PlacementOutOfBounds
from game.tile import Tile


class TestBoard(unittest.TestCase):
    def test_board_size(self):
        board = Board()
        self.assertEqual(board.rows, 15)
        self.assertEqual(board.columns, 15)

    def test_board_place_tile(self):
        board = Board()
        board.place_tile(7, 7, Tile('A', 1))
        self.assertEqual(board.grid[7][7].letter, Tile('A', 1))

    def test_board_place_out_of_bounds(self):
        with self.assertRaises(PlacementOutOfBounds):
            board = Board()
            board.place_tile(16, 7, Tile('A', 1))


if __name__ == '__main__':
    unittest.main()
