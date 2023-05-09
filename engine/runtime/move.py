from model.Components.Position          import Position
from engine.runtime.intents.MoveIntent  import MoveIntent

def move(obj, to: Position):
    global intents

    # TODO custom move speed
    dx = 1
    dy = 1
    if to.x > obj.position.x:
        dx = -dx
    if to.y > obj.position.y:
        dy = -dy

    pos = Position(obj.position.x + dx, obj.position.y + dy)
    intents.push(MoveIntent(
        objId           = obj.id,
        newPosition     = pos
    ))