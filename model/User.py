from dataclasses import dataclass

@dataclass
class User:
    username    : str       # Ingame name
    pwHash      : str       # Hashed Password