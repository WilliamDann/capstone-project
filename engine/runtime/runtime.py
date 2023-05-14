from engine.runtime.move    import move
from model.World            import World
from copy                   import deepcopy
from logging                import info

def getUserContext(username: str, world: World) -> dict:
    tiles = {}
    objs  = []

    for obj in world.objects.values():
        if obj.owner == username:
            tiles[obj.position.tile] = world.tiles[obj.position.tile].__dict__
            objs.append(obj.__dict__)

    return {
        'objects' : objs,
        'tiles'   : list(tiles.values())
    }

def runtime(username: str, world: World) -> dict:
    ctx = getUserContext(username, world)

    return {
        # Helpers
        'getObjectById' : None,         # Get an object by it's id
        'log'           : info,         # Logging function for debugging TODO remove

        # Object
        'move' : move,                  # Generates move intents

        # Globals
        'tiles'     : ctx['tiles'],     # Tiles the user is on
        'objects'   : ctx['objects'],   # Objects that belong to the user
        'world'     : deepcopy(world),  # Copy of World information TODO maybe not include this?
    }