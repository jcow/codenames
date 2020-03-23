import random


class WordDictionaries:

    FILEPATH_CLASSIC_WORD_LIST = "dictionaries/classic_word_list.txt"

    classic_dictionary = []
    naughty_dictionary = []

    @staticmethod
    def get_words(dictionary, number_of_words=25):
        word_set = set()
        while len(word_set) < 25:
            word = random.choice(dictionary)
            if word not in word_set:
                word_set.add(word)

        return list(word_set)

    @staticmethod
    def get_classic_dictionary():
        return WordDictionaries.classic_dictionary

    @staticmethod
    def initialize():
        dictionary = set()
        with open(WordDictionaries.FILEPATH_CLASSIC_WORD_LIST) as f:
            for line in f:
                line = line.strip()
                dictionary.add(line)

        WordDictionaries.classic_dictionary = list(dictionary)

    @staticmethod
    def get_classic_dictionary():
        return WordDictionaries.classic_dictionary
