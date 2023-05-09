from model.Components.Position  import Position
from model.Components.Storage   import Storage
from enum                       import Enum

class Faction(Enum):
    Consortium  = 'Consortium', #poor faction, low quality, low prices
    ThePact     = 'ThePact',    #scavengers, resources only, no manufacturing
    Syndicate   = 'Syndicate',  #rich faction, high quality, high prices
    Ravagers    = 'Ravagers'    #pirates that attack


class Faction:
    objId       : str
    objType     : Faction

    position    : Position
    storage     : Storage

    owner       : "str|None"

    def __init__(self, objType: Faction) -> None:
        self.objType  = objType
        self.position = Position(0, 0, None)
        self.storage  = Storage(0)
        self.owner    = None
        self.objId    = None