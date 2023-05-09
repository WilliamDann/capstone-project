from dataclasses                import dataclass
from model.Components.Position  import Position

@dataclass
class MoveIntent:
    objId       : str
    newPosition : Position

    def __run(self):
        global world
        if not world:
            raise Exception("No World Context found")

        # Update the position
        world.objects[self.objId].position = self.newPosition