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



    f, ax = Visualization.plotAllEncounterMapTypes(encounterList)
    f.show()


