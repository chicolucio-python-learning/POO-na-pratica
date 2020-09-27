from abc import ABC

from binary import Byte, adder, multiplier, Word, Tribyte, DoubleWord


class Integer(ABC):
    STORAGE = bytes
    def __init__(self,n):
        self.value = self.STORAGE(n)

    def __add__(self, other):
        return self.factory(adder(self.value, other.value))

    def __eq__(self, other):
        return self.value == other.value

    def __mul__(self, other):
        return self.factory(multiplier(self.value, other.value))

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value!r})'

    @classmethod
    def factory(cls, n):
        if n < 256:
            klass = Int8
        elif n < 65_536:
            klass = Int16
        elif n < 16_777_216:
            klass = Int24
        elif n < 4_294_967_296:
            klass = Int32
        return klass(n)

class Int8(Integer):
    STORAGE = Byte


class Int16(Integer):
    STORAGE = Word


class Int24(Integer):
    STORAGE = Tribyte


class Int32(Integer):
    STORAGE = DoubleWord
