from enum import Enum

class ReturnCode(Enum):
    # SUCCESS
    Ok              = 0

    # ERROR
    NotInRange       = -1
    ResourceMissing  = -2
    StorageFull      = -3
    InvalidArguments = -4

    # OTHER