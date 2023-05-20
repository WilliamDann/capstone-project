from model.ProcMan                          import ProcManType
from engine.runtime.intents.ProcManIntent   import ProcManIntent
from logging import debug

def procMan(newProcMan: ProcManType, quant: int, intents: list):
    intents.append(ProcManIntent(
        newProcMan  = newProcMan,
        quantity    = quant
    ))