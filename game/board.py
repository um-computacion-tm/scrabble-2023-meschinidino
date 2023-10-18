from game.square import Square
from game.utils import check_word_dictionary

COLUMNS = 15
ROWS = 15
TRIPLE_WORD_SCORE = ((0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14))
DOUBLE_WORD_SCORE = ((1, 1), (2, 2), (3, 3), (4, 4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3),
                     (10, 4), (13, 13), (12, 12), (11, 11), (10, 10))
TRIPLE_LETTER_SCORE = ((1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5),
                       (13, 9))
DOUBLE_LETTER_SCORE = ((0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12),
                       (7, 3), (7, 11), (8, 2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8),
                       (14, 3), (14, 11))


class PlacementOutOfBounds(Exception):
    pass


class WordNotValid(Exception):
    pass


class WordOutOfBounds(Exception):
    pass


class Board:
    def __init__(self):
        self.rows = ROWS
        self.columns = COLUMNS
        self.grid = [[Square(
        ) for _ in range(self.columns)] for _ in range(self.rows)]
        self.add_premium_squares()
        self.last_word = []

    def add_premium_squares(self):
        for coordinate in TRIPLE_WORD_SCORE:
            self.set_square_multiplier(coordinate, "word", 3)

        for coordinate in DOUBLE_WORD_SCORE:
            self.set_square_multiplier(coordinate, "word", 2)

        for coordinate in TRIPLE_LETTER_SCORE:
            self.set_square_multiplier(coordinate, "letter", 3)

        for coordinate in DOUBLE_LETTER_SCORE:
            self.set_square_multiplier(coordinate, "letter", 2)

    def set_square_multiplier(self, coordinate, multiplier_type, multiplier_value):
        square = self.grid[coordinate[0]][coordinate[1]]
        square.multiplier_type = multiplier_type
        square.multiplier = multiplier_value

    def place_tile(self, row, column, tile):
        if not (0 <= row < self.rows and 0 <= column < self.columns):
            raise PlacementOutOfBounds("Placement is outside the valid boundaries.")
        self.grid[row][column].set_tile(tile)

    def get_square(self, row, column):
        return self.grid[row][column]

    def get_tile(self, row, column):
        return self.grid[row][column].get_tile()

    def place_word(self, word, starting_row, starting_column, direction):
        self.last_word = []
        if word is None:
            raise WordNotValid
        if not check_word_dictionary(word):
            raise WordNotValid
        if direction.lower() == 'horizontal':
            self.place_horizontal(word, starting_row, starting_column)
        if direction.lower() == 'vertical':
            self.place_vertical(word, starting_row, starting_column)

    def place_horizontal(self, word, starting_row, starting_column):
        intercepted = []
        if starting_column + len(word) > 15:
            raise WordOutOfBounds
        for i in range(len(word)):
            if self.get_square(starting_row, i + starting_column).has_tile():
                continue
            self.place_tile(starting_row, i + starting_column, word[i])
            word_found = (self.check_word_vertical(starting_row, i + starting_column))
            intercepted.extend(word_found)
            self.last_word.append(self.grid[starting_row][starting_column + i])

    def place_vertical(self, word, starting_row, starting_column):
        if starting_row + len(word) > 15:
            raise WordOutOfBounds
        for i in range(len(word)):
            if self.get_square(starting_row + i, starting_column).has_tile():
                continue
            self.place_tile(i + starting_row, starting_column, word[i])
            self.last_word.append(self.grid[starting_row + i][starting_column])

    def check_left_square(self, row, col):
        return self.grid[row - 1][col].has_tile()

    def check_right_square(self, row, col):
        return self.grid[row + 1][col].has_tile()

    def check_up_square(self, row, col):
        return self.grid[row][col - 1].has_tile()

    def check_down_square(self, row, col):
        return self.grid[row][col + 1].has_tile()

    def check_word_horizontal(self, row, col):
        left = self.check_word_left(row, col)
        right = self.check_word_right(row, col)
        left.extend(right)
        if len(left) == 0:
            return ["empty"]
        return left

    def check_word_vertical(self, row, col):
        up = self.check_word_up(row, col)
        down = self.check_word_down(row, col)
        up.extend(down)
        if len(up) == 0:
            return ["empty"]
        return up

    def check_word_left(self, row, col):
        word = []
        while row >= 0 and self.check_left_square(row + 1, col):
            word.insert(0, self.grid[row][col].get_tile())
            row -= 1
        return word

    def check_word_right(self, row, col):
        word = []
        while row >= 0 and self.check_right_square(row, col):
            word.insert(0, self.grid[row + 1][col].get_tile())
            row += 1
        return word

    def check_word_up(self, row, col):
        word = []
        while col >= 0 and self.check_up_square(row, col + 1):
            word.insert(0, self.grid[row][col].get_tile())
            col -= 1
        return word

    def check_word_down(self, row, col):
        word = []
        while col >= 0 and self.check_down_square(row, col):
            word.insert(0, self.grid[row][col + 1].get_tile())
            col += 1
        return word
