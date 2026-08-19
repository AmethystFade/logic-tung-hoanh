import random
from scripts.data.number_pattern import NumberPattern

class TriangularPattern(NumberPattern):
    def __init__(self, start):
        self.start = start

    def _triangular(self):
        return [i * (i + 1) // 2 for i in range(1, 101)]
    
    def generate(self, count):
        return self._triangular()[self.start : self.start + count]
    
    def describe(self):
        return 'Số tam giác (bắt đầu từ số thứ {})'.format(self.start)
    
    @classmethod
    def random_instance(cls):
        start = random.randint(5, 75)
        return cls(start = start)

    