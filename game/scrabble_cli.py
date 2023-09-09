from game.scrabble import ScrabbleGame

PLAYERS = 2


class ScrabbleCli:
    def __init__(self):
        self.game = ScrabbleGame(PLAYERS)

    def player_turn(self, action):
        if action == 'pass':
            self.pass_turn()
        if action == 'play':
            self.play_turn()
        if action == 'draw':
            self.draw_tiles()

    def play_turn(self):
        word = input("Give a word to enter: ").lower()
        row = int(input("State starting row: "))
        column = int(input("State starting column: "))
        direction = input("State direction (horizontal or vertical: )")
        word = self.game.players[self.game.current_player_index].give_requested_tiles(word)
        self.game.place_word(word, row, column, direction)
        self.game.players[self.game.current_player_index].forfeit_tiles(word)
        self.game.players[self.game.current_player_index].increase_score(self.game.word_score(self.game.last_word))
        self.game.change_player_index()

    def pass_turn(self):
        self.game.change_player_index()

    def draw_tiles(self):
        amount = int(input("How many tiles do you want to draw? "))
        self.game.players[self.game.current_player_index].draw_tiles(self.game.tilebag, amount)
        self.game.change_player_index()
