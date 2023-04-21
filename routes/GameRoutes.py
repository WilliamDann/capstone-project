import logging
from flask                      import render_template, request
from flask.app                  import Flask
from pymongo.database           import Database
from model.Components.Position  import Position
from model.Objects.Station      import Station
from model.Objects.Ship         import Ship
from Game                       import Game
from random                     import randint
from json                       import dumps

from read_session import read_session

def dict_decode(inst):
    logging.debug(inst.__dict__)
    return inst.__dict__

def GameRoutes(app: Flask, db: Database, game: Game):
    @app.get('/play')
    def playPage():
        return render_template('Play.html', game=dumps(game.__dict__, default=dict_decode))

    @app.get('/api/game/')
    def getGame():
        return dumps(game.__dict__, default=dict_decode), 200

    @app.post('/api/game/join')
    def joinGame():
        user     = read_session(db)
        tileName = request.form.get('tileName')

        if not user:
            return render_template("Error.html", error="Authentication error"), 400
        if not tileName:
            return render_template('Error.html', error="You must select a tile to join the game"), 400

        # Ensure user has no stations in the world
        userStations = game.world.findObjects(lambda x: type(x) == Station and x.owner == user["username"])
        if len(userStations) != 0:
            return render_template("Error.html", error="You cannot join the world with active stations"), 400

        # Find tile if exists
        tile = game.world.tiles.get(tileName)
        if not tile:
            return render_template("Error.html", error=f"Tile name {tileName} was not found"), 404

        # Make sure tile does not already have a station
        stationsInTile = game.world.findObjects(lambda x: x.position.tile == tile.name and type(x) == Station)
        if len(stationsInTile) != 0:
            return render_template("Error.html", error=f"Tile {tileName} must not contain another station"), 400

        # create station owned by player
        # TODO station create logic should be elsewhere
        station                     = Station()
        station.owner               = user["username"]
        station.position            = Position(randint(0, tile.size), randint(0, tile.size), tile.name)
        station.storage.totalSpace  = 1000

        game.world.addObject(station)

        # create ship owned by player
        # TODO ship create logic should be handled elsewhere
        ship                    = Ship()
        ship.owner              = user["username"]
        ship.position           = Position(station.position.x + 2, station.position.y + 2, tile.name)
        ship.storage.totalSpace = 100

        game.world.addObject(ship)

        logging.info(f'User {user["username"]} joined tile {tile.name}')

        return "Joined Game", 200