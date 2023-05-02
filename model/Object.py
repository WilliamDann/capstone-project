from model.Components.Position  import Position
from model.Components.Storage   import Storage
from enum import Enum

class objType(Enum):
    Ship        = 'Ship',
    Asteroid    = 'Asteroid',
    Comet       = 'Comet',
    Planet      = 'Planet',
    Station     = 'Station',
    DeadPlanet  = 'DeadPlanet',
    Star        = 'Star'


class Object:
    objId       : str
    objType     : Enum

    position    : Position
    storage     : Storage

    owner       : "str|None"

    def __init__(self, objType: Enum) -> None:
        self.objType  = objType
        self.position = Position(0, 0, None)
        self.storage  = Storage(0)
        self.owner    = None
        self.objId    = None