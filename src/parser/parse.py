import re
from enum import Enum
from typing import List
from parser.options import *
from parser.commands import *
from logger.logger import *
from handlers import *

cmd_list = ["-h", "-V", "--logfile=asd", "command"]

logger = Logger(level=LogLevel.DEBUG)
logger.addHandler(logger.StreamHandler())

# option_parser = OptionParser(logger)
# option_parser.optionParserLoadConfig(cli_options)

# # option_parser.printShortMap()
# option_parser.printLongMap()

# ind = option_parser.optionParserDoParse(cmd_list)
# print(ind)
# l = option_parser.optionParserGetResult()
# for x in l:
#     x.__str__()