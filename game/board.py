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

    #TODO implement print board method
    # def print_row(self, row_number):
    #     squares = []
    #     for i in range(self.rows):
    #         squares.append(repr(self.grid[i][row_number]))
    #     return squares
    #
    # def print_board(self):
    #     columns = []
    #     for i in range(self.columns):
    #         columns.append(self.print_row(i))
    #     print(columns)