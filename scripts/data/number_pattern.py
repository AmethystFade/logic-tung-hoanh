from abc import ABC, abstractmethod

class NumberPattern(ABC):

    @abstractmethod
    def generate(self, count):
        raise NotImplementedError
    
    @abstractmethod
    def describe(self):
        raise NotImplementedError