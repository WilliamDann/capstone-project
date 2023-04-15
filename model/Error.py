from enum import Enum

class Error(Enum):
    Ok              = 0
    
    NotInRange      = -1
    ResourceMissing = -2
    StorageFull     = -3