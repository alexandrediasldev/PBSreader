from PBSclasses.EncounterMethod import EncounterMethod
from PBSclasses.Species import Species
from utils import *


class Encounter:
    
    def __init__(self, mapIdNumber, encounterDensities, encounterMethod, pokemonSpecies, levelLow, levelHigh):
        self.mapIdNumber: str = mapIdNumber
        self.encounterDensities: list[str] = encounterDensities
        self.encounterMethod: EncounterMethod = encounterMethod
        self.levelLow: str = levelLow
        self.pokemonSpecies: Species = pokemonSpecies
        self.levelHigh: str = levelHigh

    def print(self):
        printIfValue("Map id number:", self.mapIdNumber)
        printIfValue("Encounter density:", self.encounterDensities)
        self.encounterMethod.print()
        printIfValue("Pokemon name:",self.pokemonSpecies.name)
        printIfValue("Level low:", self.levelLow)
        printIfValue("Level high:", self.levelHigh)
