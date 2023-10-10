from game.board import Board
from game.player import Player
from game.tilebag import Tilebag
from game.dictionary import Dictionary
from game.utils import *


class InvalidAction(Exception):
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

    def check_first_turn(self):
        return self.board.is_board_empty()

    def play_word(self):
        word = input("Give a word to enter: ").lower()
        row = int(input("State starting row: "))
        column = int(input("State starting column: "))
        direction = input("State direction (horizontal or vertical: )")
        word = self.players[self.current_player_index].give_requested_tiles(word)
        self.board.place_word(word, row, column, direction)
        self.players[self.current_player_index].forfeit_tiles(word)
        self.players[self.current_player_index].increase_score(word_score(self.board.last_word))
        self.change_player_index()

    def pass_turn(self):
        self.change_player_index()

    def draw_tiles(self):
        amount = int(input("How many tiles do you want to draw? "))
        self.players[self.current_player_index].draw_tiles(self.tilebag, amount)
        self.change_player_index()

    def check_tiles(self):
        if len(self.tilebag.tiles) <= 0:
            self.end_game()

    def show_scores(self):
        scores = self.get_scores()
        for element in scores:
            print("Score for", element, ":", scores[element])

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

    def show_tiles(self):
        tiles = self.players[self.current_player_index].show_tiles()
        print(tiles)

    # def first_turn(self):
    #     print("Since there is no word in the center, please place your word there to start the game")
    #     word = input("Give a word to enter: ").lower()
    #     row = int(input("State starting row: "))
    #     column = int(input("State starting column: "))
    #     direction = input("State direction (horizontal or vertical: )")
    #     word = self.players[self.current_player_index].give_requested_tiles(word)
    #     if not self.valid_first_word(word, row, column, direction):
    #         self.board.place_word(word, row, column, direction)
    #         self.players[self.current_player_index].forfeit_tiles(word)
    #         self.players[self.current_player_index].increase_score(word_score(self.last_word))
    #         self.change_player_index()

    def show_board(self):
        self.board.show_board()
    #
    # @staticmethod
    # def valid_first_word(word, starting_row, starting_column, direction):
    #     mock_board = Board()
    #     mock_board.place_word(word, starting_row, starting_column, direction)
    #     return mock_board.is_board_empty()

