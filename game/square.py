from game.tile import Tile


class Square:
    def __init__(self, multiplier: int = None, letter: Tile = None):
        self.multiplier = multiplier
        self.letter = letter

    def has_letter(self):
        return self.letter is not None

    def has_multiplier(self):
        return self.multiplier is not None