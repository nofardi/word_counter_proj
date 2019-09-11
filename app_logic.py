import word_uniq_cnt
import word_spec_cnt
import urllib
import re

class AppLogic(object):
    def __init__(self, cnt_obj):
        self.processed_input = []
        self.cnt_obj = cnt_obj
    
    def process_input_into_dict(self, input):
        re.sub("[^a-zA-Z0-9]+", ' ', input) #remove all special characters and punctuations
        self.processed_input = input.lower().split()
        self.cnt_obj.update_dict_words(self.processed_input)

    def count_distinct_words(self):
        obj = word_uniq_cnt.word_uniq_count(self.cnt_obj)
        return obj.count()

    def count_word_occurance(self, word):
        obj = word_spec_cnt.word_spec_count(self.cnt_obj)
        return obj.count(word)

    def handle_big_input(self, res_obj):
        lines = res_obj.readlines()
        for line in lines:
            self.process_input_into_dict(line)

class string_handler(AppLogic):
    def __init__(self, input, cnt_obj):
        super(string_handler, self).__init__(cnt_obj)
        super(string_handler, self).process_input_into_dict(input)

    def count_distinct_words(self):
        return super(string_handler, self).count_distinct_words()

    def count_occurance(self, word):
        return super(string_handler, self).count_word_occurance(word)
    
class url_handler(AppLogic):
    def __init__(self, input, cnt_obj):
        super(url_handler, self).__init__(cnt_obj)
        self.handle_url(input)
    
    def handle_url(self, input):
        response = urllib.urlopen(input)
        self.handle_big_input(response)

    def count_distinct_words(self):
        return super(url_handler, self).count_distinct_words()

    def count_occurance(self, word):
        return super(url_handler, self).count_word_occurance(word)


class file_handler(AppLogic):
    
    def __init__(self, input, cnt_obj):
        super(file_handler, self).__init__(cnt_obj)
        self.handle_file(input)

    def handle_file(self, input):
        file_input = open(input, "r")
        self.handle_big_input(file_input)

    def count_distinct_words(self):
        return super(file_handler, self).count_distinct_words()

    def count_occurance(self, word):
        return super(file_handler, self).count_word_occurance(word)
        