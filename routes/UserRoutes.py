from flask              import request, jsonify
from flask.app          import Flask
from pymongo.database   import Database
from hashlib            import sha256

from model.User import User

def UserRoutes(app: Flask, db: Database):
    @app.post('/api/user')
    def userCreate():
        username = request.form.get('username')
        password = request.form.get('password')

        if not username:
            return "A 'username' is required to create a user", 400
        if db['users'].find_one({'username': username}):
            return "User already exists", 400
        if not password:
            return "A 'password' is required to create a user", 400

        hashedPassword = sha256(password.encode('utf-8')).hexdigest()

        db['users'].insert_one({ "username": username, "pwHash": hashedPassword })
        return "User created", 200

    @app.get('/api/user')
    def userRead():
        username = request.args.get('username')

        if not username:
            return "A 'username' is required to get a user", 400

        found = db['users'].find_one({'username': username})
        if not found:
            return f'User "{username}" does not exist', 404

        found['_id']    = str(found['_id'])
        found['pwHash'] = None
        return jsonify(found), 200

    @app.put('/api/user')
    def userUpdate():
        return "NOT IMPLEMENTED", 500

    @app.delete('/api/user')
    def userDelete():
        return "NOT IMPLEMENTED", 500