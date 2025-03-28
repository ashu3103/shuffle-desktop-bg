from abc import ABC, abstractmethod

class Handler:
    @abstractmethod
    def emit(record: str):
        pass

    @abstractmethod
    def close():
        pass