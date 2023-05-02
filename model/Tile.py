from model.Object import Object
from model.Objects.Ship   import Ship
from model.Objects.Station import Station

class Tile:
    name    : str
    size    : int = 64

    def __init__(self, name: str) -> None:
        self.name    = name