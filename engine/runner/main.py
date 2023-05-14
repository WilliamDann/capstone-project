from model.User             import User
from model.World            import World

from engine.runtime.runtime import runtime
from logging                import info, debug

def runner(user: User, world: World):
    if not user.get('userCode'):
        return

    info(f"Started script '{user.get('username')}'")
    userRuntime = runtime(user.get("username"), world)
    try:
        exec(user.get('userCode'),
            {"__builtins__": None},
            userRuntime,
        )

        for intent in userRuntime.get('intents'):
            intent.__run(world)
    except Exception as e:
        pass

    info(f"Finished script '{user.get('username')}'")