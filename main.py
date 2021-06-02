import itertools

import Visualization
from Parser import *
import FileLoader
from PBSclasses.EncounterMethod import *
from matplotlib import pyplot as plt
if __name__ == '__main__':

    csvTrainer = FileLoader.FileCsvTolist('PBS/trainers.txt')
    csvTrainerType = FileLoader.FileCsvTolist('PBS/trainertypes.txt')
    csvMove = FileLoader.FileCsvTolist('PBS/moves.txt')
    csvItem = FileLoader.FileCsvTolist('PBS/items.txt')
    csvEncounter = FileLoader.FileCsvTolist('PBS/encounters.txt')
    equalPokemonSpecies = FileLoader.FileEqualToList('PBS/pokemon.txt')

    trainerTypeList = parseTrainerTypes(csvTrainerType)
    speciesList = parsePokemon(equalPokemonSpecies)
    moveList = parserMove(csvMove)
    itemList = parseItem(csvItem)
    trainerList = parseTrainerList(csvTrainer, trainerTypeList, speciesList, moveList, itemList)
    defaultEncounterMethodList = getDefaultEncounterMethodList()
    encounterList = parseEncounter(csvEncounter, defaultEncounterMethodList, speciesList)


    mapNames = []
    d_name = dict()
    d_type = dict()
    for e in encounterList:
        mapName = e.mapIdNumber[6:]
        if(mapName not in d_name):
            d_name[mapName] = []
            d_type[mapName] = []
            mapNames.append(mapName)
        if (e.pokemonSpecies.name not in d_name[mapName]):
            d_type[mapName].append(e.pokemonSpecies.type1)
            if(e.pokemonSpecies.type2 != ""):
                d_type[mapName].append(e.pokemonSpecies.type2)
            d_name[mapName].append(e.pokemonSpecies.name)


    l1 = 8
    l2 = 7
    f, ax=plt.subplots(l1,l2)
    f.set_size_inches(20,20)
    print(len(mapNames))

    k = 0
    for i,j in itertools.product(range(l1), range(l2)):
        if(k < len(mapNames)):
            ax = Visualization.addTypeBar(d_type[mapNames[k]], f,ax,(i,j),areaName=mapNames[k])
        else:
            ax[i, j].set_axis_off()

        k += 1

    f.tight_layout()
    f.show()
    #f.savefig("types_map_small.png")
    #Visualization.showTypeBar(typeMapEncounters[12])
    # for d in defaultEncounterMethodList:
    #    d.print()
    # with open('TrainerTemplatePBS.txt', 'w') as reader:
    #    for t in trainerList:
    #        reader.write(t.toTrainerEntryBulbapedia()+'\n')
    # for s in trainerList:
    #    print(s.toTrainerEntryBulbapedia())
    # for m in moveList:
    #    m.print()
