import unittest
from unittest.mock import patch
from game.scrabble import ScrabbleGame, WordOutOfBounds
from game.board import Board
from game.tile import Tile
from game.tilebag import Tilebag


class TestScrabble(unittest.TestCase):
    def test_scrabble(self):
        game = ScrabbleGame(1)
        self.assertIsNotNone(game.board)
        self.assertIsNotNone(game.tilebag)
        self.assertEqual(len(game.players), 1)

    def test_word_validation(self):
        game = ScrabbleGame(1)
        word = [Tile('A', 1),
                Tile('R', 1),
                Tile('B', 1),
                Tile('O', 1),
                Tile('L', 1)]
        # game.insert_word(word, row=7, column=7, 'horizontal')

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
        self.assertEqual(5, game.word_score(letters))

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
        self.assertEqual(12, game.word_score(letters))

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

    def test_player_turn_pass(self):
        game = ScrabbleGame(2)
        game.player_turn('pass')
        self.assertEqual(game.current_player_index, 1)

    def test_last_player_turn(self):
        game = ScrabbleGame(2)
        game.current_player_index = 1
        game.player_turn('pass')
        self.assertEqual(game.current_player_index, 0)

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

    # @patch('game.scrabble.input', side_effect=['play', '7', '7', 'horizontal'])
    # def test_turn_word(self, mock_input):
    #     game = ScrabbleGame(1)
    #     game.players[game.current_player_index].tiles = [Tile('P', 1),
    #              Tile('L', 1),
    #              Tile('A', 1),
    #              Tile('Y', 1)]
    #     game.player_turn('play')
    #     result = game.player_turn('play')
    #     self.assertTrue(result['success'])
    #     self.assertEqual(len(game.players[0].tiles), 7)
    #     self.assertEqual(game.board.get_tile(7, 7).get_letter().get_value(), 1)
    #     self.assertTrue(game.players[0].score > 0)
    #     self.assertTrue(len(game.players[0].tiles) < 7)


if __name__ == '__main__':
    unittest.main()
