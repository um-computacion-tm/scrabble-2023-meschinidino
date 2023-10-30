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
    return dictionary.has_word(word)


def is_board_empty(board):
    return not board.grid[7][7].has_tile()


def find_letter_in_word(word, letter):
    word = word
    for i in range(len(word)):
        if word[i] == letter.get_letter():
            word.pop(i)
            break
    return word


def sort_tiles_in_word_order(word, tiles):
    word = word.lower()  # Convert word to lowercase for case-insensitive matching
    tiles_dict = {tile.get_letter().lower(): tile for tile in tiles}
    sorted_tiles = [tiles_dict.get(letter, None) for letter in word]
    return sorted_tiles


def find_missing_letters(word, board):
    word_list = []
    if len(board) == 0:
        return ""
    for letter in word:
        word_list.append(letter.upper())
    for letter in board:
        checked_word = find_letter_in_word(word_list, letter)
    return "".join(checked_word)
