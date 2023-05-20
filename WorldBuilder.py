from model.Tile import Tile
from model.World import World
from random      import choice

class WorldBuilder:
    world: World
    def __init__(self):
        self.world = World()

    # Makes tiles in the world
    def makeTiles(self, num=10):
        for i in range(num):
            self.world.addTile(Tile(f'Tile{i}'))
        return self

    # Connects tiles in the world
    def connectTiles(self, num=2):
        for tile in self.world.tiles:
            for i in range(num):
                other = choice(list(self.world.tiles.values()))
                self.world.addEdge(self.world.tiles[tile], other)
        return self

    # Create the world object
    def build(self):
        return self.world