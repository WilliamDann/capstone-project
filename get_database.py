from pymongo            import MongoClient
from pymongo.database   import Database

# Load the connection string from config file and connect to MongoDB
def get_database(configFile='db.config') -> Database:
    with open(configFile, 'r') as file:
        return MongoClient(file.readline())['capstone']