from geometry import Point, Rect


def test_rect():
    r = Rect(Point(1, 1), Point(3, 3))
    assert isinstance(r, Rect)
    assert r.topLeft == Point(1, 1)
    assert r.botRight == Point(3, 3)
    assert r.center() == Point(2, 2)
    assert repr(r) == 'Rect(Point(1, 1), Point(3, 3))'


def test_point():
    p = Point(2, 4)
    assert isinstance(p, Point)
    assert p.x == 2
    assert p.y == 4