from dataclasses import dataclass, field
from typing import Tuple

from PBSclasses.BaseData import BaseData
from PBSclasses.SpeciesEvolution import SpeciesEvolution
from PBSclasses.SpeciesStats import SpeciesStats


@dataclass
class Species(BaseData):
    id: str = ""
    name: str = ""
    internal_name: str = ""
    type1: str = ""
    base_stats: SpeciesStats = SpeciesStats(1, 1, 1, 1, 1, 1)
    gender_rate: str = ""
    base_EXP: str = ""
    moves: list[Tuple[str, str]] = field(default_factory=list)
    height: str = ""
    pokedex: str = ""
    evolutions: SpeciesEvolution = None
    type2: str = ""
    incense: str = ""
