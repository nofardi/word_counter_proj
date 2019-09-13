from word_uniq_cnt import WordUniqCnt
from word_spec_cnt import WordSpecCnt

"""
This class holds the calls to the available logic objects
"""
class AppLogic(object):
    def __init__(self, cnt_obj):
        self.cnt_obj = cnt_obj

    def count_distinct_words(self):
        obj = WordUniqCnt(self.cnt_obj)
        return obj.count()

    def count_word_occurance(self, word):
        obj = WordSpecCnt(self.cnt_obj)
        return obj.count(word)
