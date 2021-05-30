from  utils import *
class Species:
    def __init__(self, id,name,internalName,type1,type2,baseStats,genderRate,baseEXP, moves, height, pokedex, evolutions):
        self.id = id
        self.name = name
        self.internalName = internalName
        self.type1 = type1
        self.type2 = type2
        self.baseStats = baseStats
        self.genderRate = genderRate
        self.baseEXP = baseEXP
        self.moves = moves
        self.height = height
        self.evolutions = evolutions
        self.pokedex = pokedex
    def print(self):
        textList = ["Id:", "Name:","Internal Name:", "Type1:", "Type2:","Base Stats:","Gender Rate:",
                    "Base EXP:", "Moves:", "Height:", "Evolutions:", "Pokedex:"]
        attributeList = [self.id, self.name, self.internalName, self.type1, self.type2, self.baseStats,
                         self.genderRate, self.baseEXP, self.moves, self.height, self.evolutions, self.pokedex]
        for i in range(len(attributeList)):
            printIfValue(textList[i],attributeList[i])

