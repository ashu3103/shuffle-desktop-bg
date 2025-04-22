from src.handlers.handler import *

class NullHandler(Handler):
    def __init__(self, *args, **kwargs):
        pass

    def close(self):
        pass

    def emit(self, record:str):
        pass