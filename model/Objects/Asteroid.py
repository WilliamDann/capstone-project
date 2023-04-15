from model.Objects.Object       import Object
from model.Components.Storage   import ResourceType

class Asteroid(Object):
    resourceType: ResourceType

    def __init__(self, rtype: ResourceType, amount: int) -> None:
        super().__init__()

        self.storage.totalSpace  = amount
        self.storage[rtype]     += amount

        self.resourceType = rtype
