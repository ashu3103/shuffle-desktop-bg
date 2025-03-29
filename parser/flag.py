import re

FLAG_EXPRESSION_PATTERN = r"^-"

class FlagEntity:
    def __init__(self, flag: str, argument: str):
        self.flag = flag
        self.argument = argument

    def getFlag(self):
        return self.flag
    
    def getArgument(self):
        return self.argument

    