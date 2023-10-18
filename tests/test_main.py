import unittest
from unittest.mock import patch
from game.scrabble_cli import ScrabbleCli
from game.main import main


class TestMain(unittest.TestCase):
    @patch.object(ScrabbleCli, 'start_game')
    def test_main(self, *args):
        main()


if __name__ == '__main__':
    unittest.main()
