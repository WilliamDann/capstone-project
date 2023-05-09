from model.User             import User
from model.World            import World

from engine.runtime.runtime import runtime
from logging                import info, debug

def runner(user: User, world: World):
    if not user.userCode:
        return

    info(f"Started script '{user.username}'")
    userRuntime = runtime(user.username, world)
    try:
        exec(user.userCode,
            {"__builtins__": None},
            userRuntime,
        )

        for intent in userRuntime.intents:
            debug(intent)
    except Exception as e:
        pass

    info(f"Finished script '{user.username}'")