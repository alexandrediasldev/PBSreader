from dataclasses import dataclass

from PBSclasses.BaseData import BaseData
from PBSclasses.EncounterMethod import EncounterMethod
from PBSclasses.Species import Species


@dataclass
class Encounter(BaseData):
    map_id_number: str
    encounter_densities: list[str]
    encounter_method: EncounterMethod
    pokemon_species: Species
    level_low: str
    level_high: str
