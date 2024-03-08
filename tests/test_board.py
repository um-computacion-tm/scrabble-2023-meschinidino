import unittest
from io import StringIO
from unittest.mock import patch
from game.board import Board, PlacementOutOfBounds, WordNotValid, WordOutOfBounds
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

    def test_board_score_2(self):
        board = Board()
        board.grid[7][7].set_multiplier(2)
        board.place_tile(7, 7, Tile('A', 1))
        self.assertEqual(board.get_tile(7, 7), Tile('A', 1))
        self.assertEqual(board.grid[7][7].get_multiplier(), 2)

    def test_place_word_horizontal(self):
        board = Board()
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        board.place_word(tiles, 7, 7, 'horizontal')
        self.assertEqual(board.grid[7][7].letter, Tile('A', 1))
        self.assertEqual(board.grid[7][8].letter, Tile('R', 1))
        self.assertEqual(board.grid[7][9].letter, Tile('B', 1))
        self.assertEqual(board.grid[7][10].letter, Tile('O', 1))
        self.assertEqual(board.grid[7][11].letter, Tile('L', 1))

    def test_place_word_vertical(self):
        board = Board()
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        board.place_word(tiles, 7, 7, 'vertical')
        self.assertEqual(board.grid[7][7].letter, Tile('A', 1))
        self.assertEqual(board.grid[8][7].letter, Tile('R', 1))
        self.assertEqual(board.grid[9][7].letter, Tile('B', 1))
        self.assertEqual(board.grid[10][7].letter, Tile('O', 1))
        self.assertEqual(board.grid[11][7].letter, Tile('L', 1))

    def test_place_word_horizontal_outside(self):
        board = Board()
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        with self.assertRaises(WordOutOfBounds):
            board.place_word(tiles, 7, 12, 'horizontal')

    def test_place_word_vertical_outside(self):
        board = Board()
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        with self.assertRaises(WordOutOfBounds):
            board.place_word(tiles, 12, 7, 'vertical')

    def test_square_occupied(self):
        board = Board()
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        board.grid[7][8].put_tile(Tile('R', 1))
        board.place_word(tiles, 7, 7, 'horizontal')
        self.assertEqual(board.grid[7][7].letter, Tile('A', 1))
        self.assertEqual(board.grid[7][8].letter, Tile('R', 1))
        self.assertEqual(board.grid[7][9].letter, Tile('B', 1))
        self.assertEqual(board.grid[7][10].letter, Tile('O', 1))
        self.assertEqual(board.grid[7][11].letter, Tile('L', 1))

    def test_occupied_square_vertical(self):
        board = Board()
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        board.grid[8][7].put_tile(Tile('R', 1))
        board.place_word(tiles, 7, 7, 'vertical')
        self.assertEqual(board.grid[7][7].letter, Tile('A', 1))
        self.assertEqual(board.grid[8][7].letter, Tile('R', 1))
        self.assertEqual(board.grid[9][7].letter, Tile('B', 1))
        self.assertEqual(board.grid[10][7].letter, Tile('O', 1))
        self.assertEqual(board.grid[11][7].letter, Tile('L', 1))

    # def test_not_valid(self):
    #     board = Board()
    #     tiles = [Tile('L', 1),
    #              Tile('M', 1),
    #              Tile('F', 1),
    #              Tile('A', 1),
    #              Tile('O', 1)]
    #     with self.assertRaises(WordNotValid):
    #         board.place_word(tiles, 7, 12, 'horizontal')


    def test_left_word(self):
        board = Board()
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        board.grid[4][7].put_tile(Tile("C", 1))
        board.grid[5][7].put_tile(Tile("A", 1))
        board.grid[6][7].put_tile(Tile("S", 1))
        board.grid[7][7].put_tile(Tile("A", 1))
        board.place_word(tiles, 7, 7, "vertical")
        self.assertTrue(len(board.check_word_left(7, 7)) > 0)

    def test_right_word(self):
        board = Board()
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        board.grid[7][7].put_tile(Tile("C", 1))
        board.grid[8][7].put_tile(Tile("A", 1))
        board.grid[9][7].put_tile(Tile("S", 1))
        board.grid[10][7].put_tile(Tile("A", 1))
        board.place_word(tiles, 7, 7, "vertical")
        self.assertTrue(len(board.check_word_right(7, 7)) > 0)

    def test_up_word(self):
        board = Board()
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        board.grid[7][4].put_tile(Tile("C", 1))
        board.grid[7][5].put_tile(Tile("A", 1))
        board.grid[7][6].put_tile(Tile("S", 1))
        board.grid[7][7].put_tile(Tile("A", 1))
        board.place_word(tiles, 7, 7, "horizontal")
        self.assertTrue(len(board.check_word_up(7, 7)) > 0)

    def test_down_word(self):
        board = Board()
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        board.grid[7][7].put_tile(Tile("C", 1))
        board.grid[7][8].put_tile(Tile("A", 1))
        board.grid[7][9].put_tile(Tile("S", 1))
        board.grid[7][10].put_tile(Tile("A", 1))
        board.place_word(tiles, 7, 7, "horizontal")
        self.assertTrue(len(board.check_word_down(7, 7)) > 0)

    # def test_word_check_horizontal(self):
    #     board = Board()
    #     board.grid[4][7].put_tile(Tile("C", 1))
    #     board.grid[5][7].put_tile(Tile("A", 1))
    #     board.grid[6][7].put_tile(Tile("S", 1))
    #     board.grid[7][7].put_tile(Tile("A", 1))
    #     self.assertEqual(board.check_word_horizontal(7, 7), [Tile("C", 1),
    #                                                          Tile("A", 1),
    #                                                          Tile("S", 1),
    #                                                          Tile("A", 1)])
    #
    # @patch('sys.stdout', new_callable=StringIO)
    # def test_word_check_vertical(self, mock_stdout):
    #     board = Board()
    #     board.grid[7][4].put_tile(Tile("C", 1))
    #     board.grid[7][5].put_tile(Tile("A", 1))
    #     board.grid[7][6].put_tile(Tile("S", 1))
    #     board.grid[7][7].put_tile(Tile("A", 1))
    #     self.assertEqual(board.check_word_vertical(7, 6), [Tile("C", 1),
    #                                                        Tile("A", 1),
    #                                                        Tile("S", 1),
    #                                                        Tile("A", 1)])
    #
    # def test_word_check_empty_horizontal(self):
    #     board = Board()
    #     self.assertEqual(board.check_word_horizontal(7, 7), False)
    #
    # def test_word_check_empty_vertical(self):
    #     board = Board()
    #     self.assertEqual(board.check_word_vertical(7, 7), False)
    #
    # def test_word_vh(self):
    #     board = Board()
    #     self.assertFalse(board.check_word_vh((board.check_word_up, board.check_word_down), 7, 7))
    # def test_word_none(self):
    #     board = Board()
    #     with self.assertRaises(WordNotValid):
    #         board.place_word("asdasd", 7, 7, "horizontal")


if __name__ == '__main__':
    unittest.main()
