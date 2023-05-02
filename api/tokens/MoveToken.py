from api.ReturnCode             import ReturnCode
from api.tokens.Token           import Token

from model.Object               import Object
from model.Components.Position  import Position
from model.World                import World

# Token to move an object in the game world
class MoveToken(Token):
    obj     : Object
    target  : Position

    def __init__(self, obj: Object, target: "Position|Object") -> None:
        self.obj    = obj

        # Ensure that 'target' is a Position
        if isinstance(target, Object):
            target = target.position
        self.target = target

        super().__init__()

    def action(self, world: World):
        # TODO move speed based on body parts
        # TODO pathfinding? what if it runs into something, for example

        moveSpeed   = 1
        obj         = world.objects.get(self.obj.objId)

        if not obj:
            return ReturnCode.InvalidArgs

        xDiff = obj.position.x - self.target.x
        yDiff = obj.position.y - self.target.y

        if xDiff >= 0:
            obj.position.x += min(moveSpeed, xDiff)
        else:
            obj.position.x -= max(-moveSpeed, xDiff)

        if yDiff >= 0:
            obj.position.y += min(moveSpeed, yDiff)
        else:
            obj.position.y -= max(-moveSpeed, yDiff)

        return ReturnCode.Ok