from enum import Enum

class ResourceType(Enum):
    Credits         = 'Credits',        #money from trade
    BaseMetals      = 'BaseMetals',     #asteroid, mining
    ElectroMetals   = 'ElectroMetals'   #asteroid, mining
    RareMetals      = 'RareMetals',     #asteroid, mining
    BasicFuel       = 'BasicFuel',      #planet, or processed from Plasma
    ExoticFuel      = 'ExoticFuel',     #processed from Plasma
    Food            = 'Food',           #planet
    FarmResources   = 'FarmResources',  #planet
    Water           = 'Water',          #planet
    AlienFossils    = 'AlienFossils',   #planet, dead planet, dead station, for research
    AlienTech       = 'AlienTech',      #planet, dead planet, dead station, for research
    AlienResearch   = 'AlienResearch',  #recover research stored on dead station
    Organics        = 'Organics',       #comet, planet, requires processing -> polymers for electronics
    Ice             = 'Ice',            #comet, requires processing -> water
    SolidGases      = 'SolidGases',     #comet (ie methane, ammonia; process to organics)
    Plasma          = 'Plasma',         #star
    ScrapMetal      = 'ScrapMetal',     #dead planet
    Radioactives    = 'Radioactives',   #dead planet
    Components      = 'Components',     #station, manufacturing: components for computers, electronics
    Electronics     = 'Electronics',    #station, manufacturing
    ShipUpgrades    = 'ShipUpgrades',   #station (trade only)
    Generators      = 'Generators',     #station, manufacturing: power generation for ships, bases
    BldgMaterials   = 'BldgMaterials'   #station, manufacturing

   


class Storage:
    store       : "dict[ResourceType, int]"

    usedSpace   : int
    totalSpace  : int

    def __init__(self, totalSpace: int) -> None:
        self.totalSpace = totalSpace
        self.store      = {}

    def withdraw(self, type: ResourceType, n: int) -> bool:
        if self.usedSpace+n > self.totalSpace:
            return False

        if self.store.get(type) is None:
            self.store[type] = 0
        self.store[type] += n

        self.usedSpace += n
        return True

    def deopsit(self, type: ResourceType, n: int) -> bool:
        if self.store.get(type) is None:
            return False
        if self.store.get(type)-n < 0:
            return False

        self.store[type] -= n
        self.usedSpace   -= n

        return True
