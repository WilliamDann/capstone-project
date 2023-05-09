from pymongo.database   import Database
from Game               import Game

# Run a tick of the game
def tick(db: Database, game: Game):
    users = db['users'].find({})
    for user in users:
        pass