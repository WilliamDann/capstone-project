import logging
from flask              import render_template, request
from flask.app          import Flask
from pymongo.database   import Database
from model.Components.Position import Position
from model.Objects.Station import Station
from model.Objects.Ship    import Ship
from Game               import Game
from random             import randint

from read_session import read_session


def GameRoutes(app: Flask, db: Database, game: Game):
    @app.get('/api/game/tile')
    def getTile():
        pass

    @app.post('/api/game/join')
    def joinGame():
        user     = read_session(db)
        logging.debug(user)
        tileName = request.form.get('tileName')

        if not user:
            return render_template("Error.html", error="Authentication error"), 400
        if not tileName:
            return render_template('Error.html', error="You must select a tile to join the game"), 400

        # Ensure user has no stations in the world
        userStations = filter(lambda x: type(x) == Station and x.owner == user["username"], game.world.objects.values())
        if len(list(userStations)) != 0:
            return render_template("Error.html", error="You cannot join the world with active stations"), 400

        # Find tile if exists
        tile = game.world.tiles.get(tileName)
        if not tile:
            return render_template("Error.html", error=f"Tile name {tileName} was not found"), 404

        # Make sure tile does not already have a station
        stationsInTile = filter(lambda x: x.position.tile == tile.name and type(x) == Station, game.world.objects.values())
        if len(list(stationsInTile)) != 0:
            return render_template("Error.html", error=f"Tile {tileName} must not contain another station"), 400

        # create station owned by player
        station = Station()
        station.owner = user["username"]
        station.position = Position(randint(0, tile.size), randint(0, tile.size), tile.name)

        game.world.addObject(station)

        # create ship ownbed by player
        ship = Ship()
        ship.owner = user["username"]
        ship.position = Position(station.position.x + 2, station.position.y + 2, tile.name)

        game.world.addObject(ship)

        logging.info(f'User {user["username"]} joined tile {tile.name}')

        return "Joined Game", 200