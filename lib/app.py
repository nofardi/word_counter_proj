from classes.input_factory import InputFactory
from classes.word_count import WordCount
import sys
from enum import Enum

PRIMARY_INPUT_MSG = "Please enter any of the following input:\nFree text, file path or a link URL:\n(Press CTRL + C to terminate)\n"
SECOND_PROGRAM_INPUT_MSG = "Enter the word you want us to count\n"
FIRST_RESULT_MSG = "\nNumber of distinct words in the given input: "
SECOND_RESULT_MSG = "\nNumber of occurances of the given word in the given input: "

class AppModeEnum(Enum):
    UNIQ_CNT = "1"
    SPEC_CNT = "2"


"""
Main function of the executable
"""
def app():
    cnt_obj = WordCount()
    input_mode = sys.argv[1]

    if AppModeEnum(input_mode) == AppModeEnum.UNIQ_CNT:
        input_obj = process_input(sys.argv[2:], False, cnt_obj)
        print(FIRST_RESULT_MSG + str(input_obj.count_distinct_words()) + "\n")
    elif AppModeEnum(input_mode) == AppModeEnum.SPEC_CNT:
        input_obj = process_input(sys.argv[2:], True, cnt_obj)
        word_as_input = sys.argv[-1]
        print(SECOND_RESULT_MSG + str(input_obj.count_word_occurance(word_as_input)) + "\n")
    
    cnt_obj.serialize()
    
def process_input(user_input, should_ignore_last_val, cnt_obj):

    if should_ignore_last_val == True:
        user_input = " ".join(user_input[:-1])
    else:
        user_input = " ".join(user_input)
    
    try:
        input_obj = InputFactory().create_input_obj(user_input, cnt_obj)
        return input_obj
    except ValueError as v:
        print(v.args[0])
        sys.exit(1)
    except IOError as e:
        print(e.strerror)
        sys.exit(1)
    

app()