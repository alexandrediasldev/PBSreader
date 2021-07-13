from PBSclasses.EncounterMethod import EncounterMethod
from PBSclasses.Species import Species
from utils import *


class Encounter:
    
    def __init__(self, map_id_number, encounter_densities, encounter_method, pokemon_species, level_low, level_high):
        self.mapIdNumber: str = map_id_number
        self.encounterDensities: list[str] = encounter_densities
        self.encounterMethod: EncounterMethod = encounter_method
        self.levelLow: str = level_low
        self.pokemonSpecies: Species = pokemon_species
        self.levelHigh: str = level_high

    def print(self)->None:
        print_if_value("Map id number:", self.mapIdNumber)
        print_if_value("Encounter density:", self.encounterDensities)
        self.encounterMethod.print()
        print_if_value("Pokemon name:",self.pokemonSpecies.name)
        print_if_value("Level low:", self.levelLow)
        print_if_value("Level high:", self.levelHigh)
