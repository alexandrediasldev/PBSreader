from  utils import *
class Species:
    def __init__(self, id,name,internalName,type1,type2,baseStats,genderRate,baseEXP, moves, height, pokedex, evolutions):
        self.id: str = id
        self.name: str = name
        self.internalName: str = internalName
        self.type1: str = type1
        self.type2: str = type2
        self.baseStats: list[str] = baseStats
        self.genderRate:str = genderRate
        self.baseEXP:str  = baseEXP
        self.moves: list[str] = moves
        self.height:str  = height
        self.evolutions:str  = evolutions
        self.pokedex:str  = pokedex
    def print(self):
        textList = ["Id:", "Name:","Internal Name:", "Type1:", "Type2:","Base Stats:","Gender Rate:",
                    "Base EXP:", "Moves:", "Height:", "Evolutions:", "Pokedex:"]
        attributeList = [self.id, self.name, self.internalName, self.type1, self.type2, self.baseStats,
                         self.genderRate, self.baseEXP, self.moves, self.height, self.evolutions, self.pokedex]
        for i in range(len(attributeList)):
            printIfValue(textList[i],attributeList[i])

