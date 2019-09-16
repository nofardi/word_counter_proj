from collections import Counter
import json
import os

"""
Class that manages the result counter and the dictionary used thoughout the execution.
To maintain a persist result between runs the class implements a serializer and deserializer 
"""
class WordCount():
    def __init__(self):
        self.res = 0
        self.deserialize()
    
    def update_dict_words(self, words):
        temp_dict = Counter(words)
        self.words_dict.update(temp_dict)

    def serialize(self):
        curr_dir = os.getcwd()
        with open(curr_dir + '/dictJson.txt', 'w') as jsonFile:
            json.dump(self.words_dict, jsonFile)

    def deserialize(self):
        curr_dir = os.getcwd()
        try: 
            with open(curr_dir + '/dictJson.txt') as jsonFile:
                self.words_dict = Counter(json.load(jsonFile))
        except IOError:  #first run - files does not exist
            self.words_dict = Counter([])