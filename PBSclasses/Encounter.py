from dataclasses import dataclass, field
from typing import List

from PBSclasses.BaseData import BaseData
from PBSclasses.EncounterMethod import EncounterMethod
from PBSclasses.Species import Species


@dataclass
class EncounterPokemon(BaseData):
    pokemon_species: str = ""
    level_low: str = ""
    level_high: str = ""


@dataclass
class EncounterByMethod(BaseData):
    encounter_method: str = ""
    pokemon_list: List[EncounterPokemon] = field(default_factory=list)


@dataclass
class EncounterByMap(BaseData):
    map_id_number: str
    encounter_densities: List[str]
    encounters: List[EncounterByMethod]
