import random
from scripts.data.number_pattern import NumberPattern

class PrimePattern(NumberPattern):
    def __init__(self, start):
        self.start = start
    
    def _eratosthenes(self, limit):
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, limit + 1, i):
                    is_prime[j] = False
        return [i for i, prime in enumerate(is_prime) if prime]
    
    def generate(self, count):
        primes = self._eratosthenes(1000)
        return primes[self.start : self.start + count]

    def describe(self):
        return 'Số nguyên tố (bắt đầu từ số thứ {})'.format(self.start)

    @classmethod
    def random_instance(cls):
        start = random.randint(5, 50)
        return cls(start = start)