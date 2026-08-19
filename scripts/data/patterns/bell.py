import random
from scripts.data.number_pattern import NumberPattern

class BellPattern(NumberPattern):
    def __init__(self, start):
        self.start = start

    def _bell(self):
        return [1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147, 115975, 678570, 4213597, 27644437, 190899322]

    def generate(self, count):
        return self._bell()[self.start : self.start + count]
    
    def describe(self):
        return 'Số Bell (bắt đầu từ số thứ {})'.format(self.start)
    
    @classmethod
    def random_instance(cls):
        start = random.randint(1, 3)
        return cls(start = start)