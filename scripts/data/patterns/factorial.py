import random
import math
from scripts.data.number_pattern import NumberPattern

class FactorialPattern(NumberPattern):
    def __init__(self, start):
        self.start = start

    def _factorial(self):
        return [i * math.factorial(i) for i in range(1, 15)]
    
    def generate(self, count):
        return self._factorial()[self.start : self.start + count]
    
    def describe(self):
        return 'Số giai thừa (bắt đầu từ số thứ {})'.format(self.start)
    
    @classmethod
    def random_instance(cls):
        start = random.randint(1, 3)
        return cls(start = start)