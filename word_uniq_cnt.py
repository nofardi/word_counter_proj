class word_uniq_count():
    def __init__(self, words_count):
        self.words_count = words_count
        
    def count(self):
        for word in self.words_count.words_dict:
            if self.words_count.words_dict[word] == 1:
                self.words_count.res += 1
        
        return self.words_count.res
             