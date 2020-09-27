from binary import Bits, adder, multiplier


def test_how_many_bytes():
    assert Bits.how_many_bytes(0) == 1
    assert Bits.how_many_bytes(1) == 1
    assert Bits.how_many_bytes(255) == 1
    assert Bits.how_many_bytes(256) == 2
    assert Bits.how_many_bytes(65535) == 2
    assert Bits.how_many_bytes(65536) == 3


def test_number_to_bits():
    assert list(Bits.number_to_bits(0)) == [0]
    assert list(Bits.number_to_bits(1)) == [1]
    assert list(Bits.number_to_bits(255)) == [255]
    assert list(Bits.number_to_bits(256)) == [0, 1]
    assert list(Bits.number_to_bits(65535)) == [255, 255]
    assert list(Bits.number_to_bits(65536)) == [0, 0, 1]


def test_bits_big_endian_layout():
    assert Bits(1) == bytes([1])
    assert Bits(255) == bytes([255])
    assert Bits(256) == bytes([0, 1])
    assert Bits(65535) == bytes([255, 255])
    assert Bits(65536) == bytes([0, 0, 1])
    assert Bits(131_070) == bytes([0xfe, 0xff, 0x1])


def test_bits_iter():
    assert list(Bits(0)) == [0]
    assert list(Bits(1)) == [1]
    assert list(Bits(2)) == [0, 1]
    assert list(Bits(128)) == [0, 0, 0, 0, 0, 0, 0, 1]
    assert list(Bits(255)) == [1, 1, 1, 1, 1, 1, 1, 1]
    assert list(Bits(257)) == [1, 0, 0, 0, 0, 0, 0, 0, 1]
    assert list(Bits(256)) == [0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert list(Bits(131_070)) == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def test_bits_to_number():
    assert Bits(257).to_number() == 257


def test_bits_shift_left():
    assert Bits(1) << Bits(1) == Bits(2)


def test_adder():
    assert adder(Bits(0), Bits(0)) == 0
    assert adder(Bits(1), Bits(0)) == 1
    assert adder(Bits(0), Bits(1)) == 1
    assert adder(Bits(1), Bits(1)) == 2
    assert adder(Bits(5), Bits(12)) == 17
    assert adder(Bits(255), Bits(1)) == 256


def test_multiplier():
    assert multiplier(Bits(0), Bits(0)) == 0
    assert multiplier(Bits(1), Bits(0)) == 0
    assert multiplier(Bits(0), Bits(1)) == 0
    assert multiplier(Bits(1), Bits(1)) == 1
    assert multiplier(Bits(2), Bits(3)) == 6
    assert multiplier(Bits(127), Bits(2)) == 254
