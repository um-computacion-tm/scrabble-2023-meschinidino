from game.board import Board
from game.player import Player
from game.tilebag import Tilebag
from game.dictionary import Dictionary


class InvalidAction(Exception):
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

    def word_score(self, word: list):
        score = 0
        word_multipliers = 0
        for square in word:
            if square.word_multiplier is not None:
                word_multipliers += square.word_multiplier
                square.multiplier_is_up()
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

    def place_vertical(self, word, starting_row, starting_column):
        if starting_row + len(word) > 15:
            raise WordOutOfBounds
        for i in range(len(word)):
            if self.board.get_square(starting_row + i, starting_column).has_tile():
                continue
            self.board.place_tile(i + starting_row, starting_column, word[i])
            self.last_word.append(self.board.grid[starting_row + i][starting_column])
