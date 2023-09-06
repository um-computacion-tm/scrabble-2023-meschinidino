import unittest
from unittest.mock import patch
from game.scrabble_cli import ScrabbleCli
from game.tile import Tile



class MyTestCase(unittest.TestCase):

    @patch('builtins.input', side_effect=['play', '7', '7', 'horizontal'])
    def test_turn_word(self, mock_input):
        scrabblecli = ScrabbleCli()
        scrabblecli.game.players[scrabblecli.game.current_player_index].tiles = \
            [Tile('P', 1),
             Tile('L', 1),
             Tile('A', 1),
             Tile('Y', 1)]
        scrabblecli.player_turn('play')
        self.assertEqual(scrabblecli.game.board.grid[7][7].letter, Tile('P', 1))
        self.assertEqual(scrabblecli.game.board.grid[7][8].letter, Tile('L', 1))
        self.assertEqual(scrabblecli.game.board.grid[7][9].letter, Tile('A', 1))
        self.assertEqual(scrabblecli.game.board.grid[7][10].letter, Tile('Y', 1))
        # self.assertEqual(scrabblecli.game.players[scrabblecli.game.current_player_index].score, 5)

    def test_player_turn_pass(self):
        scrabblecli = ScrabbleCli()
        scrabblecli.player_turn('pass')
        self.assertEqual(scrabblecli.game.current_player_index, 1)

    def test_last_player_turn(self):
        scrabblecli = ScrabbleCli()
        scrabblecli.game.current_player_index = 1
        scrabblecli.player_turn('pass')
        self.assertEqual(scrabblecli.game.current_player_index, 0)


if __name__ == '__main__':
    unittest.main()
