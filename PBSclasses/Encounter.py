from utils import *


class Encounter:
    def __init__(self, mapIdNumber, encounterDensities, encounterMethod, pokemonSpecies, levelLow, levelHigh):
        self.mapIdNumber = mapIdNumber
        self.encounterDensities = encounterDensities
        self.encounterMethod = encounterMethod
        self.levelLow = levelLow
        self.pokemonSpecies = pokemonSpecies
        self.levelHigh = levelHigh

    def print(self):
        printIfValue("Map id number:", self.mapIdNumber)
        printIfValue("Encounter density:", self.encounterDensities)
        self.encounterMethod.print()
        printIfValue("Pokemon Species:", self.pokemonSpecies)
        printIfValue("Level low:", self.levelLow)
        printIfValue("Level high:", self.levelHigh)
