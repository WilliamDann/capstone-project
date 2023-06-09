import logging
from flask                      import render_template, request
from flask.app                  import Flask
from pymongo.database           import Database
from model.Components.Position  import Position
from Game                       import Game
from random                     import randint
from json                       import dumps

from engine.runtime.runtime     import runtime
from model.Object               import ObjectType, Object

from read_session import read_session

def dict_decode(inst):
    try:
        if type(inst) == dict:
            return inst
        return inst.__dict__
    except:
        return None

def GameRoutes(app: Flask, db: Database, game: Game):
    @app.post('/api/game/debugSpawn')
    def debugSpawn():
        objType = ObjectType[request.form.get('objType')]
        health  = request.form.get('health')
        x       = request.form.get('x')
        y       = request.form.get('y')
        tile    = request.form.get('tile')
        owner   = request.form.get('owner')

        if not objType:
            return "objType must be defined", 400
        if not tile:
            return "tile must be defined", 400
        obj = Object(objType)
        obj.position.tile = tile

        if health:
            obj.health      = health
        if x:
            obj.position.x  = x
        if y:
            obj.position.y  = y
        if owner:
            obj.owner       = owner

        game.world.addObject(obj)
        return "Object spawned", 200

    @app.get('/play')
    def playPage():
        user = read_session(db)
        if not user:
            return render_template("User/signin.html")
        return render_template('Play.html', game=dumps(game.__dict__, default=dict_decode))

    @app.get('/api/game/')
    def getGame():
        user     = read_session(db)
        if not user:
            return render_template("Error.html", error="Authentication error"), 400
        game.user = user
        game.user['pwHash'] = None

        return dumps(game.__dict__, default=dict_decode), 200

    @app.get('/api/userContext')
    def userContext():
        user     = read_session(db)
        if not user:
            return render_template("Error.html", error="Authentication error"), 400

        username    = user.get('username')
        userRuntime = runtime(username, game.world)
        for val in userRuntime.keys():
            if callable(userRuntime[val]):
                userRuntime[val] = None

        return dumps(userRuntime, default=dict_decode), 200

    @app.post('/api/game/join')
    def joinGame():
        user     = read_session(db)
        tileName = request.form.get('tileName')

        if not user:
            return render_template("Error.html", error="Authentication error"), 400
        if not tileName:
            return render_template('Error.html', error="You must select a tile to join the game"), 400

        # Ensure user has no stations in the world
        userStations = game.world.findObjects(lambda x: x.objType == ObjectType.Station and x.owner == user["username"])
        if len(userStations) != 0:
            return render_template("Error.html", error="You cannot join the world with active stations"), 400

        # Find tile if exists
        tile = game.world.tiles.get(tileName)
        if not tile:
            return render_template("Error.html", error=f"Tile name {tileName} was not found"), 404

        # Make sure tile does not already have a station
        stationsInTile = game.world.findObjects(lambda x: x.position.tile == tile.name and x.objType == ObjectType.Station)
        if len(stationsInTile) != 0:
            return render_template("Error.html", error=f"Tile {tileName} must not contain another station"), 400

        # create station owned by player
        # TODO station create logic should be elsewhere
        station                     = Object(ObjectType.Station)
        station.owner               = user["username"]
        station.position            = Position(randint(0, tile.size), randint(0, tile.size), tile.name)
        station.storage.totalSpace  = 1000

        game.world.addObject(station)

        # create ship owned by player
        # TODO ship create logic should be handled elsewhere
        ship                    = Object(ObjectType.Ship)
        ship.owner              = user["username"]
        ship.position           = Position(station.position.x + 2, station.position.y + 2, tile.name)
        ship.storage.totalSpace = 100

        game.world.addObject(ship)

        logging.info(f'User {user["username"]} joined tile {tile.name}')

        return "Joined Game", 200