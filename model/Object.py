from model.Components.Position  import Position
from model.Components.Storage   import Storage
from enum                       import Enum

class ObjectType(Enum):
    Ship        = 'Ship',
    Asteroid    = 'Asteroid',
    Comet       = 'Comet',
    Planet      = 'Planet',
    Station     = 'Station',
    DeadPlanet  = 'DeadPlanet',
    DeadStation = 'DeadStation',
    Star        = 'Star'


class Object:
    objId       : str
    objType     : ObjectType

    health      : int
    position    : Position
    storage     : Storage

    owner       : "str|None"

    def __init__(self, objType: ObjectType) -> None:
        self.objType  = objType
        self.position = Position(0, 0, None)
        self.storage  = Storage(0)
        self.health   = 100
        self.owner    = None
        self.objId    = None