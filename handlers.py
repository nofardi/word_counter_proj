from app_logic import AppLogic
import urllib
import re

class Handler(object):
    def __init__(self, cnt_obj):
        self.processed_input = []
        self.cnt_obj = cnt_obj
    
    def process_input_into_dict(self, input):
        input = re.sub(r'\s+', ' ', input) #remove duplicated spaces
        input = re.sub("[^a-zA-Z0-9]+", ' ', input) #remove all special characters and punctuations
        self.processed_input = input.lower().split()
        self.cnt_obj.update_dict_words(self.processed_input)

    def handle_outter_input(self, res_obj):
        for line in res_obj:
            self.process_input_into_dict(line)

class string_handler(Handler, AppLogic):
    def __init__(self, input, cnt_obj):
        super(string_handler, self).__init__(cnt_obj)
        super(string_handler, self).process_input_into_dict(input)

    def count_distinct_words(self):
        return super(string_handler, self).count_distinct_words()

    def count_occurance(self, word):
        return super(string_handler, self).count_word_occurance(word)
    
class url_handler(Handler, AppLogic):
    def __init__(self, input, cnt_obj):
        super(url_handler, self).__init__(cnt_obj)
        self.handle_url(input)
    
    def handle_url(self, input):
        try:
            response = urllib.urlopen(input)
            self.handle_outter_input(response)
        except urllib.error.HTTPError as e:
            print('Http error occured!', e.reason)

    def count_distinct_words(self):
        return super(url_handler, self).count_distinct_words()

    def count_occurance(self, word):
        return super(url_handler, self).count_word_occurance(word)


class file_handler(Handler, AppLogic):
    
    def __init__(self, input, cnt_obj):
        super(file_handler, self).__init__(cnt_obj)
        self.handle_file(input)

    def handle_file(self, input):
        with open(input, "r") as file_obj:
            self.handle_outter_input(file_obj)

    def count_distinct_words(self):
        return super(file_handler, self).count_distinct_words()

    def count_occurance(self, word):
        return super(file_handler, self).count_word_occurance(word)
        