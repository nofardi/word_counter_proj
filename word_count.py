from collections import Counter

"""
Class that manages the result counter and the dictionary used thoughout the execution
"""
class WordCount():
    def __init__(self):
        self.res = 0
        self.words_dict = Counter([])
    
    def update_dict_words(self, words):
        temp_dict = Counter(words)
        self.words_dict.update(temp_dict)