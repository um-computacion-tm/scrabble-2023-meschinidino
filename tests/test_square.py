import unittest

from game.square import Square
from game.tile import Tile


class TestSquare(unittest.TestCase):
    def test_empty_square(self):
        square = Square()
        self.assertEqual(square.letter_multiplier, 1)
        self.assertEqual(square.letter, None)

    def test_square_letter(self):
        tile = Tile('A', 1)
        square = Square()
        square.put_tile(tile)
        self.assertEqual(square.letter, tile)

    def test_square_multiplier(self):
        square = Square()
        square.set_multiplier(2)
        self.assertEqual(square.get_multiplier(), 2)

    def test_no_multiplier(self):
        square = Square()
        self.assertFalse(square.has_multiplier())

    def test_has_multiplier(self):
        square = Square()
        square.set_multiplier(2)
        self.assertTrue(square.has_multiplier())

    def test_no_letter(self):
        square = Square()
        self.assertFalse(square.has_tile())

    def test_has_letter(self):
        square = Square()
        square.put_tile(Tile('A', 1))
        self.assertTrue(square.has_tile())

    def test_insert_letter_full(self):
        square = Square()
        square.set_tile(Tile('A', 1))
        square.put_tile(Tile('B', 1))
        self.assertEqual(square.get_tile(), Tile('A', 1))

    def test_insert_letter_empty(self):
        square = Square()
        square.put_tile((Tile('A', 1)))
        self.assertEqual(square.letter.letter, 'A')

    def test_multiplier_type(self):
        square = Square()
        square.set_multiplier_type('word')
        self.assertEqual(square.get_multiplier_type(), 'word')

    def test_multiplier_type_2(self):
        square = Square()
        square.set_multiplier_type('letter')
        self.assertEqual(square.get_multiplier_type(), 'letter')

    def test_score_tile_empty(self):
        square = Square()
        self.assertEqual(square.individual_score(), 0)

    def test_give_info(self):
        square = Square()
        square.put_tile(Tile('A', 1))
        square.set_multiplier_type('Letter')
        square.set_multiplier(2)
        self.assertEqual((repr(square)), 'A, 1, x2 Letter')

    def test_give_info_empty(self):
        square = Square()
        self.assertEqual((repr(square)), "|  | 0 | x1|")


if __name__ == '__main__':
    unittest.main()
