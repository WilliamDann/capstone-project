from flask              import request
from pymongo.database   import Database

def readSession(db: Database):
    token = request.cookies.get('session')
    if not token:
        return None

    session = db['sessions'].find_one({"token": token})
    if not session:
        return None

    return db['users'].find_one({"username": session['username']})