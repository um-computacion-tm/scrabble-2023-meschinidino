from game.square import Square


class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[Square() for _ in range(columns)] for _ in range(rows)]

    def place_tile(self, row, col, tile):
        if 0 <= row < self.rows and 0 <= col < self.columns:
            self.grid[row][col].set_letter(tile)

    def word_score(self, word: list):
        score = 0
        word_multipliers = 0
        for square in word:
            if square.word_multiplier is not None:
                word_multipliers += square.word_multiplier
                square.multiplier_is_up()
            score += square.individual_score()
        if word_multipliers != 0:
            return score * word_multipliers
        return score

    def get_tile(self, row, column):
        return self.grid[row][column]