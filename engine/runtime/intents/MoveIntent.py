from dataclasses                import dataclass
from model.Components.Position  import Position
from model.World                import World
from logging                    import info

@dataclass
class MoveIntent:
    objId       : str
    newPosition : Position

    def run(self, world: World):
        # TODO bounds checking

        # Update the position
        info(f'Move intent executed {self.objId} to {self.newPosition}')
        world.objects[self.objId].position = self.newPosition