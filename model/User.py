from dataclasses import dataclass

@dataclass
class User:
    username    : str       # Ingame name
    pwHash      : str       # Hashed Password

    userCode    : str       # User's script to be executed every game tick