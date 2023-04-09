from flask              import Flask
from GetDatabase        import GetDatabase

from routes.UserRoutes  import UserRoutes

app = Flask(__name__)       # Create Flask app
db  = GetDatabase()         # Connect to MongoDB database

UserRoutes(app, db)         # Create User HTTP Rotues