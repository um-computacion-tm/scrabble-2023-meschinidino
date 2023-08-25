import unittest
from unittest.mock import patch
from game.tile import Tile
from game.tilebag import Tilebag, LETTERS, CantidadDeFichasSuperaTotal


class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = Tilebag()
        self.assertEqual(
            len(bag.tiles),
            sum(quantity for _, (_, quantity) in LETTERS.items()),  # Calculate the total quantity
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.tiles,
        )

    def test_take(self):
        bag = Tilebag()
        initial_tile_count = len(bag.tiles)
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),
            initial_tile_count - 2,
        )
        self.assertEqual(
            len(tiles),
            2,
        )

    def test_put(self):
        bag = Tilebag()
        initial_tile_count = len(bag.tiles)
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            initial_tile_count + len(put_tiles),
        )

    def test_take_too_many(self):
        bag = Tilebag()
        with self.assertRaises(CantidadDeFichasSuperaTotal):
            bag.take(1000000000)


if __name__ == '__main__':
    unittest.main()
