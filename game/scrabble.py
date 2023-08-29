import game.board
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
        if word_multipliers != 0:
            return score * word_multipliers
        return score
    # WORK IN PROGRESS
    # def player_turn(self):
    #     pass
    #WORK IN PROGRESS

    def place_word(self, word, starting_row, starting_column, direction):
        if direction.lower() == 'horizontal':
            if starting_column + len(word) > 15:
                raise WordOutOfBounds
            for i in range(len(word)):
                self.board.place_tile(starting_row, i + starting_column, word[i])
        if direction.lower() == 'vertical':
            if starting_row + len(word) > 15:
                raise WordOutOfBounds
            for i in range(len(word)):
                self.board.place_tile(i + starting_row, starting_column, word[i])
