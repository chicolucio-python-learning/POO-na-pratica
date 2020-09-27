from binary import Byte, adder, multiplier, Word


class Int8:
    def __init__(self, n):
        self.value = Byte(n)

    def __add__(self, other):
        sum_ = adder(self.value, other.value)
        return Int8(sum_)

    def __eq__(self, other):
        return self.value == other.value

    def __mul__(self, other):
        mul_ = multiplier(self.value, other.value)
        return Int8(mul_)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value!r})'

class Int16:
    def __init__(self, n):
        self.value = Word(n)

    def __add__(self, other):
        sum_ = adder(self.value, other.value)
        return Int16(sum_)

    def __eq__(self, other):
        return self.value == other.value

    def __mul__(self, other):
        mul_ = multiplier(self.value, other.value)
        return Int16(mul_)