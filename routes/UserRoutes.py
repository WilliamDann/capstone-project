from flask              import request, jsonify, render_template, make_response
from flask.app          import Flask
from pymongo.database   import Database
from hashlib            import sha256
from uuid               import uuid4
from read_session       import read_session

def UserRoutes(app: Flask, db: Database):
    @app.post('/api/user/auth')
    def authUser():
        username = request.form.get('username')
        password = request.form.get('password')

        if not username:
            return render_template("Error.html", error="Username not provided"), 400
        if not password:
            return render_template("Error.html", error="Password not provided"), 400

        storedUser = db['users'].find_one({"username": username})
        if not storedUser:
            return render_template("Error.html", error="Authentication error"), 400

        if storedUser['pwHash'] != sha256(password.encode('utf-8')).hexdigest():
            return render_template("Error.html", error="Authentication error"), 400

        token = uuid4().hex
        db['sessions'].insert_one( { "username": username, "token": token } )

        storedUser['pwHash'] = None
        resp = make_response(render_template("/User/account.html", user=storedUser))
        resp.set_cookie('session', token)

        return resp

    @app.post('/api/user')
    def userCreate():
        username = request.form.get('username')
        password = request.form.get('password')

        if not username:
            return render_template("User/signup.html", error="Username required"), 400
        if db['users'].find_one({'username': username}):
            return render_template("User/signup.html", error="Username already exists"), 400
        if not password:
            return render_template("User/signup.html", error="Password required"), 400

        hashedPassword = sha256(password.encode('utf-8')).hexdigest()

        db['users'].insert_one({ "username": username, "pwHash": hashedPassword })
        return render_template("User/signin.html", info="User creation successful, please sign in")

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
    @app.post('/api/user/update')
    def userUpdate():
        username = request.form.get('username')
        currentPassword = request.form.get('currentPassword')
        newPassword = request.form.get('newPassword')
        if read_session(db).get('username') != username:
            return render_template("Error.html", error="Authentication error"), 400            
        if not username:
            return render_template("User/changepass.html", error="Username not provided"), 400
        if not currentPassword:
            return render_template("User/changepass.html", msg = "password required")
        if not newPassword:
            return render_template("User/changepass.html", msg = "password required")
        storedUser = db['users'].find_one({"username": username})
        if not storedUser:
            return render_template("User/changepass.html", error="Incorrect username"), 400
        if storedUser['pwHash'] != sha256(currentPassword.encode('utf-8')).hexdigest():
            return render_template("Error.html", error="Authentication error"), 400
        hashedPassword = sha256(newPassword.encode('utf-8')).hexdigest()
        db['users'].update_one({ "username": username }, { "$set": { "pwHash": hashedPassword } })
        hashedPassword = None
        return render_template("User/account.html", user = username)

    @app.post('/api/user/delete')
    @app.delete('/api/user')
    def userDelete():
        username = request.form.get('username')
        session  = read_session(db)

        if not username:
            return render_template("Error.html", error="username is required to delete a user")
        
        if not session or not session.get('username'):
            return render_template("Error.html", error="Authentication Error"), 400
        if session.get('username') != username:
            return render_template("Error.html", error="Authentication Error"), 400
        
        # Delete user and user sign in sessions
        db['users'].delete_one({'username': session.get('username')})
        db['sessions'].delete_many({'username': session.get('username')})

        return render_template("User/signin.html", info="User deleted."), 200
        