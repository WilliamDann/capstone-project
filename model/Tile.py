from model.Object import Object

class Tile:
    name    : str
    size    : int = 64

    def __init__(self, name: str) -> None:
        self.name    = name