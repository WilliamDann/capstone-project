from flask              import Flask
from get_database       import get_database

from routes.UserRoutes  import UserRoutes
from routes.Pages       import Pages
from game               import Game, gameThread

from threading          import Thread
import logging

logging.basicConfig(filename='server.log', level=logging.DEBUG)

game = Game()
game.makeWorld(10)
logging.debug(game.world.tiles)
logging.debug(game.world.edges)

gameThread = Thread(target=gameThread, args=(game,), daemon=True)
logging.info("Starting game thread...")
gameThread.start()

app = Flask(__name__)       # Create Flask app
db  = get_database()         # Connect to MongoDB database

UserRoutes(app, db)         # Create User HTTP Rotues
Pages(app, db)              # Create routes for html Pages