from word_dictionaries import WordDictionaries

class Gameboard:

    def __init__(self):
        self._create_grid()

    def get_grid(self):
        return self.grid

    def _create_grid(self):
        words = WordDictionaries.get_words(WordDictionaries.get_classic_dictionary())

        self.grid = []
        temp_grid = []

        counter = 0
        for word in words:
            temp_grid.append(word)
            counter += 1

            if counter % 5 == 0:
                self.grid.append(temp_grid)
                temp_grid = []
