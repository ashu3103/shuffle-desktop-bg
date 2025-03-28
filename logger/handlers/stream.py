from handler import *
import sys

class StreamHandler(Handler):
    def __init__(self, terminator:chr='\n', flsh:bool=False) -> Exception:
        self.flsh = flsh
        self.terminator = terminator

    def flush():
        sys.stdout.flush()

    def close(self):
        self.flush()

    def emit(self, record: str):
        print(f'{record}{self.terminator}', flush=self.flsh)
