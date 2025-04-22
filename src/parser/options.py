import re
from typing import List
from src.decorators.singleton import singleton

FLAG_EXPRESSION_PATTERN = r"^-"

#
# Format of options stored
# option_flag_minor, option_flag_major (optional), is_required, argumental option
#
cli_options = [
    ["h", "help", False, False],
    ["V", "version", False, False],
    ["", "logfile", False, True],
    ["", "log-level", False, True]
]

class OptionParameter:
    def __init__(self, is_req, is_flag):
        self.is_required = is_req
        self.is_flag = is_flag
        self.is_valid = False
        self.argument_value = None
    
    def optionSetValid(self, valid: bool):
        self.is_valid = valid
    
    def optionIsRequired(self) -> bool:
        return self.is_required

    def optionIsFlag(self) -> bool:
        return self.is_flag

    def optionSetArgumentValue(self, arg_val: str):
        self.argument_value = arg_val
    
    def optionGetArgumentValue(self) -> str:
        return self.argument_value

## Ensure only one instance of this parser class in the project
@singleton
class OptionParser:
    __short_name_map = {}
    __long_name_map = {}

    __option_parameter_pool = []

    #
    # Initialize a parser with a set of config rules
    #
    def parser_init(self, options_config):
        try:
            for i in range(len(options_config)):
                assert isinstance(options_config[i], list)
                assert (len(options_config[i]) == 4)
                assert (isinstance(options_config[i][0], str))
                assert (isinstance(options_config[i][1], str))
                assert (isinstance(options_config[i][2], bool))
                assert (isinstance(options_config[i][3], bool))

                short_name = options_config[i][0]
                long_name = options_config[i][1]
                is_req = options_config[i][2]
                is_flag = options_config[i][3]

                self.__option_parameter_pool.append(OptionParameter(is_req, is_flag))

                if (short_name != ""):
                    self.__short_name_map[short_name] = len(self.__option_parameter_pool) - 1
                if (long_name != ""):
                    self.__long_name_map[long_name] = len(self.__option_parameter_pool) - 1
        except AssertionError as e:
            print(f"Assertion failed: {e}")

    #
    # Parse the options of a command line, flags have more priority than argument options
    # return the next index after parsing, -1 if unsuccess
    #
    def parse_options(options: List[str]) -> int:
        next_index = 0
        for i, option in enumerate(options):
            if (option.startswith('-')):
                
                pass
            elif (option.startswith('--')):
                pass
            ## base case
            else:
                break
            next_index = i

        return next_index
        





    
