import unittest
from unittest.mock import patch
from game.scrabble_cli import ScrabbleCli
from game.square import Square
from game.tile import Tile
from io import StringIO


class MyTestCase(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['hola', '7', '7', 'horizontal', 'quit'])
    def test_player_turn_play_word(self, mock_input, mock_stdout):
        cli = ScrabbleCli()
        cli.game.players[cli.game.current_player_index].tiles = \
            [Tile('H', 1),
             Tile('O', 1),
             Tile('L', 1),
             Tile('A', 1)]
        cli.play_word()
        self.assertTrue(cli.game.board.grid[7][7].has_tile())
        self.assertEqual(cli.game.board.grid[7][7].letter, Tile('H', 1))

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['word', 'hola', '7', '7', 'horizontal'])
    def test_player_turn_player_turn(self, mock_input, mock_stdout):
        cli = ScrabbleCli()
        cli.game.players[cli.game.current_player_index].tiles = \
            [Tile('H', 1),
             Tile('O', 1),
             Tile('L', 1),
             Tile('A', 1)]
        cli.player_turn()
        self.assertTrue(cli.game.board.grid[7][7].has_tile())
        self.assertEqual(cli.game.board.grid[7][7].letter, Tile('H', 1))

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['quit'])
    def test_player_turn_end(self, mock_input, mock_stdout):
        cli = ScrabbleCli()
        cli.player_turn()
        self.assertTrue(cli.game.game_state, "over")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['Dino', 'A', 'wordssssss', 'quit'])
    def test_player_turn_exception(self, mock_input, mock_stdout):
        cli = ScrabbleCli()
        cli.game.players[cli.game.current_player_index].tiles = \
            [Tile('H', 1),
             Tile('O', 1),
             Tile('L', 1),
             Tile('A', 1)]
        cli.start_game()
        self.assertEqual(mock_stdout.getvalue().strip(), "Action not valid, please choose from: pass, word, draw, "
                                                                 "quit, scores, tiles, board")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_player_scores(self, mock_stdout):
        cli = ScrabbleCli()
        cli.show_scores()

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_player_board(self, mock_stdout):
        cli = ScrabbleCli()
        cli.show_board()

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_player_tiles(self, mock_stdout):
        cli = ScrabbleCli()
        cli.show_tiles()

    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_show_player_draw_tiles(self, mock_input, mock_stdout):
        cli = ScrabbleCli()
        cli.draw_tiles()

    @patch('builtins.input', side_effect=['Dino', 'Vin', 'quit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_start_game(self, mock_input, mock_stdout):
        cli = ScrabbleCli()
        cli.start_game()
        self.assertEqual(cli.game.game_state, "over")



if __name__ == '__main__':
    unittest.main()
