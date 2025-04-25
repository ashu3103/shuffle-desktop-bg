from enum import Enum
import datetime
from handlers.null import *
from handlers.file import *
from handlers.stream import *
from handlers.handler import *
from decorators.singleton import *

class LogLevel(Enum):
    INFO = 1
    WARNING = 2
    ERROR = 3
    DEBUG = 4

def defaultStreamFormat(logLevel: LogLevel, message:str) -> str:
    LOG_COLORS = {
        LogLevel.INFO: "\033[32m",
        LogLevel.WARNING: "\033[33m",
        LogLevel.ERROR: "\033[31m",
        LogLevel.DEBUG: "\033[34m"
    }

    timeNow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    levelColor = LOG_COLORS.get(logLevel, "\033[0m")
    return f'{timeNow}  {levelColor}{logLevel.name}\033[0m  {message}'

def defaultFileFormat(logLevel: LogLevel, message:str) -> str:
    timeNow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f'{timeNow}  {logLevel.name}  {message}'

@singleton
class Logger:
    # Default log level is info
    def __init__(self, level=LogLevel.INFO):
        self.format = defaultStreamFormat
        self.level = level
        self._handler = None

    def setLevel(self, level: LogLevel):
        self.level = level

    def getLevel(self) -> LogLevel:
        return self.level

    def setFormat(self, formatCallback):
        self.format = formatCallback

    def NullHandler(self) -> NullHandler:
        return NullHandler()

    def FileHandler(self, filename: str, mode: chr='a') -> FileHandler:
        return FileHandler(filename=filename, mode=mode)

    def StreamHandler(self, flush:bool=False) -> StreamHandler:
        return StreamHandler(flush)

    def addHandler(self, handler: Handler):
        if self._handler:
            self._handler.close()
        self._handler = handler
    
    def removeHandler(self):
        if self._handler:
            self._handler.close()
            self._handler = None

    def shutdown(self):
        self.removeHandler()

    def log(self, level: LogLevel, message: str):
        try:
            if not self._handler:
                raise Exception("No handler registered")
            if level.value <= self.level.value:
                self._handler.emit(self.format(level, message))
        except Exception as e:
            print(e)
    
    # wrappers
    def info(self, message: str):
        self.log(LogLevel.INFO, message)
    
    def warning(self, message: str):
        self.log(LogLevel.WARNING, message)
    
    def error(self, message: str):
        self.log(LogLevel.ERROR, message)
    
    def debug(self, message: str):
        self.log(LogLevel.DEBUG, message)
