from WorldBuilder import WorldBuilder
from model.Tile         import Tile
from model.World        import World
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
        return WorldBuilder()   \
            .makeTiles(10)      \
            .connectTiles(2)    \
            .build()

def gameThread(db: Database, game: Game):
    while True:
        engine.tick(db, game)
        sleep(5)