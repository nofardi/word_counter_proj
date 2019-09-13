from app_logic import AppLogic
import urllib
import re

"""
General class for handling the input given.
Holds the array of the current proccessed input and the counter object that 
keeps the results perssistent.
"""
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

"""
Specific class for handling a string input 
"""
class StringHandler(Handler, AppLogic):
    def __init__(self, input, cnt_obj):
        super(StringHandler, self).__init__(cnt_obj)
        super(StringHandler, self).process_input_into_dict(input)

    def count_distinct_words(self):
        return super(StringHandler, self).count_distinct_words()

    def count_word_occurance(self, word):
        return super(StringHandler, self).count_word_occurance(word)


"""
Specific class for handling a url input 
"""
class UrlHandler(Handler, AppLogic):
    def __init__(self, input, cnt_obj):
        super(UrlHandler, self).__init__(cnt_obj)
        self._handle_url(input)
    
    def _handle_url(self, input):
        try:
            response = urllib.urlopen(input)
            self.handle_outter_input(response)
        except urllib.error.HTTPError as e:
            print('Http error occured!', e.reason)

    def count_distinct_words(self):
        return super(UrlHandler, self).count_distinct_words()

    def count_word_occurance(self, word):
        return super(UrlHandler, self).count_word_occurance(word)


"""
Specific class for handling a file input 
"""
class FileHandler(Handler, AppLogic):
    def __init__(self, input, cnt_obj):
        super(FileHandler, self).__init__(cnt_obj)
        self._handle_file(input)

    def _handle_file(self, input):
        with open(input, "r") as file_obj:
            self.handle_outter_input(file_obj)

    def count_distinct_words(self):
        return super(FileHandler, self).count_distinct_words()

    def count_word_occurance(self, word):
        return super(FileHandler, self).count_word_occurance(word)
        