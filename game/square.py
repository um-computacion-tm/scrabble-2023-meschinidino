from game.tile import Tile


class Square:
    def __init__(self):
        self.multiplier = 1
        self.letter = None
        self.multiplier_type = None

    def has_letter(self):
        return self.letter is not None

    def has_multiplier(self):
        return self.multiplier > 1

    def get_multiplier_type(self):
        return self.multiplier_type

    def get_multiplier(self):
        return self.multiplier

    def get_letter(self):
        return self.letter

    def put_letter(self, letter):
        if not self.has_letter():
            self.letter = letter

    def set_multiplier_type(self, word):
        self.multiplier_type = word

    def set_multiplier(self, amount):
        self.multiplier = amount

    def set_letter(self, tile):
        self.letter = tile

