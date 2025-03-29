from .handler import *
import sys

class StreamHandler(Handler):
    def __init__(self, flsh:bool=False) -> Exception:
        self.flsh = flsh

    def flush(self):
        sys.stdout.flush()

    def close(self):
        self.flush()

    def emit(self, record: str):
        print(f'{record}', flush=self.flsh)
