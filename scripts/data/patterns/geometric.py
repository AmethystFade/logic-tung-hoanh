import random
from scripts.data.number_pattern import NumberPattern

class GeometryPattern(NumberPattern):
    def __init__(self, start, ratio):
        self.start = start
        self.ratio = ratio

    def generate(self, count):
        return [self.start * (self.ratio ** i) for i in range(count)]
    
    def describe(self):
        return 'Cấp số nhân (bắt đầu: {}, tỉ số: {})'.format(self.start, self.ratio)
    
    @classmethod
    def random_instance(cls):
        start = random.randint(1, 15)
        ratio = random.randint(4, 9)
        return cls(start = start, ratio = ratio)