from classes.input_factory import InputFactory
from classes.word_count import WordCount
import sys

PRIMARY_INPUT_MSG = "Please enter any of the following input:\nFree text, file path or a link URL:\n(Press CTRL + C to terminate)\n"
SECOND_PROGRAM_INPUT_MSG = "Enter the word you want us to count\n"
FIRST_RESULT_MSG = "\nNumber of distinct words in the given input: "
SECOND_RESULT_MSG = "\nNumber of occurances of the given word in the given input: "

"""
Main function of the executable
"""
def app():
    cnt_obj = WordCount()
    try:
        while True:
            try:
                user_input = raw_input(PRIMARY_INPUT_MSG)
                input_obj = InputFactory().create_input_obj(user_input, cnt_obj)
            except ValueError as v:
                print(v.args[0])
                continue
            except IOError as e:
                print(e.strerror)
                continue
            print(FIRST_RESULT_MSG + str(input_obj.count_distinct_words()) + "\n")
            word_as_input = raw_input(SECOND_PROGRAM_INPUT_MSG)
            print(SECOND_RESULT_MSG + str(input_obj.count_word_occurance(word_as_input)) + "\n")
    except KeyboardInterrupt:
        sys.exit(0)

app()