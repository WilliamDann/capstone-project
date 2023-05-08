from model.Components.Position  import Position
from model.Components.Storage   import Storage
from enum                       import Enum

class ProcessManufactureType(Enum):
    IceProcessor            = 'IceProcessor',       #ice -> water
    PlasmaProcessor         = 'PlasmaProcessor',    #plasma -> basicFuel and exoticFuel
    OrganicsProcessor       = 'OrganicsProcessor'   #organics -> polymers
    ElectManufactory        = 'ElectManufactory',   #electronics
    GenManufactory          = 'GenManufactory',     #power generators
    PrefabManufactory       = 'PrefabManufactory'   #building materials

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

    def process(self, processorType: str, type: Storage.ResourceType, quantity: int) -> int:
    #check ResourceType is processable
        if processorType == 'PlasmaProcessor' and (type != 'Plasma' or self.storage.count(type) == 0):
            return -4   #return code: not right process
        if processorType == 'IceProcessor' and (type != 'Ice' or self.storage.count(type) == 0):
            return -4   #return code: not right process
        if processorType == 'OrganicsProcessor' and (type != 'Organics' or self.storage.count(type) == 0):
            return -4   #return code: not right process
        
    #check quantity of ResourceType is available in storage
        if Storage.store[type] < quantity:
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

def manufacture(self, manufactoryType: str, type1: Storage.ResourceType, type2: Storage.ResourceType, quantity: int):
    #check ResourceType can be used in manufacturing
        if manufactoryType == 'ElecManufactory' and \
            ((type1 != 'Polymer' or type2 != 'Polymer') or \
            (type1 != 'ElectroMetals' or type2 != 'ElectroMetals') or\
            self.storage.count(type1) == 0 or self.storage.count(type2) == 0):
            return -4   #return code: not right process
        if manufactoryType == 'GenManufactory' and \
            ((type1 != 'RareMetals' or type2 != 'RareMetals') or \
            (type1 != 'ExoticFuel' or type2 != 'ExoticFuel') or\
            self.storage.count(type1) == 0 or self.storage.count(type2) == 0):
            return -4   #return code: not right process
        if manufactoryType == 'PrefabManufactory' and \
            ((type1 != 'BaseMetals' or type2 != 'BaseMetals') or \
            (type1 != 'ScrapMetals' or type2 != 'ScrapMetals') or\
            self.storage.count(type1) == 0 or self.storage.count(type2) == 0):
            return -4   #return code: not right process
        
    #check quantity of ResourceType is available in storage
        if Storage.store[type1] < quantity or Storage.store[type2] < quantity:
            return -2    #return code: resource missing
        
    #check there is a manufactory of correct type
        if Storage.store[manufactoryType] <= 0:
            return -2   #return code: resource missing

        if manufactoryType == 'ElecManufactory':
            Storage.withdraw('Polymer', quantity) 
            Storage.withdraw('ElectroMetals', quantity) 
            Storage.deposit('Electronics', quantity)  
            return 0    #return code: ok
        
        if manufactoryType == 'GenManufactory':
            Storage.withdraw('RareMetals', quantity)  
            Storage.withdraw('ExoticFuel', quantity)
            Storage.deposit('Generators', quantity)  
            return 0    #return code: ok
        
        if manufactoryType == 'PrefabManufactory':
            Storage.withdraw('BaseMetals', quantity)  
            Storage.withdraw('ScrapMetals', quantity)
            Storage.deposit('Prefab', quantity)  
            return 0    #return code: ok

