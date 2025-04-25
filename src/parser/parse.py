import re
from enum import Enum
from typing import List
from parser.options import *

option_parser = OptionParser()
option_parser.optionParserLoadConfig(cli_options)

option_parser.printShortMap()

ind = option_parser.optionParserDoParse(["-c", "ass", "af"])
print(ind)
l = option_parser.optionParserGetResult()
for x in l:
    x.__str__()
