import os
from .handler import *

class FileHandler(Handler):
    def __init__(self, filename:str, mode:chr='a', terminator:chr='\n', delay:bool=False) -> Exception:
        self.filename = filename
        self.terminator = terminator
        self.mode = mode
        self.delay = delay
        try:
            if not delay:
                file = open(filename, mode)
                self.file = file
        except (FileNotFoundError):
            print(f'File {filename} doesn\'t exist')
        except Exception as e:
            print(f'An error occured: {e}')

    def close(self):
        if self.file:
            self.file.close()

    def emit(self, record: str):
        try:
            if self.delay and not self.file:
                file = open(self.filename, self.mode)
                self.file = file
            if not self.file:
                raise Exception("File not opened")
            
            ## everything is okay, write the record
            self.file.write(f'{record}{self.terminator}')
        except (FileNotFoundError):
            print(f'File {self.filename} doesn\'t exist')
        except Exception as e:
            print(f'An error occured: {e}')
