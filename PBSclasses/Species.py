from dataclasses import dataclass
from typing import Tuple

from PBSclasses.BaseData import BaseData
from PBSclasses.SpeciesStats import SpeciesStats


@dataclass
class Species(BaseData):
    id: str
    name: str
    internal_name: str
    type1: str
    base_stats: SpeciesStats
    gender_rate: str
    base_EXP: str
    moves: list[Tuple[str, str]]
    height: str
    pokedex: str
    evolutions: str
    type2: str = ""
    incense: str = ""
