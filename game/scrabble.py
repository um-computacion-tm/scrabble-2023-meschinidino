from game.board import Board
from game.player import Player
from game.tilebag import Tilebag
from game.utils import *
from game.dictionary import Dictionary


class WordNotInDictionary(Exception):
    pass


class InvalidAction(Exception):
    pass


class WordNotThroughCenter(Exception):
    pass


class WordNotValid(Exception):
    pass


class ScrabbleGame:
    def __init__(self, amount):
        self.board = Board()
        self.tilebag = Tilebag()
        self.players = []
        self.current_player_index = 0
        self.game_state = None
        self.dictionary = Dictionary('dictionaries/dictionary.txt')
        for i in range(amount):
            self.players.append(Player())

    def change_player_index(self):
        if self.current_player_index == len(self.players) - 1:
            self.current_player_index = 0
        else:
            self.current_player_index += 1

    def get_scores(self):
        scores = {}
        for player in self.players:
            scores[player.get_name()] = player.get_score()
        return scores

    def play_word(self, word, row, column, direction):
        word = self.players[self.current_player_index].give_requested_tiles(word)
        self.board.place_word(word, row, column, direction)
        self.players[self.current_player_index].forfeit_tiles(word)
        self.players[self.current_player_index].increase_score(word_score(self.board.last_word))
        self.change_player_index()

    def pass_turn(self):
        self.change_player_index()

    def draw_tiles(self, amount):
        self.players[self.current_player_index].draw_tiles(self.tilebag, amount)
        self.change_player_index()

    def check_tiles(self):
        if len(self.tilebag.tiles) <= 0:
            self.end_game()

    def game_state_start(self):
        self.game_state = 'ongoing'

    def end_game(self):
        self.game_state = 'over'

    def start_player_tiles(self):
        for player in self.players:
            player.draw_tiles(self.tilebag, 7)

    def get_player_names(self):
        for i in range(len(self.players)):
            self.players[i].set_name(input(f"Player {i + 1} state your name: "))

    def validate_word(self, word, row, col, direction):
        validated_word = word
        if not check_word_dictionary(word):
            raise WordNotInDictionary
        if is_board_empty(self.board):
            if self.validate_word_through_center(word, row, col, direction):
                raise WordNotThroughCenter
        if self.letters_on_board(word, row, col, direction):
            validated_word = take_letters_from_word(word, self.find_letters_on_board(word, row, col, direction))
        return validated_word

    @staticmethod
    def validate_word_through_center(word, row, col, direction):
        board = Board()
        board.place_word(word, row, col, direction)
        return is_board_empty(board)

    def find_letters_on_board(self, word, row, col, direction):
        letters = []
        if direction == 'horizontal':
            for i in range(len(word)):
                tile = self.board.grid[row][col + i].get_tile()
                if tile is not None:
                    letters.append(tile)

        if direction == 'vertical':
            for i in range(len(word)):
                tile = self.board.grid[row + i][col].get_tile()
                if tile is not None:
                    letters.append(tile)
        return letters

    def letters_on_board(self, word, row, col, direction):
        tiles = self.find_letters_on_board(word, row, col, direction)
        return len(tiles) > 0
