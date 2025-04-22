from abc import ABC, abstractmethod

class Handler:
    @abstractmethod
    def emit(self, record: str):
        pass

    @abstractmethod
    def close(self):
        pass