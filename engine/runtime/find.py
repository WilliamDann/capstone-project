from model.World  import World
from model.Object import ObjectType

def find(world: World, t: ObjectType, tile: str):
    return world.findObjects(lambda x: x.objType == t and x.position.tile == tile)