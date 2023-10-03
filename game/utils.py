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
        if word != "empty":
            score += word_score(word)
    return score
