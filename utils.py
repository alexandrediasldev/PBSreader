from typing import Dict, List, Tuple
def printIfValue(text,value):
    if(value != ""):
        print(text, value)

def findSizesOfSubplots(numberOfPlot) -> Tuple[int,int]:
    i = 0
    j = 0
    while i * j < numberOfPlot:
        if (i < j):
            i += 1
        else:
            j += 1
    return i, j


def getDictsEncountersNameType(encounterList, skipNumber=False) -> Tuple[Dict[str,str],Dict[str,str],Dict[str,str]]:
    """

    :param encounterList: the list of wild pokemon encounters
    :param skipNumber: Skip the starting map number
    :return:
    """
    mapNames: List[str]= []
    d_name: Dict[str,str] = dict()
    d_type: Dict[str,str] = dict()
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