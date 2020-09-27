'''Geometry'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __truediv__(self, scalar):
        return self.__class__(self.x / scalar, self.y / scalar)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'


class Rect:
    def __init__(self, topLeft, botRight):
        self.topLeft = topLeft
        self.botRight = botRight

    def center(self):
        return (self.topLeft + self.botRight) / 2

    def __repr__(self):
        return f'{self.__class__.__name__}({self.topLeft!r}, {self.botRight!r})'