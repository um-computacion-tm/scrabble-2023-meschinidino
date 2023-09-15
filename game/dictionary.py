class Dictionary:
    def __init__(self, file_path):
        self.words = self.load_words(file_path)

    @staticmethod
    def load_words(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return set(word.strip() for word in file)

    def has_word(self, word):
        return word in self.words
