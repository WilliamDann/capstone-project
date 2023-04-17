from model.Components.Position  import Position
from model.Components.Storage   import Storage

class Object:
    position    : Position
    storage     : Storage

    owner       : "str|None"

    def __init__(self) -> None:
        self.position = Position(0, 0, None)
        self.storage  = Storage(0)
        self.owner    = None