from flask              import Flask
from get_database       import get_database

from Game               import Game, gameThread
from routes.UserRoutes  import UserRoutes
from routes.GameRoutes  import GameRoutes
from routes.Pages       import Pages

from threading          import Thread
import logging

logging.basicConfig(filename='server.log', level=logging.DEBUG)

db  = get_database()         # Connect to MongoDB database
logging.info("Loaded mongo db.")

# TODO load & save game world
game = Game()
game.makeWorld(10)
logging.info("Game world loaded.")

gameThread = Thread(target=gameThread, args=(db, game,), daemon=True)
gameThread.start()
logging.info("Started game thread.")

app = Flask(__name__)       # Create Flask app

UserRoutes(app, db)         # Create User HTTP Rotues
GameRoutes(app, db, game)
Pages(app, db)              # Create routes for html Pages