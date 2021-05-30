import PBSclasses.Trainers as tr
import PBSclasses.Pokemon as pk
import PBSclasses.TrainerTypes as tp
import PBSclasses.Species as sp
import PBSclasses.Move as mv
import PBSclasses.Item as it


def parseItem(csvOutput, hasPluralName = False):
    itemList = []
    for line in csvOutput:
        moveName = ""
        line.append("")
        if(hasPluralName):
            item = it.Item(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8],
                       line[9],line[10])
        else:
            item = it.Item(line[0], line[1], line[2], "",line[3], line[4], line[5], line[6], line[7], line[8],
                       line[9])
        itemList.append(item)

    return itemList


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
        idNumber = line[0]
        id = line[1]
        name = line[2]
        baseMoney = line[3]
        battleBGM = line[4]
        victoryME = line[5]
        introME = line[6]
        gender = line[7]
        skillLevel = line[8]
        type = tp.TrainerType(idNumber, id, name, baseMoney, battleBGM, victoryME, introME, gender, skillLevel)
        trainerTypeList.append(type)
    return trainerTypeList


def parsePokemon(equalOutput):
    id = -1
    speciesList = []
    for line in equalOutput:
        first = line[0]
        if (len(line) > 1):
            second = line[1]
        if (first.startswith('[') and first.endswith(']')):
            if (id != -1):
                species = sp.Species(id, name, internalName, type1, type2, baseStats, genderRate, baseEXP, moves,
                                     height, pokedex, evolutions)
                speciesList.append(species)
                id = name = internalName = type1 = type2 = baseStats = genderRate = baseEXP = moves = height = pokedex = evolutions = ""

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
            baseStats = second
        elif (first == "GenderRate"):
            genderRate = second
        elif (first == "BaseEXP"):
            baseEXP = second
        elif (first == "Moves"):
            moves = second
        elif (first == "Height"):
            height = second
        elif (first == "Pokedex"):
            pokedex = second
        elif (first == "Evolutions"):
            evolutions = second

    species = sp.Species(id, name, internalName, type1, type2, baseStats, genderRate, baseEXP, moves, height, pokedex,
                         evolutions)
    speciesList.append(species)
    return speciesList


def parseTrainerList(csvOutput, trainerTypeList, speciesList, moveList, itemList):
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
                pkm = pk.Pokemon(line, speciesList, moveList, itemList)
                pokemonList.append(pkm)
                trainerType = ""
                for t in trainerTypeList:
                    if (t.id == type):
                        trainerType = t

                train = tr.Trainer(trainerType, name, nbPokemon, pokemonList)
                trainerList.append(train)

                pokemonList = []
                lineNum = -1
            else:
                pkm = pk.Pokemon(line, speciesList, moveList, itemList)
                pokemonList.append(pkm)
        lineNum += 1
    return trainerList
