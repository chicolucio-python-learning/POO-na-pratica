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

    assert Int8(127) + Int8(2) == Int8(254)