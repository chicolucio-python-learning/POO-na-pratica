import pytest

from integers import Int8, Int16, Int24, Int32


def test_int8():
    assert isinstance(Int8(0), Int8)
    assert isinstance(Int8(255), Int8)

    with pytest.raises(ValueError):
        Int8(256)

    assert Int8(0) + Int8(0) == Int8(0)
    assert Int8(1) + Int8(1) == Int8(2)
    assert Int8(254) + Int8(1) == Int8(255)

    assert Int8(127) * Int8(2) == Int8(254)

def test_int16():
    assert isinstance(Int16(0), Int16)
    assert isinstance(Int16(65535), Int16)

    with pytest.raises(ValueError):
        Int16(65536)

    assert Int16(0) + Int16(0) == Int16(0)
    assert Int16(255) + Int16(1) == Int16(256)

    assert Int16(256) * Int16(2) == Int16(512)

def test_int24():
    assert isinstance(Int24(0), Int24)
    assert isinstance(Int24(16_777_215), Int24)
    with pytest.raises(ValueError):
        Int24(16_777_216)

    assert Int24(0) + Int24(0) == Int24(0)
    assert Int24(65535) + Int24(1) == Int24(65536)

    assert Int24(65536) * Int24(2) == Int24(131_072)


def test_int32():
    assert isinstance(Int32(0), Int32)
    assert isinstance(Int32(4_294_967_295), Int32)
    with pytest.raises(ValueError):
        Int32(4_294_967_296)

    assert Int32(0) + Int32(0) == Int32(0)
    assert Int32(16_777_215) + Int32(1) == Int32(16_777_216)

    assert Int32(16_777_216) * Int32(2) == Int32(33_554_432)

def test_scale_up():
    assert Int8(255) + Int8(1) == Int16(256)
    assert Int8(128) * Int8(2) == Int16(256)

    assert Int16(65_535) + Int16(1) == Int24(65_536)
    assert Int16(32_768) * Int16(2) == Int24(65_536)

    assert Int24(16_777_215) + Int24(1) == Int32(16_777_216)
    assert Int24(8_388_608) * Int24(2) == Int32(16_777_216)