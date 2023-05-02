from api.ReturnCode import ReturnCode

class Token:
    f     : function    # the code to run
    args  : list        # The arguments to supply to the token

    def __init__(self, owner: str, args: list) -> None:
        self.owner = owner
        self.args  = args

    def run(self) -> ReturnCode:
        return self.f.__call__()