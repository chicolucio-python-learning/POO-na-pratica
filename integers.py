from abc import ABC

from binary import Byte, adder, multiplier, Word, Tribyte, DoubleWord


def select(n):
    if 0 <= n < 256:
        return Int8(n)
    elif 256 <= n < 65_536:
        return Int16(n)
    elif 65_536 <= n < 16_777_216:
        return Int24(n)
    elif 16_277_216 <= n < 4_294_967_296:
        return  Int32(n)
    raise ValueError


class Integer(ABC):
    STORAGE = bytes
    def __init__(self,n):
        self.value = self.STORAGE(n)

    def __add__(self, other):
        sum_ = adder(self.value, other.value)
        return select(sum_)

    def __eq__(self, other):
        return self.value == other.value

    def __mul__(self, other):
        mul_ = multiplier(self.value, other.value)
        return select(mul_)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value!r})'


class Int8(Integer):
    STORAGE = Byte


class Int16(Integer):
    STORAGE = Word


class Int24(Integer):
    STORAGE = Tribyte


class Int32(Integer):
    STORAGE = DoubleWord
