from model.Components.Position  import Position
from model.Objects.Object       import Object
from model.Objects.Asteroid     import Asteroid
from model.ReturnCode           import ReturnCode

class Ship(Object):
    _actionRange : int                  # Range actions can be taken in

    _moveAmount  : int                  # Amount moved per moveTo() tick. (should be replaced later with a component system)
    _mineAmount  : int                  # The amount mined per mine() tick. (should be replaced later with a component system)

    def __init__(self) -> None:
        super().__init__("Ship")
        self._mineAmount  = 10
        self._moveAmount = 2

    def mine(self, target: Asteroid) -> ReturnCode:
        if self.position.dist(target) > self._actionRange:
            return ReturnCode.NotInRange

        # Withdraw resource from target if resource avalible
        if not target.storage.withdraw(target.resourceType, self._mineAmount):
            return ReturnCode.ResourceMissing

        # Deposit resource into ship if storage space avalible
        if not self.storage.deopsit(target.resourceType, self._mineAmount):
            return ReturnCode.StorageFull

        return ReturnCode.Ok