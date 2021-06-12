import itertools
from PBSclasses.Environment import Environment
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

    env = Environment()
    env.loadEnvironment(csvTrainerType,equalPokemonSpecies,csvMove,csvItem,csvTrainer,csvEncounter)
    env.speciesList[12].print()
    env.moveList[5].print()

    #f, ax = Visualization.plotAllEncounterMapTypes(env.encounterList)
    #f.show()
