from game.board import Board
from game.player import Player
from game.tilebag import Tilebag
from game.dictionary import Dictionary


class InvalidAction(Exception):
    pass


class WordNotValid(Exception):
    pass


class WordOutOfBounds(Exception):
    pass


class ScrabbleGame:
    def __init__(self, amount):
        self.board = Board()
        self.tilebag = Tilebag()
        self.players = []
        self.current_player_index = 0
        self.dictionary = Dictionary('dictionaries/dictionary.txt')
        self.last_word = []
        for i in range(amount):
            self.players.append(Player())

    @staticmethod
    def word_score(word: list):
        score = 0
        word_multipliers = 0
        for square in word:
            if square.multiplier_type == 'word':
                word_multipliers += square.multiplier
            score += square.individual_score()
            square.multiplier_is_up()
        if word_multipliers != 0:
            return score * word_multipliers
        return score

    def change_player_index(self):
        if self.current_player_index == len(self.players) - 1:
            self.current_player_index = 0
        else:
            self.current_player_index += 1

    def place_word(self, word, starting_row, starting_column, direction):
        self.last_word = []
        if word is None:
            print(InvalidAction)
        if not self.check_word_validity(word):
            raise WordNotValid
        if direction.lower() == 'horizontal':
            self.place_horizontal(word, starting_row, starting_column)
        if direction.lower() == 'vertical':
            self.place_vertical(word, starting_row, starting_column)

    def place_horizontal(self, word, starting_row, starting_column):
        if starting_column + len(word) > 15:
            raise WordOutOfBounds
        for i in range(len(word)):
            if self.board.get_square(starting_row, i + starting_column).has_tile():
                continue
            self.board.place_tile(starting_row, i + starting_column, word[i])
            self.last_word.append(self.board.grid[starting_row][starting_column + i])

    def place_vertical(self, word, starting_row, starting_column):
        if starting_row + len(word) > 15:
            raise WordOutOfBounds
        for i in range(len(word)):
            if self.board.get_square(starting_row + i, starting_column).has_tile():
                continue
            self.board.place_tile(i + starting_row, starting_column, word[i])
            self.last_word.append(self.board.grid[starting_row + i][starting_column])

    def get_scores(self):
        scores = {}
        for player in self.players:
            scores[player.get_name()] = player.get_score()
        return scores

    def check_word_validity(self, word):
        check = ""
        for letter in word:
            check += letter.get_letter()
        return self.dictionary.has_word(check.lower())

    def check_first_turn(self):
        return self.board.is_board_empty()

    def check_left_square(self, row, col):
        return self.board.grid[row - 1][col].has_tile()

    def check_right_square(self, row, col):
        return self.board.grid[row + 1][col].has_tile()

    def check_up_square(self, row, col):
        return self.board.grid[row][col - 1].has_tile()

    def check_down_square(self, row, col):
        return self.board.grid[row][col + 1].has_tile()

    def check_word_left(self, row, col):
        word = []
        while col >= 0 and self.board.grid[row][col].has_tile():
            word.insert(0, self.board.grid[row][col].get_tile())
            col -= 1
        return len(word) > 0

    def check_word_right(self, row, col):
        word = []
        while col >= 0 and self.board.grid[row][col].has_tile():
            word.insert(0, self.board.grid[row][col].get_tile())
            col += 1
        return len(word) > 0

    def check_word_up(self, row, col):
        word = []
        while row >= 0 and self.board.grid[row][col].has_tile():
            word.insert(0, self.board.grid[row][col].get_tile())
            row -= 1
        return len(word) > 0

    def check_word_down(self, row, col):
        word = []
        while row >= 0 and self.board.grid[row][col].has_tile():
            word.insert(0, self.board.grid[row][col].get_tile())
            row += 1
        return len(word) > 0
