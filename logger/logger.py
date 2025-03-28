from enum import Enum
from handlers.null import *
from handlers.file import *
from handlers.stream import *
from handlers.handler import *

class LogLevel(Enum):
    INFO = 1
    WARNING = 2
    ERROR = 3
    DEBUG = 4


def defaultFormat(logLevel: LogLevel, message:str) -> str:

    pass

class Logger:
    def __init__(self, level):
        self.format = defaultFormat
        self.level = level

    def setLevel(self, level: LogLevel):
        self.level = level

    def setFormat(self, formatCallback):
        self.format = formatCallback

    def NullHandler(self) -> NullHandler:
        return NullHandler()

    def FileHandler(self, filename: str, mode: chr='a') -> FileHandler:
        return FileHandler(filename=filename, mode=mode)

    def StreamHandler(self) -> StreamHandler:
        return StreamHandler()

    def addHandler(self, handler: Handler):
        if self.handler:
            self.handler.close()
        self.handler = handler
    
    def removeHandler(self):
        if self.handler:
            self.handler.close()
            self.handler = None

    def shutdown(self):
        self.removeHandler()

    def log(self, level: LogLevel, message: str):
        try:
            if not self.handler:
                raise Exception("No handler registered")
            if level.value >= self.level.value:
                self.handler.emit(self.format(level, message))
        except Exception as e:
            print(e)
    
    # wrappers
    def info(self, message):
        self.log(LogLevel.INFO, message)
    
    def warning(self, message):
        self.log(LogLevel.WARNING, message)
    
    def error(self, message):
        self.log(LogLevel.ERROR, message)
    
    def debug(self, message):
        self.log(LogLevel.DEBUG, message)




