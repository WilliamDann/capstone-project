from dataclasses                import dataclass
from model.Components.Position  import Position
from model.World                import World
from logging                    import info

@dataclass
class MoveIntent:
    objId       : str
    newPosition : Position

    def run(self, world: World):

        # Perform bounds checking
        obj = world.objects[self.objId]
        if abs(obj.position.x - self.newPosition.x) > 1:
            info(f'Error: X-coordinate out of bounds for object {self.objId}')
            return

        if abs(obj.position.y - self.newPosition.y) > 1:
            info(f'Error: Y-coordinate out of bounds for object {self.objId}')
            return
    
        # Update the position
        info(f'Move intent executed {self.objId} to {self.newPosition}')
        world.objects[self.objId].position = self.newPosition