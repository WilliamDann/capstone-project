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
        self.time += 1
        info(f'Tick {self.time} Complete')

def gameThread(db: Database, game: Game):
    while True:
        game.tick()

        userList = db['users'].find( {} )
        for user in userList:
            username = user.get('username')
            userCode = user.get("userCode")

            if not username or not userCode:
                continue

            # This code is responsible for executing user python code
            # This is basically a remote code execution vulnerability baked into our app
            # DO NOT TOUCH THIS UNLESS YOU KNOW WHAT YOU ARE DOING. 
            try:
                exec(userCode,                  \
                    {"__builtins__": None},     \
                    {}
                )
            except Exception as e:
                pass

        sleep(5)