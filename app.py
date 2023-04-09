from flask              import Flask
from get_database       import get_database

from routes.UserRoutes  import UserRoutes
from routes.Pages       import Pages

app = Flask(__name__)       # Create Flask app
db  = get_database()         # Connect to MongoDB database

UserRoutes(app, db)         # Create User HTTP Rotues
Pages(app, db)              # Create routes for html Pages