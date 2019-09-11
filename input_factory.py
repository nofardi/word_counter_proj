import app_logic
from enum import Enum
import re

REGEX_STRING = "[A-Z|a-z]\\w*"
REGEX_FILE = "^\/([A-z0-9-_+]+\/)*([A-z0-9]+\.(txt))$"
REGEX_URL = "https*://.*"
INVALID_TYPE_ERROR = "Input isn't supported"

class InputEnum(Enum):
    STRING = 1
    FILE = 2
    URL = 3
    OTHER = 4

class InputFactory:
    def factory(self, user_input, cnt_obj):
        self.cnt_obj = cnt_obj
        input_obj = self.get_input_obj(user_input)
        return input_obj

    def get_input_obj(self, user_input):
        input_type = self.get_input_type(user_input)
        if input_type == InputEnum.STRING:
            return app_logic.string_handler(user_input, self.cnt_obj)
        elif input_type == InputEnum.FILE:
            return app_logic.file_handler(user_input, self.cnt_obj)
        elif input_type == InputEnum.URL:
            return app_logic.url_handler(user_input, self.cnt_obj)
        else: # unsupported input
            raise ValueError(INVALID_TYPE_ERROR)

    def get_input_type(self, user_input):
        string_pattern = re.compile(REGEX_STRING)
        file_pattern = re.compile(REGEX_FILE)
        url_pattern = re.compile(REGEX_URL)
        if url_pattern.match(user_input):
            return InputEnum.URL
        elif file_pattern.match(user_input):
            return InputEnum.FILE
        elif string_pattern.match(user_input):
            return InputEnum.STRING
        else:
            return InputEnum.OTHER