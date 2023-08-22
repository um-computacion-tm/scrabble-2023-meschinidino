from game.tile import Tile


class Square:
    def __init__(self, multiplier: int = 1, letter: Tile = None):
        self.multiplier = multiplier
        self.letter = letter

    def has_letter(self):
        return self.letter is not None

    def has_multiplier(self):
        return self.multiplier > 1

    def insert_letter(self, letter):
        if not self.has_letter():
            self.letter = letter
