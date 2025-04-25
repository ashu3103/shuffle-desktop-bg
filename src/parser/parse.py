import re
from enum import Enum
from typing import List
from parser.options import *

option_parser = OptionParser()
option_parser.optionParserLoadConfig(cli_options)

option_parser.printShortMap()
option_parser.printLongMap()
