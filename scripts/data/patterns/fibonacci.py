import random
from scripts.data.number_pattern import NumberPattern

class FibonacciPattern(NumberPattern):
    def __init__(self, start):
        self.start = start

    def generate(self, count):
        fibo = [0] * 60
        fibo[0], fibo[1] = 0, 1
        for index in range(2, 60):
            fibo[index] = fibo[index - 1] + fibo[index - 2]
        return fibo[self.start : self.start + count]

    def describe(self):
        return 'Dãy Fibonacci (bắt đầu từ số thứ {})'.format(self.start)

    @classmethod
    def random_instance(cls):
        start = random.randint(10, 40)
        return cls(start = start)