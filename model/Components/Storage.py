from enum import Enum

class ResourceType(Enum):
    Credits ='credits',
    Iron    ='iron',
    Copper  ='copper'

class Storage:
    store       : "dict[ResourceType, int]"

    usedSpace   : int
    totalSpace  : int

    def __init__(self, totalSpace: int) -> None:
        self.totalSpace = totalSpace
        self.store      = {}

    def withdraw(self, type: ResourceType, n: int) -> bool:
        if self.usedSpace+n > self.totalSpace:
            return False

        if self.store.get(type) is None:
            self.store[type] = 0
        self.store[type] += n

        self.usedSpace += n
        return True

    def deopsit(self, type: ResourceType, n: int) -> bool:
        if self.store.get(type) is None:
            return False
        if self.store.get(type)-n < 0:
            return False

        self.store[type] -= n
        self.usedSpace   -= n

        return True
