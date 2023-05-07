from model.Components.Position  import Position
from model.Components.Storage   import Storage
from enum                       import Enum

class ProcessManufactureType(Enum):
    IceProcessor            = 'IceProcessor',
    PlasmaProcessor         = 'PlasmaProcessor',
    OrganicsProcessor       = 'OrganicsProcessor'
    CompManufacturer        = 'CompManufacturer',   #components
    ElectManufacturer       = 'ElectManufacturer',  #electronics
    GenManufacturer         = 'GenManufacturer',    #power generators
    BldgMatManufacturer     = 'BldgMatManufacturer' #building materials

class ProcessManufacture:
    objId       : str
    objType     : ProcessManufactureType

    position    : Position
    storage     : Storage

    owner       : "str|None"

    def __init__(self, objType: ProcessManufactureType) -> None:
        self.objType  = objType
        self.position = Position(0, 0, None)
        self.storage  = Storage(0)
        self.owner    = None
        self.objId    = None

    def process(self, processorType: str, type: Storage.ResourceType, quantity: int):
    #check ResourceType is processable
        if Storage.ResourceType != 'Plasma' and \
            Storage.ResourceType != 'Organics' and \
            Storage.ResourceType != 'Ice':
            return -4   #return code: not right process
        
    #check quantity of ResourceType is available in storage
        if Storage.store[Storage.ResourceType] < quantity:
            return -2    #return code: resource missing
        
    #check there is a processor of correct type
        if Storage.store[processorType] <= 0:
            return -2   #return code: resource missing

        if processorType == 'PlasmaProcessor':
            Storage.withdraw('Plasma', quantity)  
            Storage.deposit('BasicFuel', quantity)  
            Storage.deposit('ExoticFuel', quantity //12)
            return 0    #return code: ok
        
        if processorType == 'IceProcessor':
            Storage.withdraw('Ice', quantity)  
            Storage.deposit('Water', quantity)  
            return 0    #return code: ok
        
        if processorType == 'OrganicsProcessor':
            Storage.withdraw('Organics', quantity)  
            Storage.deposit('Polymer', quantity)  
            return 0    #return code: ok

