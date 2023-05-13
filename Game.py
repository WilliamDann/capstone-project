from model.Tile         import Tile
from model.World        import World
from random             import choice
from time               import sleep
from pymongo.database   import Database
import engine.main      as engine

class Game:
    time    : int
    world   : World

    def __init__(self) -> None:
        self.time   = 0
        self.world  = World()

    def makeWorld(self, tiles=10):
        for i in range(tiles):
            self.world.addTile(Tile(f'Tile{i}'))
        for tile in self.world.tiles:
            for i in range(2):
                other = choice(list(self.world.tiles.values()))
                self.world.addEdge(self.world.tiles[tile], other)

def gameThread(db: Database, game: Game):
    while True:
        engine.tick(db, game)
        sleep(5)