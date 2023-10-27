from game.scrabble import ScrabbleGame
from game.utils import *

PLAYERS = 2


class ActionNotValid(Exception):
    pass


class ScrabbleCli:
    def __init__(self):
        self.game = ScrabbleGame(PLAYERS)
        self.VALID_ACTIONS = {
            'pass': self.game.pass_turn,
            'word': self.play_word,
            'draw': self.game.draw_tiles,
            'quit': self.game.end_game,
            'scores': self.show_scores,
            'tiles': self.show_tiles,
            'board': self.show_board
        }

    def player_turn(self):
        action = input("What would you like to do? (word, pass, draw, scores, quit, tiles, board) ").lower()
        chosen_action = self.VALID_ACTIONS.get(action)
        if chosen_action:
            chosen_action()
        else:
            options = ', '.join(self.VALID_ACTIONS.keys())
            raise ActionNotValid(f"Action not valid, please choose from: {options}")

    def start_game(self):
        self.game.game_state_start()
        self.game.get_player_names()
        self.game.start_player_tiles()
        while True:
            try:
                self.game.check_tiles()
                if self.game.game_state == 'over':
                    break
                self.player_turn()
            except Exception as e:
                print(e)

    def show_scores(self):
        scores = self.game.get_scores()
        for element in scores:
            print(f"Score for {element}: {scores[element]}")

    def show_board(self):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(self.game.board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(square) for square in row])
            )

    def show_tiles(self):
        tiles = self.game.players[self.game.current_player_index].show_tiles()
        print(tiles)

    def play_word(self):
        word = input("Give a word to enter: ").lower()
        row = int(input("State starting row: "))
        column = int(input("State starting column: "))
        direction = input("State direction (horizontal or vertical: )")
        self.game.play_word(word, row, column, direction)

    def draw_tiles(self):
        amount = int(input("How many tiles do you want to draw? "))
        self.game.draw_tiles(amount)
