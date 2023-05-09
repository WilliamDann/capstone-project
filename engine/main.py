from pymongo.database       import Database
from Game                   import Game
from engine.runner.main     import runner
from logging                import info

# Run a tick of the game
def tick(db: Database, game: Game):
    info(f"Started tick {game.time}")

    # Run user scripts
    users = db['users'].find({})
    for user in users:
        runner(user)

    info(f"Finished tick {game.time}")

    # Update game tick
    game.time += 1