'''Geometry'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Rect:
    def __init__(self, topLeft, botRight):
        self.topLeft = topLeft
        self.botRight = botRight

    def center(self):
        return Point((self.topLeft.x + self.botRight.x) / 2,
                     (self.topLeft.y + self.botRight.y) / 2)