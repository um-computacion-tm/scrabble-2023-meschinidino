from tile import Tile
import random


class BagTiles:
    def __init__(self):
        self.tiles = [
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
        ]
        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self, tiles):
        self.tiles.extend(tiles)
