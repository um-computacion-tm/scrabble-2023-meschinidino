from game.square import Square

COLUMNS = 15
ROWS = 15
TRIPLE_WORD_SCORE = ((0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14))
DOUBLE_WORD_SCORE = ((1, 1), (2, 2), (3, 3), (4, 4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3),
                     (10, 4), (13, 13),(12, 12), (11, 11), (10, 10))
TRIPLE_LETTER_SCORE = ((1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5),
                       (13, 9))
DOUBLE_LETTER_SCORE = ((0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12),
                       (7, 3), (7, 11), (8, 2),(8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8),
                       (14, 3), (14, 11))

class PlacementOutOfBounds(Exception):
    pass


class Board:
    def __init__(self):
        self.rows = ROWS
        self.columns = COLUMNS
        self.grid = [[Square() for _ in range(self.columns)] for _ in range(self.rows)]
        self.add_premium_squares()

    def add_premium_squares(self):
        for coordinate in TRIPLE_WORD_SCORE:
            self.grid[coordinate[0]][coordinate[1]].multiplier_type = "word"
            self.grid[coordinate[0]][coordinate[1]].multiplier = 3
        for coordinate in TRIPLE_LETTER_SCORE:
            self.grid[coordinate[0]][coordinate[1]].multiplier_type = "letter"
            self.grid[coordinate[0]][coordinate[1]].multiplier = 3
        for coordinate in DOUBLE_WORD_SCORE:
            self.grid[coordinate[0]][coordinate[1]].multiplier_type = "word"
            self.grid[coordinate[0]][coordinate[1]].multiplier = 2
        for coordinate in DOUBLE_LETTER_SCORE:
            self.grid[coordinate[0]][coordinate[1]].multiplier_type = "letter"
            self.grid[coordinate[0]][coordinate[1]].multiplier = 2

    def place_tile(self, row, column, tile):
        if not (0 <= row < self.rows and 0 <= column < self.columns):
            raise PlacementOutOfBounds("Placement is outside the valid boundaries.")
        self.grid[row][column].set_tile(tile)

    def get_square(self, row, column):
        return self.grid[row][column]

    def get_tile(self, row, column):
        return self.grid[row][column].get_tile()

    def print_row(self, row_number):
        squares = []
        for i in range(self.rows):
            squares.append(repr(self.grid[i][row_number]))
        return squares

    def is_board_empty(self):
        return not self.grid[7][7].has_tile()

    # def print_board(self):
    #     columns = []
    #     for i in range(self.columns):
    #         columns.append(self.print_row(i))
    # for i in range(len(columns)):
    #         if len(str(i))==1:
    #             print("0" + str(i), columns[i])
    #             print("--------------------------------------------------------------------------------"
    #                   "--------------------------------------------------------------------------------"
    #                   "-------------------------------------")
    #         else:
    #             print(i+1, columns[i])
    #             print("--------------------------------------------------------------------------------"
    #                   "--------------------------------------------------------------------------------"
    #                   "-------------------------------------")
