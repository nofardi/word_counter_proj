from collections import Counter

class WordCount():
    def __init__(self):
        self.res = 0
        self.words_dict = Counter([])
    
    def update_dict_words(self, words):
        temp_dict = Counter(words)
        dict.update(self.words_dict, temp_dict)