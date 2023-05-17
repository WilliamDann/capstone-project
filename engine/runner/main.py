from model.User             import User
from model.World            import World

from engine.runtime.runtime import runtime
from logging                import info, debug, error

def runner(user: User, world: World):
    if not user.get('userCode'):
        return

    info(f"Started script '{user.get('username')}'")
    userRuntime = runtime(user.get("username"), world)
    userGlobals = {"intents": [], "__builtins__": None}
    try:
        exec(user.get('userCode'),
            userGlobals,
            userRuntime,
        )

        for intent in userGlobals.get('intents'):
            intent.run(world)
    except Exception as e:
        error(str(e))

    info(f"Finished script '{user.get('username')}'")