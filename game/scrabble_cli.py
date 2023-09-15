from game.scrabble import ScrabbleGame

PLAYERS = 2


class ScrabbleCli:
    def __init__(self):
        self.game = ScrabbleGame(PLAYERS)
        self.game_state = None
        self.VALID_ACTIONS = {
            'pass': self.pass_turn,
            'play': self.play_turn,
            'draw': self.draw_tiles,
            'quit': self.end_game,
            'scores': self.show_scores,
            'tiles': self.show_tiles,
        }

    def player_turn(self):
        action = input("What would you like to do? (play, pass, draw, scores, quit, tiles) ").lower()
        chosen_action = self.VALID_ACTIONS.get(action)
        if chosen_action:
            chosen_action()
        else:
            options = ', '.join(self.VALID_ACTIONS.keys())
            print(f"Action not valid, please choose from: {options}")

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
        self.get_player_names()
        self.start_player_tiles()
        while True:
            if self.game.check_first_turn():
                self.first_turn()
                continue
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

    def start_player_tiles(self):
        for player in self.game.players:
            player.draw_tiles(self.game.tilebag, 7)

    def get_player_names(self):
        for i in range(len(self.game.players)):
            self.game.players[i].set_name(input(f"Player {i + 1} state your name: "))

    def show_tiles(self):
        tiles = self.game.players[self.game.current_player_index].show_tiles()
        print(tiles)

    def first_turn(self):
        print("Since there is no word in the center, please place your word there to start the game")
        word = input("Give a word to enter: ").lower()
        row = int(input("State starting row: "))
        column = int(input("State starting column: "))
        direction = input("State direction (horizontal or vertical: )")
        word = self.game.players[self.game.current_player_index].give_requested_tiles(word)
        if not self.valid_first_word(word, row, column, direction):
            self.game.place_word(word, row, column, direction)
            self.game.players[self.game.current_player_index].forfeit_tiles(word)
            self.game.players[self.game.current_player_index].increase_score(self.game.word_score(self.game.last_word))
            self.game.change_player_index()

    @staticmethod
    def valid_first_word(word, starting_row, starting_column, direction):
        mock_game = ScrabbleGame(1)
        mock_game.place_word(word, starting_row, starting_column, direction)
        return mock_game.board.is_board_empty()
