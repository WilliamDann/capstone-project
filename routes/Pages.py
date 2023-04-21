from flask      import render_template, make_response
from flask.app  import Flask

from read_session import read_session

def Pages(app: Flask, db):
    @app.get('/')
    def home():
        return render_template('home.html')

    @app.get('/signin')
    def signin():
        return render_template('User/signin.html')

    @app.get('/signup')
    def signup():
        return render_template('User/signup.html')

    @app.get('/signout')
    def signout():
        user = read_session(db)
        if not user:
            return render_template('User/signin.html')

        resp = make_response(render_template('User/signin.html', info="Signout successful."))
        resp.set_cookie('session', '', expires=0)
        return resp

    @app.get('/account')
    def userAccount():
        user = read_session(db)
        if not user:
            return render_template("User/signin.html")
        return render_template('User/account.html', user=user)
    
    @app.get('/changepass')
    def changePass():
        user = read_session(db)
        if not user:
            return render_template("User/signin.html")
        return render_template('User/changepass.html', user=user)
    
    @app.get('/User/delete')
    def deleteUserConfirm():
        user = read_session(db)
        if not user:
            return render_template("User/signin.html")
        return render_template("User/delete.html", user=user)