import unittest
from io import StringIO
from unittest.mock import patch

from game.player import Player, LetterNotFound
from game.tilebag import Tilebag
from game.tile import Tile


class TestPlayer(unittest.TestCase):
    def test_player(self):
        player = Player()
        self.assertEqual(player.score, 0)
        self.assertEqual(len(player.tiles), 0)

    def test_player_score(self):
        player = Player()
        player.increase_score(2)
        self.assertEqual(player.score, 2)

    def test_player_score_many(self):
        player = Player()
        player.increase_score(2)
        player.increase_score(2)
        self.assertEqual(player.score, 4)

    def test_player_draw(self):
        player = Player()
        bag = Tilebag()
        player.draw_tiles(bag, 2)
        self.assertEqual(len(player.tiles), 2)

    def test_player_exchange(self):
        player = Player()
        bag = Tilebag()
        player.draw_tiles(bag, 2)
        tile = player.tiles[0]
        player.exchange_tile(player.tiles[0], bag)
        self.assertFalse(tile == player.tiles[0])

    def test_find_letter_in_tiles(self):
        player = Player()
        player.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 1)]
        result = player.find_letter_in_tiles('B')
        self.assertIsInstance(result, Tile)
        self.assertEqual(result.get_letter(), 'B')
        result = player.find_letter_in_tiles('X')
        self.assertFalse(result)

    def test_give_requested_tiles(self):
        player = Player()
        player.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 1)]
        word = 'ABC'
        result = player.give_requested_tiles(word)
        self.assertEqual(len(result), len(word))

    @patch('sys.stdout', new_callable=StringIO)
    def test_give_tiles_empty(self, mock_stdout):
        player = Player()
        player.give_requested_tiles("word")
        self.assertEqual(mock_stdout.getvalue().strip(), "Letter 'w' not found in player's tiles")

    def test_forfeit_tile(self):
        player = Player()
        player.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 1)]
        player.forfeit_tile(Tile('A', 1))
        self.assertEqual([Tile('B', 3), Tile('C', 1)], player.tiles)

    def test_forfeit_tiles(self):
        player = Player()
        player.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 1)]
        player.forfeit_tiles([Tile('B', 3), Tile('C', 1)])
        self.assertEqual(player.tiles, [Tile('A', 1)])

    def test_set_name(self):
        player = Player()
        player.set_name('Dino')
        self.assertEqual(player.get_name(), 'Dino')

    def test_get_score(self):
        player = Player()
        player.increase_score(2)
        self.assertEqual(player.get_score(), 2)

    def test_show_tiles(self):
        player = Player()
        self.assertEqual(player.show_tiles(), player.tiles)



if __name__ == '__main__':
    unittest.main()
