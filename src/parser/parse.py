import re
from enum import Enum
from typing import List
from parser.options import *

option_parser = OptionParser()
option_parser.optionParserLoadConfig(cli_options)

# option_parser.printShortMap()
option_parser.printLongMap()

ind = option_parser.optionParserDoParse(["--config=lk", "-h", "-c", "af"])
print(ind)
l = option_parser.optionParserGetResult()
for x in l:
    x.__str__()
