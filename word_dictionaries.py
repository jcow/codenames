


class WordDictionaries:

    FILEPATH_CLASSIC_WORD_LIST = "dictionaries/classic_word_list.txt"

    classic_dictionary = set()
    naughty_dictionary = set()

    @staticmethod
    def get_classic_dictionary():
        return WordDictionaries.classic_dictionary

    @staticmethod
    def initialize():
        with open(WordDictionaries.FILEPATH_CLASSIC_WORD_LIST) as f:
            for line in f:
                line = line.strip()
                WordDictionaries.classic_dictionary.add(line)

    @staticmethod
    def get_classic_dictionary():
        return WordDictionaries.classic_dictionary
