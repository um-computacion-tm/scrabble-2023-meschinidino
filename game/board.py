from game.square import Square


class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[Square() for _ in range(columns)] for _ in range(rows)]

    def place_tile(self, row, col, tile):
        if 0 <= row < self.rows and 0 <= col < self.columns:
            self.grid[row][col].insert_letter(tile)
