from dataclasses  import dataclass
from model.Object import ObjectType
from model.World  import World
from logging      import info, error

@dataclass
class AttackIntent:
    attackerId  : str
    attackeeId  : str

    def run(self, world: World):
        info(world.objects)

        attacker = world.objects[self.attackerId]
        attackee = world.objects[self.attackeeId]

        if not attacker or not attackee:
            error('Invalid attacker or attackee')
            error(attacker)
            error(attackee)
            return

        if attacker.position.tile != attackee.position.tile:
            error(f'Invalid attack intent, on different tiles: {attacker.position.tile} vs {attackee.position.tile}')
            return
        if attacker.position.dist(attackee.position) > 5:
            error(f'Invalid attack intent, distance too great')
            return
        if (attacker.objType != ObjectType.Ship):
            error(f'Invalid attack intent, wrong type for attacker')
            return

        info(f'Attack intent executed {self.attackerId} to {self.attackeeId} for {10} damage')
        world.objects[self.attackeeId].health -= 10
        if (world.objects[self.attackeeId].health <= 0):
            info(f'Object {self.attackeeId} died as a result of the attack intent.')
            del world.objects[self.attackeeId]