from model.Components.Position          import Position
from engine.runtime.intents.MoveIntent  import MoveIntent
from logging import debug

def move(obj, to: Position, intents: list):
    # TODO custom move speed
    dx = 1
    dy = 1
    if to['x'] < obj['position'].x:
        dx = -dx
    if to['y'] < obj['position'].y:
        dy = -dy

    pos = Position(obj['position'].x + dx, obj['position'].y + dy, obj['position'].tile)
    intents.append(MoveIntent(
        objId           = obj['objId'],
        newPosition     = pos
    ))