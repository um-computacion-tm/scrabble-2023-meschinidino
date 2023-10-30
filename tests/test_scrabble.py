import unittest
from io import StringIO
from unittest.mock import patch
from game.scrabble import ScrabbleGame
from game.board import Board
from game.tile import Tile
from game.square import Square
from game.tilebag import Tilebag
from game.scrabble import WordNotInDictionary, WordNotThroughCenter, WordNotValid


class TestScrabble(unittest.TestCase):
    def test_scrabble(self):
        game = ScrabbleGame(1)
        self.assertIsNotNone(game.board)
        self.assertIsNotNone(game.tilebag)
        self.assertEqual(len(game.players), 1)

    def test_get_scores(self):
        game = ScrabbleGame(1)
        game.players[0].set_name("Dino")
        self.assertEqual(game.get_scores(), {'Dino': 0})

    def test_game_over(self):
        game = ScrabbleGame(1)
        game.end_game()
        self.assertEqual(game.game_state, "over")

    def test_game_ongoing(self):
        game = ScrabbleGame(1)
        game.game_state_start()
        self.assertEqual(game.game_state, "ongoing")

    @patch('builtins.input', side_effect=['quit'])
    def test_start_game(self, mock_input):
        game = ScrabbleGame(1)
        game.end_game()
        self.assertEqual(game.game_state, "over")

    def test_check_empty_tilebag(self):
        game = ScrabbleGame(1)
        game.tilebag.tiles = []
        game.check_tiles()
        self.assertEqual(game.game_state, "over")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['Dino', 'scores', 'quit'])
    def test_start_game(self, mock_input, mock_stdout):
        game = ScrabbleGame(1)
        game.end_game()
        self.assertEqual(game.game_state, "over")

    def test_last_player_turn(self):
        game = ScrabbleGame(2)
        game.current_player_index = 1
        game.pass_turn()
        self.assertEqual(game.current_player_index, 0)

    def test_player_pass_turn(self):
        game = ScrabbleGame(2)
        game.pass_turn()
        self.assertEqual(game.current_player_index, 1)

    def test_turn_word(self):
        game = ScrabbleGame(1)
        game.players[game.current_player_index].tiles = \
            [Tile('H', 1),
             Tile('O', 1),
             Tile('L', 1),
             Tile('A', 1)]
        game.play_word('hola', 7, 7, 'horizontal')
        self.assertEqual(game.board.grid[7][7].letter, Tile('H', 1))
        self.assertEqual(game.board.grid[7][8].letter, Tile('O', 1))
        self.assertEqual(game.board.grid[7][9].letter, Tile('L', 1))
        self.assertEqual(game.board.grid[7][10].letter, Tile('A', 1))
        self.assertEqual(game.players[game.current_player_index].score, 4)

    def test_player_draw_cards(self):
        game = ScrabbleGame(1)
        game.players[game.current_player_index].tiles = \
            [Tile('P', 1),
             Tile('L', 1),
             Tile('A', 1),
             Tile('Y', 1)]
        game.draw_tiles(1)
        self.assertEqual(len(game.players[game.current_player_index - 1].tiles), 5)

    def test_start_player_tiles(self):
        game = ScrabbleGame(1)
        game.start_player_tiles()
        self.assertEqual(len(game.players[game.current_player_index].tiles), 7)

    @patch('builtins.input', side_effect=['Dino'])
    def test_get_player_names(self, mock_input):
        game = ScrabbleGame(1)
        game.get_player_names()
        self.assertEqual(game.players[game.current_player_index].get_name(), "Dino")


class TestValidateWord(unittest.TestCase):
    def test_validate_word(self):
        game = ScrabbleGame(1)
        word = "arbol"
        checked = game.validate_word(word, 7, 7, 'horizontal')
        self.assertEqual(checked, [])

    def test_word_not_in_dict(self):
        game = ScrabbleGame(1)
        word = "aaaaaaaaa"
        with self.assertRaises(WordNotInDictionary):
            game.validate_word(word, 7, 7, 'horizontal')

    def test_word_not_centered(self):
        game = ScrabbleGame(1)
        word = "arbol"
        with self.assertRaises(WordNotThroughCenter):
            game.validate_word(word, 6, 6, 'horizontal')

    def test_find_letters_on_board(self):
        game = ScrabbleGame(1)
        game.players[game.current_player_index].tiles = \
            [Tile('R', 1),
             Tile('B', 1),
             Tile('L', 1)]
        game.board.grid[7][7].set_tile(Tile('A', 1))
        game.board.grid[7][10].set_tile(Tile('O', 1))
        letters = game.find_letters_on_board('arbol', 7, 7, 'horizontal')
        self.assertEqual(letters, [Tile('A', 1), Tile('O', 1)])

    def test_find_letters_on_board_vertical(self):
        game = ScrabbleGame(1)
        game.board.grid[7][7].set_tile(Tile('A', 1))
        game.board.grid[10][7].set_tile(Tile('O', 1))
        letters = game.find_letters_on_board('arbol', 7, 7, 'vertical')
        self.assertEqual(letters, [Tile('A', 1), Tile('O', 1)])

    def test_validate_word_final(self):
        game = ScrabbleGame(1)
        word = "arbol"
        game.board.grid[7][7].set_tile(Tile('A', 1))
        game.board.grid[10][7].set_tile(Tile('O', 1))
        self.assertEqual(game.validate_word(word, 7, 7, 'vertical'), [Tile('A', 1), Tile('O', 1)])

    def test_combine_word_and_hand(self):
        game = ScrabbleGame(1)
        game.players[game.current_player_index].tiles = \
            [Tile('R', 1),
             Tile('B', 1),
             Tile('L', 1)]
        word = [Tile('A', 1),
                Tile('R', 1),
                Tile('B', 1),
                Tile('O', 1),
                Tile('L', 1)]
        combined = game.combine_board_and_hand([Tile('A', 1), Tile('O', 1)], 'arbol')
        self.assertEqual(combined, word)

    def test_combine_word_and_hand2(self):
        game = ScrabbleGame(1)
        tiles = \
            [Tile('H', 1),
             Tile('O', 1),
             Tile('L', 1),
             Tile('A', 1)]
        game.players[game.current_player_index].tiles = \
            [Tile('H', 1),
             Tile('O', 1),
             Tile('L', 1),
             Tile('A', 1)]
        combined = game.combine_board_and_hand([], "hola")
        self.assertEqual(combined, tiles)


if __name__ == '__main__':
    unittest.main()
