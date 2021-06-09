def printIfValue(text,value):
    if(value != ""):
        print(text, value)

def findSizesOfSubplots(numberOfPlot):
    i = 0
    j = 0
    while i * j < numberOfPlot:
        if (i < j):
            i += 1
        else:
            j += 1
    return i, j


def getDictsEncountersNameType(encounterList, skipNumber=False):
    mapNames = []
    d_name, d_type = dict(), dict()
    for e in encounterList:
        if(skipNumber):
            mapName = e.mapIdNumber[6:]
        else:
            mapName = e.mapIdNumber

        if (mapName not in d_name):
            d_name[mapName], d_type[mapName] = [], []
            mapNames.append(mapName)
        if (e.pokemonSpecies.name not in d_name[mapName]):
            d_type[mapName].append(e.pokemonSpecies.type1)
            if (e.pokemonSpecies.type2 != ""):
                d_type[mapName].append(e.pokemonSpecies.type2)
            d_name[mapName].append(e.pokemonSpecies.name)

    return d_name, d_type, mapNames