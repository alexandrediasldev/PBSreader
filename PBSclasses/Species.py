from dataclasses import dataclass
from typing import Tuple

from PBSclasses.BaseData import BaseData
from PBSclasses.SpeciesStats import SpeciesStats


@dataclass
class Species(BaseData):
    Id: str
    Name: str
    InternalName: str
    Type1: str
    BaseStats: SpeciesStats
    GenderRate: str
    BaseEXP: str
    Moves: list[Tuple[str, str]]
    Height: str
    Pokedex: str
    Evolutions: str
    Type2: str = ""
    Incense: str = ""
