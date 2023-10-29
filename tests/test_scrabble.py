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
        word = [Tile('A', 1),
                Tile('R', 1),
                Tile('B', 1),
                Tile('O', 1),
                Tile('L', 1)]
        checked = game.validate_word(word, 7, 7, 'horizontal')
        self.assertEqual(checked, word)

    def test_word_not_in_dict(self):
        game = ScrabbleGame(1)
        word = [Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1),
                Tile('A', 1), Tile('A', 1), Tile('A', 1)]
        with self.assertRaises(WordNotInDictionary):
            game.validate_word(word, 7, 7, 'horizontal')

    def test_word_not_centered(self):
        game = ScrabbleGame(1)
        word = [Tile('A', 1),
                Tile('R', 1),
                Tile('B', 1),
                Tile('O', 1),
                Tile('L', 1)]
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
        word = [Tile('A', 1),
                Tile('R', 1),
                Tile('B', 1),
                Tile('O', 1),
                Tile('L', 1)]
        game.players[game.current_player_index].tiles = \
            [Tile('R', 1),
             Tile('B', 1),
             Tile('L', 1)]
        game.board.grid[7][7].set_tile(Tile('A', 1))
        game.board.grid[10][7].set_tile(Tile('O', 1))
        self.assertEqual(game.validate_word(word, 7, 7, 'vertical'), [Tile('R', 1),
                                                                      Tile('B', 1),
                                                                      Tile('L', 1)])



#
#     def test_word_overlaps(self):
#         game = ScrabbleGame(1)
#         word = [Tile('A', 1),
#                 Tile('R', 1),
#                 Tile('B', 1),
#                 Tile('O', 1),
#                 Tile('L', 1)]
#         game.board.grid[7][7].put_tile(Tile('R', 1))
#         checked = game.validate_word(word, 7, 6, 'horizontal')
#         self.assertEqual(checked, [Tile('A', 1),
#                                    Tile('B', 1),
#                                    Tile('O', 1),
#                                    Tile('L', 1)])
#
#     def test_word_overlaps_fail(self):
#         game = ScrabbleGame(1)
#         word = [Tile('A', 1),
#                 Tile('R', 1),
#                 Tile('B', 1),
#                 Tile('O', 1),
#                 Tile('L', 1)]
#         game.board.grid[7][7].put_tile(Tile('R', 1))
#         with self.assertRaises(WordNotValid):
#             game.validate_word(word, 7, 7, 'horizontal')


# @patch('builtins.input', side_effect=['pass'])
# def test_player_turn_pass(self, mock_input):
#     game = ScrabbleGame(1)
#     game.play_turn()
#     self.assertEqual(game.current_player_index, 1)

# @patch('sys.stdout', new_callable=StringIO)

#
# @patch('sys.stdout', new_callable=StringIO)
# @patch('builtins.input', side_effect=['Dino', 'not an action', 'quit'])
# def test_action_not_valid(self, mock_input, mock_stdout):
#     game = ScrabbleGame(1)
#     square = Square()
#     square.put_tile(Tile('A', 1))
#     game.board.grid[7][7] = square
#     game.game_state_start()
#     self.assertEqual(mock_stdout.getvalue().strip(), "Action not valid, please choose from: pass, play, draw, "
#                                                      "quit, scores, tiles, board")
#     self.assertEqual(game.game_state, "over")
#
# @patch('sys.stdout', new_callable=StringIO)
# @patch('builtins.input', side_effect=['hola', '7', '7', 'horizontal'])
# def test_first_turn(self, mock_input, mock_stdout):
#     game = ScrabbleGame(1)
#
#     game.players[game.current_player_index].tiles = \
#         [Tile('H', 1),
#          Tile('O', 1),
#          Tile('L', 1),
#          Tile('A', 1)]
#     game.first_turn()
#     self.assertEqual(game.board.grid[7][7].letter, Tile('H', 1))
#     self.assertEqual(game.board.grid[7][8].letter, Tile('O', 1))
#     self.assertEqual(game.board.grid[7][9].letter, Tile('L', 1))
#     self.assertEqual(game.board.grid[7][10].letter, Tile('A', 1))
#
# @patch('sys.stdout', new_callable=StringIO)
# @patch('builtins.input', side_effect=['hola', '0', '7', 'horizontal'])
# def test_first_turn_wrong(self, mock_input, mock_stdout):
#     game = ScrabbleGame(1)
#
#     game.players[game.current_player_index].tiles = \
#         [Tile('H', 1),
#          Tile('O', 1),
#          Tile('L', 1),
#          Tile('A', 1)]
#     game.first_turn()
#     self.assertFalse(game.board.grid[0][7].has_tile())
#
# @patch('sys.stdout', new_callable=StringIO)
# @patch('builtins.input', side_effect=["Dino", 'hola', '7', '7', 'horizontal', 'quit'])
# def test_game_start_board_empty(self, mock_input, mock_stdout):
#     game = ScrabbleGame(1)
#     game.players[game.current_player_index].tiles = \
#         [Tile('H', 1),
#          Tile('O', 1),
#          Tile('L', 1),
#          Tile('A', 1)]
#     game.game_state_start()
#     self.assertTrue(game.board.grid[7][7].has_tile())
#     self.assertEqual(game.board.grid[7][7].letter, Tile('H', 1))


if __name__ == '__main__':
    unittest.main()
