import random
from scripts.data.number_pattern import NumberPattern

class ArithmeticPattern(NumberPattern):
    def __init__(self, start, step):
        self.start = start
        self.step = step

    def generate(self, count):
        return [self.start + i * self.step for i in range(count)]

    def describe(self):
        return 'Cấp số cộng (bắt đầu: {}, bước: {})'.format(self.start, self.step)

    @classmethod
    def random_instance(cls):
        start = random.randint(100, 500)
        step = random.randint(50, 1000)
        return cls(start = start, step = step)