import unittest
import classes.handlers as handlers
from classes.word_count import WordCount
from classes.input_factory import InputFactory
import os

class TestCounterMethods(unittest.TestCase):

    def test_count_string(self):
        remove_results_file()
        cnt_obj = WordCount()
        self.assertEqual(handlers.StringHandler("Hi! My name is (what?), my name is (who?), my name is Slim Shady", cnt_obj).count_distinct_words(), 5)
        cnt_obj = WordCount()
        self.assertEqual(handlers.StringHandler("Hi! My name is (what?), my name is (who?), my name is Slim Shady", cnt_obj).count_word_occurance("my"), 3)
    
    def test_count_file(self):
        remove_results_file()
        cnt_obj = WordCount()
        curr_dir = os.getcwd()
        self.assertEqual(handlers.FileHandler(curr_dir + "/tests/sample.txt", cnt_obj).count_distinct_words(), 319)
        cnt_obj = WordCount()
        self.assertEqual(handlers.FileHandler(curr_dir + "/tests/sample.txt", cnt_obj).count_word_occurance("sample"), 7)
    
    def test_count_url(self):
        remove_results_file()
        cnt_obj = WordCount()
        self.assertEqual(handlers.UrlHandler("http://txt2html.sourceforge.net/sample.txt", cnt_obj).count_distinct_words(), 319)
        cnt_obj = WordCount()
        self.assertEqual(handlers.UrlHandler("http://txt2html.sourceforge.net/sample.txt", cnt_obj).count_word_occurance("sample"), 7)

class TestInputMethods(unittest.TestCase):

    def test_string_input(self):
        cnt_obj = WordCount()
        self.assertIsInstance(InputFactory().create_input_obj("bla bla", cnt_obj), handlers.StringHandler)
        self.assertIsInstance(InputFactory().create_input_obj("Hi! My name is (what?), my name is (who?), my name is Slim Shady", cnt_obj), handlers.StringHandler)
        
    def test_file_input(self):
        cnt_obj = WordCount()
        curr_dir = os.getcwd()
        self.assertIsInstance(InputFactory().create_input_obj(curr_dir + "/tests/sample.txt", cnt_obj), handlers.FileHandler)
 
    def test_url_input(self):
        cnt_obj = WordCount()
        self.assertIsInstance(InputFactory().create_input_obj("http://txt2html.sourceforge.net/sample.txt", cnt_obj), handlers.UrlHandler)
 
class TestPersistResults(unittest.TestCase):
    def test_persist_results(self):
        remove_results_file()
        cnt_obj = WordCount()
        self.assertEqual(handlers.UrlHandler("http://txt2html.sourceforge.net/sample.txt", cnt_obj).count_distinct_words(), 319)
        cnt_obj.serialize()
        cnt_obj.deserialize()
        self.assertEqual(handlers.UrlHandler("http://txt2html.sourceforge.net/sample.txt", cnt_obj).count_distinct_words(), 0)
        cnt_obj.serialize()
        cnt_obj.deserialize()
        self.assertEqual(handlers.StringHandler("sample", cnt_obj).count_word_occurance("sample"), 15)

def remove_results_file():
    filename = os.getcwd() + '/dictJson.txt'
    try:
        os.remove(filename)
    except OSError:
        pass


suite_counter = unittest.TestLoader().loadTestsFromTestCase(TestCounterMethods)
suite_input = unittest.TestLoader().loadTestsFromTestCase(TestInputMethods)
suite_persist = unittest.TestLoader().loadTestsFromTestCase(TestPersistResults)
unittest.TextTestRunner(verbosity=2).run(suite_counter)
unittest.TextTestRunner(verbosity=2).run(suite_input)
unittest.TextTestRunner(verbosity=2).run(suite_persist)