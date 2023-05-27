from engine.runtime.intents.AttackIntent import AttackIntent

def attack(attacker: str, attackee: str, intents: list):
    intents.append(AttackIntent(
        attackerId=attacker,
        attackeeId=attackee
    ))