from binary import Byte, adder


class Int8:
    def __init__(self, n):
        self.value = Byte(n)

    def __add__(self, other):
        sum_ = adder(self.value, other.value)
        return Int8(sum_)

    def __eq__(self, other):
        return self.value == other.value