import pytest

from adt import IntervalMap


def test_interval_map():
    m = IntervalMap()

    m[5] = 'cinco'
    m[10] = 'dez'
    m[15] = 'quinze'

    assert m.get(0) == 'cinco'
    assert m.get(4) == 'cinco'
    assert m.get(5) == 'dez'
    assert m.get(9) == 'dez'
    assert m.get(10) == 'quinze'
    assert m.get(14) == 'quinze'

    with pytest.raises(KeyError):
        m.get(15)