from typing import List
from enum import Enum
from decorators.singleton import singleton
from logger.logger import *

class CommandAction(Enum):
    ADD_IMAGE = 1
    LIST_IMAGE = 2
    DELETE_IMAGE = 3
    SHUFFLE = 4

class CommandResult:
    def __init__(self, action: CommandAction, args: List[str]):
        self.action = action
        self.args = args
    
    def __str__(self):
        return f"({self.action}, ({self.args}))"

class CommandEntity:
    def __init__(self, command_name: str, number_of_args: List[int], action: CommandAction, log_message: str):
        self.command_name = command_name
        self.number_of_args = number_of_args
        self.number_of_args.sort()
        self.action = action
        self.log_msg = log_message
    def __str__(self):
        return f"({self.command_name}, ({self.number_of_args}), {self.action})"


cli_commands = [
    CommandEntity("add_image", [1], CommandAction.ADD_IMAGE, ""),
    CommandEntity("list_images", [0], CommandAction.LIST_IMAGE, ""),
    CommandEntity("delete_image", [1], CommandAction.DELETE_IMAGE, "")
]

@singleton
class CommandParser:
    __parsed_command: CommandResult = None

    def __init__(self):
        pass
        # self.logger = logger

    def commandParserLoadConfig(self, config: List[CommandEntity]):
        self.config = config
    
    def commandParserDoParse(self, input: List[str]) -> int:
        curr_index = 0
        args = []
        if (len(input) == 0):
            print(f"No command speified")
            return -1
        command = input[curr_index]
        curr_index = curr_index + 1

        entity: CommandEntity = None
        for c in self.config:
            if (command == c.command_name):
                entity = c
                break
            
        if (not entity):
            print(f"{command} is not a valid command")
            return -1
        
        while curr_index < len(input):
            args.append(input[curr_index])
            curr_index = curr_index + 1

        if len(args) > entity.number_of_args[len(entity.number_of_args) - 1]:
            print(f"{command}: Too many arguments provided")
            return -1
        
        if (len(args) < entity.number_of_args[0]):
            print(f"{command}: Too less arguments provided")
            return -1

        self.__parsed_command = CommandResult(entity.action, args)

    
    def commandParserGetResult(self) -> CommandResult:
        return self.__parsed_command