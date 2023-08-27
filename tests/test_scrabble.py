import unittest
from game.scrabble import ScrabbleGame
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

    def test_board_score(self):
        game = ScrabbleGame(1)
        board = Board()
        letters = []
        board.place_tile(7, 7, Tile('A', 1))
        board.place_tile(7, 8, Tile('R', 1))
        board.place_tile(7, 9, Tile('B', 1))
        board.place_tile(7, 10, Tile('O', 1))
        board.place_tile(7, 11, Tile('L', 1))
        for i in range(5):
            letters.append(board.get_tile(7, 7 + i))
        self.assertEqual(5, game.word_score(letters))

    def test_board_score_multipliers(self):
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
            letters.append(board.get_tile(7, 7 + i))
        self.assertEqual(12, game.word_score(letters))

    def board_test_score_2(self):
        board = Board()
        board.grid[7][7].set_multiplier(2)
        board.place_tile(7, 7, Tile('A', 1))
        self.assertEqual(board.get_tile(7, 7), Tile('A', 1))
        self.assertEqual(board.grid[7][7].get_multiplier(), 2)




if __name__ == '__main__':
    unittest.main()
