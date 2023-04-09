from flask      import render_template, make_response
from flask.app  import Flask

from readSession import readSession

def Pages(app: Flask, db):
    @app.get('/')
    def home():
        return render_template('home.html')

    @app.get('/play')
    def play():
        return render_template('play.html')

    @app.get('/signin')
    def signin():
        return render_template('User/signin.html')

    @app.get('/signup')
    def signup():
        return render_template('User/signup.html')
    
    @app.get('/signout')
    def signout():
        user = readSession(db)
        if not user:
            return render_template('User/signin.html')

        resp = make_response(render_template('User/signin.html'))
        resp.set_cookie('session', '', expires=0)
        return resp

    @app.get('/account')
    def userAccount():
        user = readSession(db)
        if not user:
            return render_template("User/signin.html")
        return render_template('User/account.html', user=user)