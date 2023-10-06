import unittest
from io import StringIO
from unittest.mock import patch
from game.scrabble import ScrabbleGame, WordOutOfBounds, WordNotValid
from game.board import Board
from game.tile import Tile
from game.tilebag import Tilebag


class TestScrabble(unittest.TestCase):
    def test_scrabble(self):
        game = ScrabbleGame(1)
        self.assertIsNotNone(game.board)
        self.assertIsNotNone(game.tilebag)
        self.assertEqual(len(game.players), 1)

    def test_place_word_horizontal(self):
        game = ScrabbleGame(1)
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        game.place_word(tiles, 7, 7, 'horizontal')
        self.assertEqual(game.board.grid[7][7].letter, Tile('A', 1))
        self.assertEqual(game.board.grid[7][8].letter, Tile('R', 1))
        self.assertEqual(game.board.grid[7][9].letter, Tile('B', 1))
        self.assertEqual(game.board.grid[7][10].letter, Tile('O', 1))
        self.assertEqual(game.board.grid[7][11].letter, Tile('L', 1))

    def test_place_word_vertical(self):
        game = ScrabbleGame(1)
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        game.place_word(tiles, 7, 7, 'vertical')
        self.assertEqual(game.board.grid[7][7].letter, Tile('A', 1))
        self.assertEqual(game.board.grid[8][7].letter, Tile('R', 1))
        self.assertEqual(game.board.grid[9][7].letter, Tile('B', 1))
        self.assertEqual(game.board.grid[10][7].letter, Tile('O', 1))
        self.assertEqual(game.board.grid[11][7].letter, Tile('L', 1))

    def test_place_word_horizontal_outside(self):
        game = ScrabbleGame(1)
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        with self.assertRaises(WordOutOfBounds):
            game.place_word(tiles, 7, 12, 'horizontal')

    def test_place_word_vertical_outside(self):
        game = ScrabbleGame(1)
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        with self.assertRaises(WordOutOfBounds):
            game.place_word(tiles, 12, 7, 'vertical')

    def test_square_occupied(self):
        game = ScrabbleGame(1)
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        game.board.grid[7][8].put_tile(Tile('R', 1))
        game.place_word(tiles, 7, 7, 'horizontal')
        self.assertEqual(game.board.grid[7][7].letter, Tile('A', 1))
        self.assertEqual(game.board.grid[7][8].letter, Tile('R', 1))
        self.assertEqual(game.board.grid[7][9].letter, Tile('B', 1))
        self.assertEqual(game.board.grid[7][10].letter, Tile('O', 1))
        self.assertEqual(game.board.grid[7][11].letter, Tile('L', 1))

    def test_occupied_square_vertical(self):
        game = ScrabbleGame(1)
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        game.board.grid[8][7].put_tile(Tile('R', 1))
        game.place_word(tiles, 7, 7, 'vertical')
        self.assertEqual(game.board.grid[7][7].letter, Tile('A', 1))
        self.assertEqual(game.board.grid[8][7].letter, Tile('R', 1))
        self.assertEqual(game.board.grid[9][7].letter, Tile('B', 1))
        self.assertEqual(game.board.grid[10][7].letter, Tile('O', 1))
        self.assertEqual(game.board.grid[11][7].letter, Tile('L', 1))

    def test_get_scores(self):
        game = ScrabbleGame(1)
        game.players[0].set_name("Dino")
        self.assertEqual(game.get_scores(), {'Dino': 0})

    def test_word_validity(self):
        game = ScrabbleGame(1)
        self.assertTrue(game.check_word_validity([Tile('A', 1),
                                                  Tile('R', 1),
                                                  Tile('B', 1),
                                                  Tile('O', 1),
                                                  Tile('L', 1)]))

    def test_not_valid(self):
        game = ScrabbleGame(1)
        tiles = [Tile('L', 1),
                 Tile('M', 1),
                 Tile('F', 1),
                 Tile('A', 1),
                 Tile('O', 1)]
        with self.assertRaises(WordNotValid):
            game.place_word(tiles, 7, 12, 'horizontal')

    def test_check_left(self):
        game = ScrabbleGame(1)
        game.board.grid[7][7].put_tile(Tile('A', 1))
        self.assertTrue(game.check_left_square(8, 7))
        self.assertTrue(game.check_down_square(7, 6))
        self.assertTrue(game.check_right_square(6, 7))
        self.assertTrue(game.check_up_square(7, 8))

    def test_left_word(self):
        game = ScrabbleGame(1)
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        game.board.grid[4][7].put_tile(Tile("C", 1))
        game.board.grid[5][7].put_tile(Tile("A", 1))
        game.board.grid[6][7].put_tile(Tile("S", 1))
        game.board.grid[7][7].put_tile(Tile("A", 1))
        game.place_word(tiles, 7, 7, "vertical")
        self.assertTrue(len(game.check_word_left(7, 7)) > 0)

    def test_right_word(self):
        game = ScrabbleGame(1)
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        game.board.grid[7][7].put_tile(Tile("C", 1))
        game.board.grid[8][7].put_tile(Tile("A", 1))
        game.board.grid[9][7].put_tile(Tile("S", 1))
        game.board.grid[10][7].put_tile(Tile("A", 1))
        game.place_word(tiles, 7, 7, "vertical")
        self.assertTrue(len(game.check_word_right(7, 7)) > 0)

    def test_up_word(self):
        game = ScrabbleGame(1)
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        game.board.grid[7][4].put_tile(Tile("C", 1))
        game.board.grid[7][5].put_tile(Tile("A", 1))
        game.board.grid[7][6].put_tile(Tile("S", 1))
        game.board.grid[7][7].put_tile(Tile("A", 1))
        game.place_word(tiles, 7, 7, "horizontal")
        self.assertTrue(len(game.check_word_up(7, 7)) > 0)

    def test_down_word(self):
        game = ScrabbleGame(1)
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        game.board.grid[7][7].put_tile(Tile("C", 1))
        game.board.grid[7][8].put_tile(Tile("A", 1))
        game.board.grid[7][9].put_tile(Tile("S", 1))
        game.board.grid[7][10].put_tile(Tile("A", 1))
        game.place_word(tiles, 7, 7, "horizontal")
        self.assertTrue(len(game.check_word_down(7, 7)) > 0)

    def test_word_check_horizontal(self):
        game = ScrabbleGame(1)
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        game.board.grid[4][7].put_tile(Tile("C", 1))
        game.board.grid[5][7].put_tile(Tile("A", 1))
        game.board.grid[6][7].put_tile(Tile("S", 1))
        game.board.grid[7][7].put_tile(Tile("A", 1))
        self.assertEqual(game.check_word_horizontal(7, 7), [Tile("C", 1),
                                                            Tile("A", 1),
                                                            Tile("S", 1),
                                                            Tile("A", 1)])

    @patch('sys.stdout', new_callable=StringIO)
    def test_word_check_vertical(self, mock_stdout):
        game = ScrabbleGame(1)
        tiles = [Tile('A', 1),
                 Tile('R', 1),
                 Tile('B', 1),
                 Tile('O', 1),
                 Tile('L', 1)]
        game.board.grid[7][4].put_tile(Tile("C", 1))
        game.board.grid[7][5].put_tile(Tile("A", 1))
        game.board.grid[7][6].put_tile(Tile("S", 1))
        game.board.grid[7][7].put_tile(Tile("A", 1))
        self.assertEqual(game.check_word_vertical(7, 6), [Tile("C", 1),
                                                          Tile("A", 1),
                                                          Tile("S", 1),
                                                          Tile("A", 1)])
        game.show_board()

    def test_word_check_empty_horizontal(self):
        game = ScrabbleGame(1)
        self.assertEqual(game.check_word_horizontal(7, 7), ["empty"])

    def test_word_check_empty_vertical(self):
        game = ScrabbleGame(1)
        self.assertEqual(game.check_word_vertical(7, 7), ["empty"])


if __name__ == '__main__':
    unittest.main()
