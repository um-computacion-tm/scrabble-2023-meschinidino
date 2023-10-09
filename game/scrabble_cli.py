from game.scrabble import ScrabbleGame
from game.utils import *

PLAYERS = 2


class ScrabbleCli:
    def __init__(self):
        self.game = ScrabbleGame(PLAYERS)
        self.game_state = None
        self.VALID_ACTIONS = {
            'pass': self.game.pass_turn,
            'play': self.game.play_turn,
            'draw': self.game.draw_tiles,
            'quit': self.game.end_game,
            'scores': self.game.show_scores,
            'tiles': self.game.show_tiles,
            'board': self.game.show_board
        }

    def player_turn(self):
        action = input("What would you like to do? (play, pass, draw, scores, quit, tiles, board) ").lower()
        chosen_action = self.VALID_ACTIONS.get(action)
        if chosen_action:
            chosen_action()
        else:
            options = ', '.join(self.VALID_ACTIONS.keys())
            print(f"Action not valid, please choose from: {options}")

    def start_game(self):
        self.game.game_state_start()
        self.game.get_player_names()
        self.game.start_player_tiles()
        while True:
            if self.game.check_first_turn():
                self.game.first_turn()
                continue
            self.game.check_tiles()
            if self.game_state == 'over':
                break
            self.player_turn()
