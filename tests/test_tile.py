import unittest
from game.tile import Tile


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

    def test_tile_repr(self):
        tile = Tile('A', 1)
        expected_repr = 'A:1'
        self.assertEqual(repr(tile), expected_repr)

    def test_eq_same_objects(self):
        tile = Tile('A', 1)
        self.assertTrue(tile == tile)

    def test_eq_different_objects(self):
        tile1 = Tile('A', 1)
        tile2 = Tile('A', 1)

        self.assertTrue(tile1 == tile2)
        self.assertTrue(tile2 == tile1)

    def test_neq_different_objects(self):
        tile1 = Tile('A', 1)
        tile2 = Tile('B', 2)

        self.assertTrue(tile1 != tile2)
        self.assertTrue(tile2 != tile1)

    def test_eq_invalid_comparison(self):
        tile = Tile('A', 1)
        other_object = 'Not a Tile object'

        self.assertFalse(tile == other_object)
        self.assertFalse(other_object == tile)

    def test_get_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, tile.get_letter())



if __name__ == '__main__':
    unittest.main()
