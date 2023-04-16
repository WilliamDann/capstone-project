from flask              import Flask
from get_database       import get_database

from routes.UserRoutes  import UserRoutes
from routes.Pages       import Pages
from Game               import Game, gameThread

from threading          import Thread
import logging

logging.basicConfig(filename='server.log', level=logging.DEBUG)

db  = get_database()         # Connect to MongoDB database
logging.info("Loaded mongo db.")

# TODO load & save game world
game = Game()
game.makeWorld(10)
logging.debug(game.world.tiles)
logging.debug(game.world.edges)
logging.info("Game world loaded.")

gameThread = Thread(target=gameThread, args=(db, game,), daemon=True)
gameThread.start()
logging.info("Started game thread.")

app = Flask(__name__)       # Create Flask app

UserRoutes(app, db)         # Create User HTTP Rotues
Pages(app, db)              # Create routes for html Pages