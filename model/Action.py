from model.Components.Position  import Position
from model.Components.Storage   import Storage
from enum                       import Enum

class ActionType(Enum):
    Mine        = 'Mine',
    Process     = 'Process',
    Manufacture = 'Manufacture',
    Trade       = 'Trade',
    Build       = 'Build',
    Repair      = 'Repair',
    Research    = 'Research'


class Action:
    objId       : str
    objType     : ActionType

    position    : Position
    storage     : Storage

    owner       : "str|None"

    def __init__(self, objType: ActionType) -> None:
        self.objType  = objType
        self.position = Position(0, 0, None)
        self.storage  = Storage(0)
        self.owner    = None
        self.objId    = None