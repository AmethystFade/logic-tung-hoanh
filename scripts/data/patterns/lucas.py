import random
from scripts.data.number_pattern import NumberPattern

class LucasPattern(NumberPattern):
    def __init__(self, start):
        self.start = start

    def _lucas_number(self):
        lucas = [0] * 60
        lucas[0], lucas[1] = 2, 1
        for i in range(2, 60):
            lucas[i] = lucas[i - 1] + lucas[i - 2]
        return lucas
    
    def generate(self, count):
        return self._lucas_number()[self.start : self.start + count]

    def describe(self):
        return 'Dãy Lucas (bắt đầu từ số thứ {})'.format(self.start)

    @classmethod
    def random_instance(cls):
        start = random.randint(5, 40)
        return cls(start = start)