from enum import Enum
from typing import List
from parser.options import *
from parser.commands import *
from logger.logger import *
from handlers import *

## Pass a copy of sys
def parse(input: List[str], option_config=cli_options, command_config=cli_commands):
    ## Parse options first
    option_parser = OptionParser()
    option_parser.optionParserLoadConfig(option_config)

    ind = option_parser.optionParserDoParse(input)
    if (ind == -1):
        return [None, None]
    input = input[ind:]

    ## Parse command
    command_parser = CommandParser()
    command_parser.commandParserLoadConfig(command_config)
    ind = command_parser.commandParserDoParse(input)
    if (ind == -1):
        return [None, None]

    return [option_parser.optionParserGetResult(), command_parser.commandParserGetResult()]
