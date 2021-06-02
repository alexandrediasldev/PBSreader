import Exception as ex


def getSpeciesFromName(name, speciesList):
    if (name == ""):
        return ""
    for s in speciesList:
        if (name == s.internalName):
            return s
    raise ex.UnknownPBSName(name + " not found in species list")


def getItemFromName(name, itemList):
    if (name == ""):
        return ""
    for item in itemList:
        if (item.id == name):
            return item
    raise ex.UnknownPBSName(name + " not found in item list")


def getMoveFromName(name, moveList):
    if (name == ""):
        return ""
    for m in moveList:
        if (m.id == name):
            return m
    raise ex.UnknownPBSName(name + " not found in move list")

def getEncounterMethodFromName(name, encounterMethodList):
    if(name == ""):
        return ""
    for m in encounterMethodList:
        if (m.methodName == name):
            return m
    return ""
def getTrainerTypeFromName(name, trainerTypeList):
    if(name == ""):
        return ""
    for t in trainerTypeList:
        if (t.id == name):
            return t

    raise ex.UnknownPBSName(name + " not found in trainer type list")
