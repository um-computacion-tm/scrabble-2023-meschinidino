import unittest
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


if __name__ == '__main__':
    unittest.main()
