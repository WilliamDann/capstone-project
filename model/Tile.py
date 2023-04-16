from model.Objects.Object import Object

class Tile:
    name    : str
    objects : "list[Object]"

    def __init__(self, name: str) -> None:
        self.name    = name
        self.objects = []