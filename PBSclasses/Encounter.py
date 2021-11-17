from PBSclasses.BaseData import BaseData
from PBSclasses.EncounterMethod import EncounterMethod
from PBSclasses.Species import Species


class Encounter(BaseData):
    def __init__(
        self,
        map_id_number,
        encounter_densities,
        encounter_method,
        pokemon_species,
        level_low,
        level_high,
    ):
        self.map_id_number: str = map_id_number
        self.encounter_densities: list[str] = encounter_densities
        self.encounter_method: EncounterMethod = encounter_method
        self.level_low: str = level_low
        self.level_high: str = level_high
        self.pokemon_species: Species = pokemon_species
