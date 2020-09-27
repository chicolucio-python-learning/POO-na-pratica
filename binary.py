from itertools import zip_longest


class Bits(bytes):
    CHUNK = 8

    def __new__(cls, n):
        return super().__new__(cls, cls.number_to_bits(n))

    @staticmethod
    def number_to_bits(n, size=CHUNK):
        length = Bits.how_many_bytes(n, size=size)
        mask = 2 ** size - 1
        offset = lambda i: i * size
        bit_slice = lambda n, i: (n & (mask << offset(i))) >> offset(i)

        return (bit_slice(n, i) for i in range(length))

    def to_number(self):
        return sum(byte_ * (2 ** (8 * i))
                   for i, byte_ in enumerate(super().__iter__()))

    @staticmethod
    def how_many_bytes(value, size=CHUNK):
        l = 1
        limit = (2 ** size) - 1
        while value > limit:
            value >>= size
            l += 1
        return l

    def __repr__(self):
        return f'{self.to_number()}'



    def __iter__(self):
        if self == bytes([0]):
            yield 0
            return

        size = self.CHUNK
        last_byte = len(self) - 1

        for byte_number, value in enumerate(super().__iter__()):
            count = 0

            while value:
                yield value & 1
                value >>= 1
                count += 1

            if byte_number < last_byte:
                yield from (0 for _ in range(size - count))


    def __lshift__(self, other):
        return Bits(self.to_number() << other.to_number())


class Byte(Bits):
    SIZE = 1

    def __new__(cls, n):
        if n >= cls.upper_bound():
            raise ValueError(f'{n}. Byte must be in range(0, {cls.upper_bound()})')

        return super().__new__(cls, n)

    @classmethod
    def upper_bound(cls):
        return 2 ** (cls.SIZE * cls.CHUNK)


class Word(Byte):
    SIZE = 2


class Tribyte(Byte):
    SIZE = 3


class DoubleWord(Byte):
    SIZE = 4


def fulladder(a, b, cin):
    sum_ = (a ^ b) ^ cin
    cout = a & b | cin & (a ^ b)
    return sum_, cout


def adder(n, m):
    acc = sum_ = cout = cin = 0

    for i, (a, b) in enumerate(zip_longest(n, m, fillvalue=0)):
        sum_, cout = fulladder(a, b, cin)

        acc |= sum_ << i
        cin = cout

    acc |= cout << (i + 1)

    return acc


def multiplier(n, m):
    acc = Bits(0)
    shifter = 0

    for bit in m:
        if bit == 1:
            acc = Bits(adder(acc, n << Bits(shifter)))
        shifter += 1

    return acc.to_number()
