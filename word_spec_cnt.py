class word_spec_count():   
    def __init__(self, word_count):
        self.word_count = word_count

    def count(self, word):
        return self.word_count.words_dict[word.lower()]