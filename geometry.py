'''Geometry'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rect:
    def __init__(self, topLeft, botRight):
        self.topLeft = topLeft
        self.botRight = botRight
