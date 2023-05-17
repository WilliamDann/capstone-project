from dataclasses                import dataclass
from model.Components.Position  import Position
from logging                    import info

@dataclass
class MoveIntent:
    objId       : str
    newPosition : Position

    def run(self, world):
        # TODO bounds checking

        # Boundaries
        min_x = 1
        max_x = 1
        min_y = 1
        max_y = 1

        cur_x = 0
        cur_y = 0

        for obj in world.objects:
            if obj == self.objId:
                cur_x = obj.position.x

        # Perform bounds checking
        if self.newPosition.x < self.objId.positon.x + max_x or self.newPosition.x > self.objId.position.x - min_x:
            info(f'Error: X-coordinate out of bounds for object {self.objId}')
            return

        if self.newPosition.y < min_y or self.newPosition.y > max_y:
            info(f'Error: Y-coordinate out of bounds for object {self.objId}')
            return
    
        # Update the position
        info(f'Move intent executed {self.objId} to {self.newPosition}')
        world.objects[self.objId].position = self.newPosition