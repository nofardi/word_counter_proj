from input_factory import InputFactory
from word_count import WordCount
import sys

PRIMARY_INPUT_MSG = "Please enter any of the following input:\nFree text, file path or a link URL:\n(Press CTRL + C to terminate)\n"
SECOND_PROGRAM_INPUT_MSG = "Enter the word you want us to count\n"

def app():
    cnt_obj = WordCount()
    try:
        while True:
            user_input = raw_input(PRIMARY_INPUT_MSG)
            input_obj = InputFactory().factory(user_input, cnt_obj)
            print(input_obj.count_distinct_words())
            word_as_input = raw_input(SECOND_PROGRAM_INPUT_MSG)
            print(input_obj.count_occurance(word_as_input))
    except KeyboardInterrupt:
        sys.exit(0)

app()