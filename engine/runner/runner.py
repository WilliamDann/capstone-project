from engine.runtime.runtime import runtime
from logging                import info, debug

def runner(user):
    if not user.userCode:
        return

    info(f"Started script '{user.username}'")
    userRuntime = runtime()
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