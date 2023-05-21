from model.World  import World
from model.Object import ObjectType

def find(world: World, t: ObjectType):
    return world.findObjects(lambda x: x.objType == t)