from game.scrabble import ScrabbleGame

PLAYERS = 2


class ScrabbleCli:
    def __init__(self):
        self.game = ScrabbleGame(PLAYERS)
        self.game_state = None

    def player_turn(self):
        action = input("What would you like to do? (play, pass, draw, scores, quit) ").lower()
        if action == 'pass':
            self.pass_turn()
        if action == 'play':
            self.play_turn()
        if action == 'draw':
            self.draw_tiles()
        if action == 'quit':
            self.game_state = 'over'
        if action == 'scores':
            self.show_scores()
        elif action != 'pass' and action != 'play' and action != 'draw' and action != 'quit':
            print("Action not valid, please choose play, pass or draw.")

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

    def start_game(self):
        self.game_state_start()
        while True:
            self.check_tiles()
            if self.game_state == 'over':
                break
            self.player_turn()

    def check_tiles(self):
        if len(self.game.tilebag.tiles) <= 0:
            self.end_game()

    def show_scores(self):
        scores = self.game.get_scores()
        for element in scores:
            print("Score for", element, ":", scores[element])

    def game_state_start(self):
        self.game_state = 'ongoing'

    def end_game(self):
        self.game_state = 'over'
