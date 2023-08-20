import unittest

from game.tile import Tile
from game.tilebag import Tilebag, LETTERS
from game.square import Square
from unittest.mock import patch
from game.dictionary import Dictionary


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)


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


class TestSquare(unittest.TestCase):
    def test_empty_square(self):
        square = Square()
        self.assertEqual(square.multiplier, None)
        self.assertEqual(square.letter, None)

    def test_square_letter(self):
        tile = Tile('A', 1)
        square = Square(letter=tile)
        self.assertEqual(square.letter, tile)

    def test_square_multiplier(self):
        square = Square(multiplier=2)
        self.assertEqual(square.multiplier, 2)

    def test_no_multiplier(self):
        square = Square()
        self.assertFalse(square.has_multiplier())

    def test_has_multiplier(self):
        square = Square(multiplier=2)
        self.assertTrue(square.has_multiplier())

    def test_no_letter(self):
        square = Square()
        self.assertFalse(square.has_multiplier())

    def test_has_letter(self):
        square = Square(letter=Tile('A', 1))
        self.assertTrue(square.has_letter())


class TestDictionary(unittest.TestCase):
    def test_dictionary(self):
        dictionary = Dictionary('game/dictionary.txt')
        self.assertTrue(dictionary.has_word('arbol'))

    def test_word_false(self):
        dictionary = Dictionary('game/dictionary.txt')
        self.assertFalse(dictionary.has_word('willkommen'))


if __name__ == '__main__':
    unittest.main()
