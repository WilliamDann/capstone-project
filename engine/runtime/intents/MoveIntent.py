from dataclasses                import dataclass
from model.Components.Position  import Position

@dataclass
class MoveIntent:
    objId       : str
    newPosition : Position

    def __run(self):
        # User scripts will not have a valid world global
        global world
        if not world:
            raise Exception("No World Context found")

        # TODO bounds checking

        # Update the position
        world.objects[self.objId].position = self.newPosition