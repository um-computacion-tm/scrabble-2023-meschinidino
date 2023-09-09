class Tile:
    def __init__(self, letter=None, value=None):
        self.letter = letter
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.letter == other.letter and self.value == other.value
        return False

    def __repr__(self):
        return f"Tile(letter='{self.letter}', value={self.value})"

    def get_value(self):
        return self.value

    def get_letter(self):
        return self.letter
