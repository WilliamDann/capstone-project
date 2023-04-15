from dataclasses                import dataclass
from model.Components.Position  import Position
from model.Components.Storage   import Storage

class Object:
    position    : Position
    storage     : Storage

    def __init__(self) -> None:
        self.position = Position()
        self.storage  = Storage()