from game.tilebag import Tilebag


class Player:
    def __init__(self):
        self.score = 0
        self.tiles = []

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
