from api.ReturnCode import ReturnCode

class Token:
    def __init__(self) -> None:
        pass

    # 'abstract' method to be overridden by token behavior
    def action(self) -> ReturnCode:
        return self.f.__call__()