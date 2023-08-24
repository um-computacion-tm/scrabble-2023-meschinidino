from game.board import Board
from game.player import Player
from game.tilebag import Tilebag


class ScrabbleGame:
    def __init__(self, amount):
        self.board = Board(15, 15)
        self.tilebag = Tilebag()
        self.players = []
        for i in range(amount):
            self.players.append(Player())

