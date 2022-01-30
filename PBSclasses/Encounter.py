from dataclasses import dataclass

from PBSclasses.BaseData import BaseData
from PBSclasses.EncounterMethod import EncounterMethod
from PBSclasses.Species import Species


@dataclass
class Encounter(BaseData):
    encounter_chance: str = ""
    encounter_method: str = ""
    pokemon_species: str = ""
    level_low: str = ""
    level_high: str = ""


@dataclass
class MapEncounter(BaseData):
    map_id_number: str
    encounter_densities: list[str]
    encounters: list[Encounter]
