import random
from scripts.data.number_pattern import NumberPattern

class PrimeProgressionPattern(NumberPattern):
    def __init__(self, start_index, start_num, start_step):
        self.start_index = start_index
        self.start_num = start_num
        self.start_step = start_step

    def _eratosthenes(self, limit):
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, limit + 1, i):
                    is_prime[j] = False
        return [i for i, prime in enumerate(is_prime) if prime]

    def generate(self, count):
        '''
        Create a sequence where the steps are consecutive primes
        '''
        seq = [self.start_num]
        steps = self._eratosthenes(100)
        
        # Find start_step in the list, if not found use closest
        if self.start_step in steps:
            start_step_index = steps.index(self.start_step)
        else:
            start_step_index = 0
            
        # Generate enough numbers for start_index + count
        needed = self.start_index + count
        for i in range(start_step_index, len(steps)):
            if len(seq) >= needed:
                break
            prev = seq[-1] + steps[i]
            seq.append(prev)
            
        # If we still don't have enough, keep adding with last step
        while len(seq) < needed:
            seq.append(seq[-1] + steps[-1])
            
        return seq[self.start_index : self.start_index + count]

    def describe(self):
        return "Dãy số bắt đầu từ {} có khoảng cách giữa 2 số là số nguyên tố (gap đầu = {})".format(self.start_num, self.start_step)

    @classmethod        
    def random_instance(cls):
        start_index = random.randint(1, 20)
        start_num = random.randint(1, 100)
        # Generate primes up to 10 for start_step
        primes = []
        for num in range(2, 11):
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        start_step = random.choice(primes) if primes else 2
        return cls(start_index=start_index, start_num=start_num, start_step=start_step)