from flask              import Flask
from GetDatabase        import GetDatabase

from routes.UserRoutes  import UserRoutes
from routes.Pages       import Pages

app = Flask(__name__)       # Create Flask app
db  = GetDatabase()         # Connect to MongoDB database

UserRoutes(app, db)         # Create User HTTP Rotues
Pages(app, db)              # Create routes for html Pages