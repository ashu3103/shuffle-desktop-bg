from typing import List
from decorators.singleton import singleton

#
# Format of options stored
# option_flag_minor, option_flag_major (optional), is_required, is_flag
#
cli_options = [
    ["h", "help", False, True],
    ["V", "version", False, True],
    ["r", "repository", True, False],
    ["", "logfile", False, False],
    ["", "loglevel", False, False],
]

class OptionParameter:
    def __init__(self, is_req, is_flag):
        self.is_required = is_req
        self.is_flag = is_flag
        self.is_valid = False
        self.argument_value = None
        self.result_index = -1

    def __str__(self):
        if (not self.is_flag and self.is_valid):
            return f'({self.is_valid}, {self.is_required}, {self.is_flag}, {self.argument_value})'
        return f'({self.is_valid}, {self.is_required}, {self.is_flag})'

    def optionSetValid(self, valid: bool):
        self.is_valid = valid

    def optionGetValid(self):
        return self.is_valid
    
    def optionIsRequired(self) -> bool:
        return self.is_required

    def optionIsFlag(self) -> bool:
        return self.is_flag

    def optionSetArgumentValue(self, arg_val: str):
        self.argument_value = arg_val
    
    def optionGetArgumentValue(self) -> str:
        return self.argument_value

## Simple {key, value} pair
class OptionResult:
    def __init__(self, key: str, value: OptionParameter):
        self.key = key
        self.value = value
    def __str__(self):
        print(f'({self.key}, {self.value.__str__()})')


### Helper functions
def is_option(a: str) -> bool:
    if (a.startswith('-') or a.startswith('--')): return True
    return False

def extract_flag_arg(s: str) -> List:
    flag = None
    arg = None
    l = s.split('=')
    if (len(l) >= 2):
        arg = l[1]
    flag = l[0].split('--')[1]
    return [flag, arg]

## Ensure only one instance of this parser class in the project
@singleton
class OptionParser:
    __short_name_map = {}
    __long_name_map = {}

    __option_parameter_pool: List[OptionParameter] = []
    __result: List[OptionResult] = []

    def __init__(self):
        pass
        # self.logger = logger
    #
    # Initialize a parser with a set of config rules
    # Config rules have a defined format given below:
    # ( <short_name>, <long_name>, <is_required>, <is_flag> ), where <is_required> and <is_flag>
    # are mandatory, if <short_name>/<long_name> are not applicable use empty-strings (only)
    #
    def optionParserLoadConfig(self, options_config):
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
    # return the next index after parsing, -1 if unsuccess and maintain a result list for later 
    # use
    #
    def optionParserDoParse(self, options: List[str]) -> int:
        try:
            curr_index = 0
            ## Priority based results flag have higher priority than non-flags/argument options
            result_flag_index = 0
            result_non_flag_index = 0
            flag = ""
            while(curr_index < len(options)):
                option = options[curr_index]
                if (option.startswith('--')):
                    flag, argument = extract_flag_arg(options[curr_index])
                    if (self.__long_name_map.__contains__(flag)):
                        option_parameter: OptionParameter = self.__option_parameter_pool[self.__long_name_map[flag]]
                        if (option_parameter.optionGetValid()):  ## if already a flag was detected ignore it
                            print(f"duplicate option: --{flag}")
                            return -1
                        
                        if (not option_parameter.optionIsFlag()):
                            if not argument:
                                print(f"Argument is required for --{flag}")
                                return -1
                            option_parameter.optionSetArgumentValue(argument)
                        option_parameter.optionSetValid(True)
                    else:
                        print(f"--{flag} is not a valid option")
                        return -1
                elif (option.startswith('-')):
                    assert (len(option)==2)
                    flag = option[1]
                    if (self.__short_name_map.__contains__(flag)):
                        option_parameter: OptionParameter = self.__option_parameter_pool[self.__short_name_map[flag]]
                        if (option_parameter.optionGetValid()):  ## if already a flag was detected ignore it
                            print(f"duplicate option: -{flag}")
                            return -1
                        
                        if (not option_parameter.optionIsFlag()):
                            curr_index = curr_index + 1
                            if (curr_index >= len(options) or is_option(options[curr_index])):
                                print(f"Argument is required for -{flag}")
                                return -1
                            option_parameter.optionSetArgumentValue(options[curr_index])
                        option_parameter.optionSetValid(True)
                    else:
                        print(f"-{flag} is not a valid option")
                        return -1
                ## base case
                else:
                    break

                ## Populate result
                if (option_parameter.optionIsFlag()):
                    self.__result.insert(result_flag_index, OptionResult(flag, option_parameter))
                    result_flag_index = result_flag_index + 1
                    result_non_flag_index = result_non_flag_index + 1
                else:
                    self.__result.append(OptionResult(flag, option_parameter))
                    result_non_flag_index = result_non_flag_index + 1
                curr_index = curr_index + 1

            for op in self.__option_parameter_pool:
                if (op.is_required and not op.is_valid):
                    print(f'Some flags are required but not present')
                    return -1
            return curr_index
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            return -1
    
    ## For development purpose only TODO: Remove it ###################################################
    def printShortMap(self):
        for key, value in self.__short_name_map.items():
            print(f'Key: {key}, Value: {self.__option_parameter_pool[value].__str__()}')
    
    def printLongMap(self):
        for key, value in self.__long_name_map.items():
            print(f'Key: {key}, Value: {self.__option_parameter_pool[value].__str__()}')
    ###################################################################################################

    def optionParserGetResult(self) -> List[OptionResult]:
        return self.__result
        





    
