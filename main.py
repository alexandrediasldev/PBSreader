from Parser import *
import FileLoader
from PBSclasses.EncounterMethod import *





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
    encounterList = parseEncounter(csvEncounter, defaultEncounterMethodList)
    for e in encounterList:
        e.print()
    #for d in defaultEncounterMethodList:
    #    d.print()
    #with open('TrainerTemplatePBS.txt', 'w') as reader:
    #    for t in trainerList:
    #        reader.write(t.toTrainerEntryBulbapedia()+'\n')
    for s in trainerList:
        print(s.toTrainerEntryBulbapedia())
    #for m in moveList:
    #    m.print()

