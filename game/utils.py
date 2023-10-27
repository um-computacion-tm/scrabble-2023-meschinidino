from game.dictionary import Dictionary

dictionary = Dictionary("dictionaries/dictionary.txt")


def word_score(word: list):
    score = 0
    word_multipliers = 0
    for square in word:
        if square.multiplier_type == 'word':
            word_multipliers += square.multiplier
        score += square.individual_score()
        square.multiplier_is_up()
    if word_multipliers != 0:
        return score * word_multipliers
    return score


def list_word_score(words):
    score = 0
    for word in words:
        score += get_score_tiles(word)
    return score


def get_score_tiles(word):
    score = 0
    for letter in word:
        score += letter.get_value()
    return score


def check_word_dictionary(word):
    check = ""
    for letter in word:
        check += letter.get_letter()
    return dictionary.has_word(check.lower())


def is_board_empty(board):
    return not board.grid[7][7].has_tile()
