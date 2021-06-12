import PBSclasses.Trainers as tr
import PBSclasses.Pokemon as pk
import PBSclasses.TrainerTypes as tp
import PBSclasses.Species as sp
import PBSclasses.Move as mv
import PBSclasses.Item as it
import PBSclasses.Encounter as en
from Finder import *
import PBSclasses.Environment as env
from PBSclasses.SpeciesEvolution import SpeciesEvolution
from PBSclasses.SpeciesStats import SpeciesStats


def parseItem(csvOutput, hasPluralName=False):
    itemList = []
    for line in csvOutput:
        moveName = ""
        line.append("")
        if (hasPluralName):
            item = it.Item(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8],
                           line[9], line[10])
        else:
            item = it.Item(line[0], line[1], line[2], "", line[3], line[4], line[5], line[6], line[7], line[8],
                           line[9])
        itemList.append(item)

    return itemList


def parseEncounter(csvOutput, encounterMethods, environment):

    encounterList = []
    l = len(csvOutput)
    i = 0
    while i < l:
        line = csvOutput[i]
        if (len(line) == 1):
            isMapName = True
            methodTmp = getEncounterMethodFromName(line[0], encounterMethods)
            if (methodTmp != ""):
                method = methodTmp
                isMapName = False

            if (isMapName):
                mapName = line[0]
                i += 1
                if (i < l):
                    line = csvOutput[i]
                    if (len(line) == 1):
                        encounterDensity = ['25', '10', '10']
                    else:
                        encounterDensity = line

        elif (len(line) == 2):
            species = getSpeciesFromName(line[0], environment.speciesList)
            levelLow = line[1]
            levelHigh = ""
            encounterList.append(en.Encounter(mapName, encounterDensity, method, species, levelLow, levelHigh))
        else:
            species = getSpeciesFromName(line[0], environment.speciesList)
            levelLow = line[1]
            levelHigh = line[2]
            encounterList.append(en.Encounter(mapName, encounterDensity, method, species, levelLow, levelHigh))
        i += 1

    return encounterList


def parserMove(csvOutput):
    movesList = []
    for line in csvOutput:
        move = mv.Move(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8],
                       line[9], line[10], line[11], line[12], line[13])
        movesList.append(move)

    return movesList


def parseTrainerTypes(csvOutput):
    trainerTypeList = []
    for line in csvOutput:
        idNumber, id, name, baseMoney, battleBGM, victoryME, introME, gender, skillLevel = \
            line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8]

        type = tp.TrainerType(idNumber, id, name, baseMoney, battleBGM, victoryME, introME, gender, skillLevel)
        trainerTypeList.append(type)
    return trainerTypeList


def parsePokemonMove(moves):
    movesAndLevel = moves.split(',')
    levelMoves = []
    for i in range(0,len(movesAndLevel),2):
        level = movesAndLevel[i]
        if(i+1< len(movesAndLevel)):
            move = movesAndLevel[i+1]
            levelMoves.append((level,move))
    return levelMoves



def parsePokemonBaseStats(baseStats):
    stats = baseStats.split(',')
    if(len(stats) < 5):
        return SpeciesStats(1,1,1,1,1,1)

    return SpeciesStats(stats[0],stats[1],stats[2],stats[3],stats[4], stats[5])
def parsePokemonEvolution(evolution):
    evo = evolution.split(',')
    name = method = parameter = ""
    if(len(evo) >= 1):
        name = evo[0]
    if(len(evo) >= 2):
        method = evo[1]
    if (len(evo) >= 3):
        parameter = evo[2]

    return SpeciesEvolution(name,method,parameter)

def parsePokemon(equalOutput):
    id = -1
    speciesList = []
    for line in equalOutput:
        if (line[0].startswith('\ufeff')):
            line[0] = line[0][1:]
        first = line[0]
        if (len(line) > 1):
            second = line[1]
        if (first.startswith('[') and first.endswith(']')):
            if (id != -1):
                species = sp.Species(id, name, internalName, type1, type2, baseStats, genderRate, baseEXP, moves,
                                     height, pokedex, evolutions)

                speciesList.append(species)
                id = name = internalName = type1 = type2 = baseStats = genderRate \
                    = baseEXP = moves = height = pokedex = evolutions = ""

            id = int(first[1:-1])

        elif (first == "Name"):
            name = second
        elif (first == "InternalName"):
            internalName = second
        elif (first == "Type1"):
            type1 = second
        elif (first == "Type2"):
            type2 = second
        elif (first == "BaseStats"):
            baseStats = parsePokemonBaseStats(second)
        elif (first == "GenderRate"):
            genderRate = second
        elif (first == "BaseEXP"):
            baseEXP = second
        elif (first == "Moves"):
            moves = parsePokemonMove(second)
        elif (first == "Height"):
            height = second
        elif (first == "Pokedex"):
            pokedex = second
        elif (first == "Evolutions"):
            evolutions = parsePokemonEvolution(second)

    species = sp.Species(id, name, internalName, type1, type2, baseStats, genderRate, baseEXP, moves, height, pokedex,
                         evolutions)
    speciesList.append(species)
    return speciesList

def parseTrainerPokemon(pokemonAttributes, environment):
        species = level = heldItem = moveList = ability = \
            gender = form = shininess = nature = IVs = hapiness = \
            nickname = shadow = ballType = ""
        for i in range(len(pokemonAttributes)):
            attribute = pokemonAttributes[i]
            if (i == 0):
                species = getSpeciesFromName(attribute, environment.speciesList)
            elif (i == 1):
                level = attribute
            elif (i == 2):
                heldItem = getItemFromName(attribute, environment.itemList)
            elif (i == 3):
                moveList = []
                for i in range(3, 7):
                    if (i >= len(pokemonAttributes)):
                        break
                    moveName = pokemonAttributes[i]
                    if (moveName != ""):
                        moveList.append(getMoveFromName(moveName, environment.moveList))
            elif (i == 7):
                ability = attribute
            elif (i == 8):
                gender = attribute
            elif (i == 9):
                form = attribute
            elif (i == 10):
                shininess = attribute
            elif (i == 11):
                nature = attribute
            elif (i == 12):
                IVs = attribute
            elif (i == 13):
                hapiness = attribute
            elif (i == 14):
                nickname = attribute
            elif (i == 15):
                shadow = attribute
            elif (i == 16):
                ballType = attribute
        return pk.Pokemon(species,level,heldItem,moveList,ability,form,gender,
                          shininess,nature,IVs,hapiness,nickname,shadow,ballType)

def parseTrainerList(csvOutput, environment):
    lineNum = 0
    pokemonList = []
    trainerList = []
    for line in csvOutput:
        if (lineNum == 0):
            type = line[0]
        elif (lineNum == 1):
            name = line[0]
        elif (lineNum == 2):
            nbPokemon = int(line[0])
        else:
            if (nbPokemon + 2 == lineNum):
                pkm = parseTrainerPokemon(line, environment)
                pokemonList.append(pkm)

                trainerType = getTrainerTypeFromName(type, environment.trainerTypeList)
                train = tr.Trainer(trainerType, name, nbPokemon, pokemonList)
                trainerList.append(train)

                pokemonList = []
                lineNum = -1
            else:
                pkm = parseTrainerPokemon(line, environment)
                pokemonList.append(pkm)
        lineNum += 1
    return trainerList
