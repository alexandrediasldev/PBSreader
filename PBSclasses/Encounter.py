from PBSclasses.EncounterMethod import EncounterMethod
from PBSclasses.Species import Species
from utils import *


class Encounter:
    
    def __init__(self, map_id_number, encounter_densities, encounter_method, pokemon_species, level_low, level_high):
        self.map_id_number: str = map_id_number
        self.encounter_densities: list[str] = encounter_densities
        self.encounter_method: EncounterMethod = encounter_method
        self.level_low: str = level_low
        self.pokemon_species: Species = pokemon_species
        self.level_high: str = level_high

    def print(self)->None:
        print_if_value("Map id number:", self.map_id_number)
        print_if_value("Encounter density:", self.encounter_densities)
        self.encounter_method.print()
        print_if_value("Pokemon name:", self.pokemon_species.name)
        print_if_value("Level low:", self.level_low)
        print_if_value("Level high:", self.level_high)
