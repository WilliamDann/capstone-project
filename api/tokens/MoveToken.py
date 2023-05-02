from api.tokens.Token           import Token
from model.Object               import Object
from model.Components.Position  import Position

class MoveToken(Token):
    def __init__(self, obj: Object, target: "Position|Object") -> None:
        super().__init__()

    def validate(self) -> bool:
        # Ensure that 'to' is a Position
        if isinstance(to, Object):
            to = to.position
        if not isinstance(to, Position):
            return False

        # Ensure that 'obj' has move parts
        # TODO parts need to be implemented

        return True 

    def action(self):
        # TODO move speed based on body parts
        moveSpeed = 1
        pass