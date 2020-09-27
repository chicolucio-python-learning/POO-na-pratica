import pytest

from integers import Int8


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