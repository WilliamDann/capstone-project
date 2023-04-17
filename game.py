from model.Tile       import Tile
from model.World      import World
from random           import choice
from logging          import info
from time             import sleep
from pymongo.database import Database

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
            other = choice(list(self.world.tiles.values()))
            self.world.addEdge(self.world.tiles[tile], other)

    def tick(self):
        info(f'Starting tick {self.time+1}')
        self.time += 1
        info(f'Tick {self.time} Complete')

def gameThread(db: Database, game: Game):
    while True:
        game.tick()
        sleep(1)