from enum import Enum

class ReturnCode(Enum):
    Ok              = 0

    NotInRange      = -1
    ResourceMissing = -2
    StorageFull     = -3