from dataclasses import dataclass, field
from typing import List

from PBSclasses.BaseData import BaseData
from PBSclasses.EncounterMethod import EncounterMethod
from PBSclasses.Species import SpeciesV15


@dataclass
class EncounterPokemonV15(BaseData):
    pokemon_species: str = ""
    level_low: str = ""
    level_high: str = ""


@dataclass
class EncounterByMethodV15(BaseData):
    encounter_method: str = ""
    pokemon_list: List[EncounterPokemonV15] = field(default_factory=list)


@dataclass
class EncounterV15(BaseData):
    map_id_number: str
    encounter_densities: List[str]
    encounters: List[EncounterByMethodV15]


@dataclass
class EncounterPokemonV19(BaseData):
    encounter_chance: str = ""
    pokemon_species: str = ""
    level_low: str = ""
    level_high: str = ""


@dataclass
class EncounterByMethodV19(BaseData):
    encounter_method: str = ""
    encounter_density: str = ""
    pokemon_list: List[EncounterPokemonV15] = field(default_factory=list)


@dataclass
class EncounterV19(BaseData):
    map_id_number: str
    version_number: str
    encounters: List[EncounterByMethodV15]
