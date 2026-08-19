import random
from scripts.data.number_pattern import NumberPattern

class DoubleArithmeticPattern(NumberPattern):
    '''
    Dãy số lồng nhau tịnh tiến
    Các vị trí lẻ sẽ tuân theo dãy riêng
    Các vị trí chẵn sẽ tuân theo dãy riêng 
    Chỉ áp dụng cho dãy ngang
    '''
    def __init__(self, start_1, step_1, start_2, step_2):
        self.start_1 = start_1
        self.step_1 = step_1
        self.start_2 = start_2
        self.step_2 = step_2

    def generate(self, count = 8):
        seq = [0] * count
        if count > 0:
            seq[0] = self.start_1
        if count > 1:
            seq[1] = self.start_2
        for i in range(2, count):
            if i % 2 == 0:
                seq[i] = seq[i - 2] + self.step_1
            else:
                seq[i] = seq[i - 2] + self.step_2
        return seq

    def describe(self):
        return 'Dãy số đôi, dãy ở vị trí lẻ bắt đầu từ {} cách nhau {}, dãy ở vị trí chẵn bắt đầu từ {} cách nhau {}'.format(self.start_1, self.step_1, self.start_2, self.step_2)

    @classmethod
    def random_instance(cls):
        start_1 = random.randint(1, 20)
        step_1 = random.randint(4, 100)
        start_2 = random.randint(1, 20)
        step_2 = random.randint(4, 100)
        return cls(start_1=start_1, step_1=step_1, start_2=start_2, step_2=step_2)