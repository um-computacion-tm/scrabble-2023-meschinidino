from game.square import Square

COLUMNS = 15
ROWS = 15


class PlacementOutOfBounds(Exception):
    pass


class Board:
    def __init__(self):
        self.rows = ROWS
        self.columns = COLUMNS
        self.grid = [[Square() for _ in range(self.columns)] for _ in range(self.rows)]

    def place_tile(self, row, column, tile):
        if not (0 <= row < self.rows and 0 <= column < self.columns):
            raise PlacementOutOfBounds("Placement is outside the valid boundaries.")
        self.grid[row][column].set_tile(tile)

    def get_square(self, row, column):
        return self.grid[row][column]

    def get_tile(self, row, column):
        return self.grid[row][column].get_tile()