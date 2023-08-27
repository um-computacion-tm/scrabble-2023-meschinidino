from game.board import Board
from game.player import Player
from game.tilebag import Tilebag
from game.dictionary import Dictionary

class InvalidAction(Exception):
    pass


class ScrabbleGame:
    def __init__(self, amount):
        self.board = Board()
        self.tilebag = Tilebag()
        self.players = []
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


    # def prompt_for_action(self, action):
    #     if action == 'pass':
    #         return action
    #     if action == 'skip':
    #         return action
    #     if action == 'exchange':
    #         return action
    #     raise InvalidAction
    #
    # def player_insert_tiles(self, player: Player(), word: list, coordinates: list):
    #     for i in range(len(coordinates))
    #     self.board.place_tile()
    # def player_turn(self, action):
    #     while True:
    #         if action == 'pass':
    #             break
    #         if action == 'put':

