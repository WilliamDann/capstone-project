from math import sqrt

class Position:
    x: int
    y: int
    tile: str

    def __init__(self, x: int, y: int, tile: str) -> None:
        self.x = x
        self.y = y
        self.tile = tile

    def __add__(self, other):
        self.x += other.x
        self.y += other.y

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y

    def dist(self, other):
        if other.tile != self.tile:
            return None # TODO this could be done better

        return sqrt(
            ((other.x - self.x) ** 2) -   \
            ((other.y - self.y) ** 2)     \
        )