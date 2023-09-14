import unittest
from unittest.mock import patch
from game.scrabble_cli import ScrabbleCli
from game.square import Square
from game.tile import Tile
from io import StringIO


class MyTestCase(unittest.TestCase):

    @patch('builtins.input', side_effect=['play', 'hola', '7', '7', 'horizontal'])
    def test_turn_word(self, mock_input):
        scrabblecli = ScrabbleCli()
        scrabblecli.game.players[scrabblecli.game.current_player_index].tiles = \
            [Tile('H', 1),
             Tile('O', 1),
             Tile('L', 1),
             Tile('A', 1)]
        scrabblecli.player_turn()
        self.assertEqual(scrabblecli.game.board.grid[7][7].letter, Tile('H', 1))
        self.assertEqual(scrabblecli.game.board.grid[7][8].letter, Tile('O', 1))
        self.assertEqual(scrabblecli.game.board.grid[7][9].letter, Tile('L', 1))
        self.assertEqual(scrabblecli.game.board.grid[7][10].letter, Tile('A', 1))
        self.assertEqual(scrabblecli.game.players[scrabblecli.game.current_player_index - 1].score, 4)

    @patch('builtins.input', side_effect=['play', 'hola', '7', '7', 'horizontal'])
    def test_word_double_points(self, mock_input):
        scrabblecli = ScrabbleCli()
        scrabblecli.game.players[scrabblecli.game.current_player_index].tiles = \
            [Tile('H', 1),
             Tile('O', 1),
             Tile('L', 1),
             Tile('A', 1)]
        scrabblecli.game.board.grid[7][7].set_multiplier_type("word")
        scrabblecli.game.board.grid[7][7].set_word_multiplier(2)
        scrabblecli.player_turn()
        self.assertEqual(scrabblecli.game.board.grid[7][7].letter, Tile('H', 1))
        self.assertEqual(scrabblecli.game.board.grid[7][8].letter, Tile('O', 1))
        self.assertEqual(scrabblecli.game.board.grid[7][9].letter, Tile('L', 1))
        self.assertEqual(scrabblecli.game.board.grid[7][10].letter, Tile('A', 1))
        self.assertEqual(len(scrabblecli.game.players[scrabblecli.game.current_player_index].tiles), 0)
        self.assertEqual(scrabblecli.game.players[scrabblecli.game.current_player_index - 1].score, 10)

    @patch('builtins.input', side_effect=['draw', '1'])
    def test_player_draw_cards(self, mock_input):
        scrabblecli = ScrabbleCli()
        scrabblecli.game.players[scrabblecli.game.current_player_index].tiles = \
            [Tile('P', 1),
             Tile('L', 1),
             Tile('A', 1),
             Tile('Y', 1)]
        scrabblecli.player_turn()
        self.assertEqual(len(scrabblecli.game.players[scrabblecli.game.current_player_index - 1].tiles), 5)

    @patch('builtins.input', side_effect=['pass'])
    def test_player_turn_pass(self, mock_input):
        scrabblecli = ScrabbleCli()
        scrabblecli.player_turn()
        self.assertEqual(scrabblecli.game.current_player_index, 1)

    @patch('builtins.input', side_effect=['pass'])
    def test_last_player_turn(self, mock_input):
        scrabblecli = ScrabbleCli()
        scrabblecli.game.current_player_index = 1
        scrabblecli.player_turn()
        self.assertEqual(scrabblecli.game.current_player_index, 0)

    def test_game_over(self):
        scrabblecli = ScrabbleCli()
        scrabblecli.end_game()
        self.assertEqual(scrabblecli.game_state, "over")

    def test_game_state_start(self):
        scrabblecli = ScrabbleCli()
        scrabblecli.game_state_start()
        self.assertEqual(scrabblecli.game_state, "ongoing")

    @patch('builtins.input', side_effect=['quit'])
    def test_start_game(self, mock_input):
        scrabblecli = ScrabbleCli()
        scrabblecli.start_game()
        self.assertEqual(scrabblecli.game_state, "over")

    def test_check_empty_tilebag(self):
        scrabblecli = ScrabbleCli()
        scrabblecli.game.tilebag.tiles = []
        scrabblecli.check_tiles()
        self.assertEqual(scrabblecli.game_state, "over")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_scores(self, mock_stdout):
        scrabblecli = ScrabbleCli()
        scrabblecli.game.players.pop(1)
        scrabblecli.game.players[0].set_name("Dino")
        scrabblecli.show_scores()
        self.assertEqual(mock_stdout.getvalue().strip(), "Score for Dino : 0")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['Dino', 'scores', 'quit'])
    def test_start_game(self, mock_input, mock_stdout):
        scrabblecli = ScrabbleCli()
        scrabblecli.game.players.pop(1)
        scrabblecli.game.players[0].set_name("Dino")
        scrabblecli.start_game()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Score for Dino : 0')
        self.assertEqual(scrabblecli.game_state, "over")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['Dino', 'tiles', 'quit'])
    def test_show_tiles(self, mock_input, mock_stdout):
        scrabblecli = ScrabbleCli()
        scrabblecli.game.players.pop(1)
        scrabblecli.game.players[0].set_name("Dino")
        scrabblecli.start_game()
        self.assertEqual(mock_stdout.getvalue().strip(), repr(scrabblecli.game.players[0].tiles))
        self.assertEqual(scrabblecli.game_state, "over")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['Dino', 'not an action', 'quit'])
    def test_action_not_valid(self, mock_input, mock_stdout):
        scrabblecli = ScrabbleCli()
        scrabblecli.game.players.pop(1)
        scrabblecli.game.players[0].set_name("Dino")
        scrabblecli.start_game()
        self.assertEqual(mock_stdout.getvalue().strip(), "Action not valid, please choose from: pass, play, draw, "
                                                         "quit, scores, tiles")
        self.assertEqual(scrabblecli.game_state, "over")

    # @patch('builtins.input', side_effect=['play', 'hola', '7', '7', 'horizontal'])
    # def test_first_turn(self, mock_input):
    #     scrabblecli = ScrabbleCli()
    #     scrabblecli.start_game()
    #     self.assertFalse(scrabblecli.game.board.grid[7][7].has_tile())

    # @patch('builtins.input', side_effect=['play', 'hola', '7', '7', 'horizontal'])
    # def test_first_turn(self):
    #     scrabblecli = ScrabbleCli()
    #     scrabblecli.game.players[scrabblecli.game.current_player_index].tiles = \
    #         [Tile('H', 1),
    #          Tile('O', 1),
    #          Tile('L', 1),
    #          Tile('A', 1)]
    #     scrabblecli.player_turn()
    #     self.assertEqual(scrabblecli.game.board.grid[7][7].letter, Square())
    #     self.assertEqual(scrabblecli.game.board.grid[7][8].letter, Square())
    #     self.assertEqual(scrabblecli.game.board.grid[7][9].letter, Square())
    #     self.assertEqual(scrabblecli.game.board.grid[7][10].letter, Square())
    #     self.assertEqual(scrabblecli.game.players[scrabblecli.game.current_player_index - 1].score, 4)

if __name__ == '__main__':
    unittest.main()
