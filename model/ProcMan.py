from model.Components.Position  import Position
from model.Components.Storage   import Storage, ResourceType
from enum                       import Enum

class ProcManType(Enum):
    IceProc         = 'IceProc',        #Ice Processor: ice -> water
    PlasmaProc      = 'PlasmaProc',     #Plasma Processor: plasma -> basicFuel and exoticFuel
    OrganProc       = 'OrganProc'       #Organics Processor: organics -> polymers
    ElectMan        = 'ElectMan',       #Electronics Manufactory
    GenMan          = 'GenMan',         #Power Generator Manufactory
    PrefabMan       = 'PrefabMan'       #Building Materials (Prefab) Manufactory

class ProcMan:
    objId       : str
    objType     : ProcManType

    position    : Position
    storage     : Storage

    owner       : "str|None"

    inputs_outputs = {
        ProcManType.IceProc: {
            'inputs': {
                ResourceType.Ice: 1
            },
            'outputs': {
                ResourceType.Water: 1
            }
        },
        ProcManType.PlasmaProc: {
            'inputs': {
                ResourceType.Plasma: 10
            },
            'outputs': {
                ResourceType.BasicFuel: 9,
                ResourceType.ExoticFuel: 1
            }
        },
        ProcManType.OrganProc: {
            'inputs': {
                ResourceType.Organics: 1
            },
            'outputs': {
                ResourceType.Polymer: 1
            }
        },
        ProcManType.ElectMan: {
            'inputs': {
                ResourceType.Polymer: 1,
                ResourceType.ElectroMetals: 1
            },
            'outputs': {
                ResourceType.Electronics: 1
            }
        },
        ProcManType.GenMan: {
            'inputs': {
                ResourceType.RareMetals: 5,
                ResourceType.ExoticFuel: 3,
                ResourceType.BaseMetals: 10,
                ResourceType.Electronics: 1
            },
            'outputs': {
                ResourceType.Generators: 1
            }
        },
        ProcManType.PrefabMan: {
            'inputs': {
                ResourceType.BaseMetals: 1,
                ResourceType.ScrapMetals: 1
            },
            'outputs': {
                ResourceType.Prefab: 1
            }
        }
    }    

    def __init__(self, objType: ProcManType) -> None:
        self.objType  = objType
        self.position = Position(0, 0, None)
        self.storage  = Storage(0)
        self.owner    = None
        self.objId    = None

    def procMan(procManType: ProcManType, quantity: int) -> int:

        recipe_quantity: int = 0    # pulled for each input or output item from inputs_outputs

        # Check if the procManType is valid
        if procManType not in ProcMan.inputs_outputs:
            #TODO: send a message to the log that the requested procManType is not valid
            return -4  # Return code: invalid process

        # Check if there is a processor of the correct type
        if Storage.store[procManType] <= 0:
            #TODO: send a message to the log that the processor/manufactory is missing
            return -2  # Return code: resource missing

        # Check if the required quantity of ResourceType(s) is available in storage
        # have to check all input quantities first, before removing anything from storage 
        for item in ProcMan.inputs_outputs.get(procManType, {}).get('inputs', {}):
            recipe_quantity = ProcMan.inputs_outputs.get(procManType, {}).get('inputs', {}).get(item, 0)
            if Storage.store[item] < quantity * recipe_quantity:
                #TODO: send a message to the log exactly which resource is missing enough quantity
                return -2  # Return code: resource missing

        # Can now process resources based on the procManType: first inputs then outputs    
        for item in ProcMan.inputs_outputs.get(procManType, {}).get('inputs', {}):
            recipe_quantity = ProcMan.inputs_outputs.get(procManType, {}).get('inputs', {}).get(item, 0)
            Storage.withdraw(item, quantity * recipe_quantity)
        for item in ProcMan.inputs_outputs.get(procManType, {}).get('outputs', {}):
            recipe_quantity = ProcMan.inputs_outputs.get(procManType, {}).get('outputs', {}).get(item, 0)   
            Storage.deposit(item, quantity * recipe_quantity)
        return 0  # Return code: OK
