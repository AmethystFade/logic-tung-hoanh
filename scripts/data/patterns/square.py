import random
from scripts.data.number_pattern import NumberPattern

class SquarePattern(NumberPattern):
    def __init__(self, start):
        self.start = start

    def _square(self):
        return [i * i for i in range(1, 101)]
    
    def generate(self, count):
        return self._square()[self.start : self.start + count]
    
    def describe(self):
        return 'Số chính phương (bắt đầu từ số thứ {})'.format(self.start)
    
    @classmethod
    def random_instance(cls):
        start = random.randint(5, 75)
        return cls(start = start)
