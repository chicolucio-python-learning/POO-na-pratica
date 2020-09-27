from abc import ABC

from adt import IntervalMap
from binary import Byte, adder, multiplier, Word, Tribyte, DoubleWord


class Integer(ABC):
    STORAGE = bytes
    types = IntervalMap()

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
        klass = cls.types.get(n)
        return klass(n)

    @classmethod
    def register(cls, upper_bound, klass):
        cls.types[upper_bound] = klass


def Int(n):
    return Integer.factory(n)


class Int8(Integer):
    STORAGE = Byte


class Int16(Integer):
    STORAGE = Word


class Int24(Integer):
    STORAGE = Tribyte


class Int32(Integer):
    STORAGE = DoubleWord

Integer.register(256, Int8)
Integer.register(65_536, Int16)
Integer.register(16_777_216, Int24)
Integer.register(4_294_967_296, Int32)