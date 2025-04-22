import re
from enum import Enum
from typing import List
from src.parser.options import *

class Action(Enum):
    NOOP: 0

class CommandEntity:
    command = None
    acceptedArgCount = [0]
    action = Action.NOOP

def usage():
    print("Usage")
    

def version():
    print("Version")
    

def parser(log, cmd: str) -> List[FlagEntity]:
    ## Get flags (support for single dash '-')
    cmdIndex = 0
    ## The first index is the commad itself (skip)
    log.debug(f'parsing the command: {cmd[cmdIndex]}')

    flagList = []
    commandList = []

    cmdIndex = cmdIndex + 1
    while (re.match(FLAG_EXPRESSION_PATTERN, cmd[cmdIndex])):
        currentFlag = cmd[cmdIndex]
        if currentFlag == "-?":
            usage()
            exit(1)
        elif currentFlag == "-v":
            version()
            exit(0)
        elif currentFlag == "-L":
            cmdIndex = cmdIndex + 1
            flagList.append(FlagEntity(currentFlag, cmd[cmdIndex]))
        else:
            usage()
            exit(1)
        cmdIndex = cmdIndex + 1

    ## Get command
    pass