from dataclasses                import dataclass
from model.ProcMan              import ProcManType
from logging                    import info

@dataclass
class ProcManIntent:
    objId       : str
    newProcMan  : ProcManType
    quant       : int

    def run(self, newProcMan: ProcManType, quant: int):

        # Issue intent to run ProcMan
    
        # Update the logs
        info(f'ProcMan Intent issued to process/manufacture quantity: {quant} of {newProcMan} type')

        # Check that process succeeded successfully
       