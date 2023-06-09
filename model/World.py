from model.Object           import Object
from model.Tile             import Tile
from uuid                   import uuid4

class World:
    tiles   : "dict[str, Tile]"       # World Graph Verts: [tileName, tileObject]
    edges   : "dict[str, list[str]]"  # World Graph Edges: [tileAName, tileBName]

    objects : "dict[str, Object]"    # Objects in the game world [uuid, object]

    def __init__(self) -> None:
        self.tiles   = {}
        self.edges   = {}
        self.objects = {}

    def addTile(self, tile: Tile):
        self.tiles[tile.name] = tile
        self.edges[tile.name] = []

    def getTile(self, name: str) -> "Tile|None":
        return self.tiles.get(name)

    def addEdge(self, frm: Tile, to: Tile):
        self.edges[frm.name].append(to.name)

    def removeEdge(self, frm: Tile, to: Tile):
        self.edges[frm.name] = filter(lambda x: x != to.name, self.edges[frm.name])
        self.edges[to.name]  = filter(lambda x: x != frm.name, self.edges[to.name])

    def addObject(self, obj: Object):
        objId = uuid4().hex
        obj.objId           = objId
        self.objects[objId] = obj
        return objId

    def findObjects(self, f) -> "list[Object]":
        return list(filter(f, self.objects.values()))

    def findTiles(self, f) -> "list[Tile]":
        return list(filter(f, self.tiles.values()))