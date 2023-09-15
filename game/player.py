from game.tilebag import Tilebag


class LetterNotFound(Exception):
    pass


class Player:
    def __init__(self):
        self.score = 0
        self.tiles = []
        self.name = ""

    def increase_score(self, amount):
        self.score += amount

    def draw_tiles(self, bag: Tilebag, amount):
        self.tiles.extend(bag.take(amount))

    def exchange_tile(self, tile, bag: Tilebag):
        for i in range(len(self.tiles)):
            if self.tiles[i] == tile:
                popped = self.tiles.pop(i)
                bag.put([popped])
                break

        self.tiles.extend(bag.take(1))

    def find_letter_in_tiles(self, letter):
        for tile in self.tiles:
            if tile.get_letter() == letter.upper():
                return tile
        return None

    def give_requested_tiles(self, word):
        letters = []
        for letter in word:
            tile = self.find_letter_in_tiles(letter)
            if tile is not None:
                letters.append(tile)
            else:
                raise LetterNotFound(f"Letter '{letter}' not found in player's tiles")
        return letters

    def forfeit_tiles(self, word):
        for tile in word:
            self.forfeit_tile(tile)

    def forfeit_tile(self, tile):
        for i in range(len(self.tiles)):
            if self.tiles[i].get_letter() == tile.get_letter():
                self.tiles.pop(i)
                break

    def set_name(self, name):
        self.name = name

    def get_score(self):
        return self.score

    def get_name(self):
        return self.name

    def show_tiles(self):
        return self.tiles
