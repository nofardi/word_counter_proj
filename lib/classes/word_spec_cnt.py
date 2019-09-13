"""
Holds the logic behind counting the occerance of a specific word
"""
class WordSpecCnt():   
    def __init__(self, word_count):
        self.word_count = word_count

    def count(self, word):
        return self.word_count.words_dict[word.lower()]