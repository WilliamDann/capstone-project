from math import sqrt

class Position:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y

    def dist(self, other):
        return sqrt(
            ((other.x - self.x) ** 2) -   \
            ((other.y - self.y) ** 2)     \
        )