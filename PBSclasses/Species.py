from typing import Tuple

from PBSclasses.BaseData import BaseData
from PBSclasses.SpeciesStats import SpeciesStats


class Species(BaseData):
    def __init__(
        self,
        id,
        name,
        internal_name,
        type1,
        type2,
        base_stats,
        gender_rate,
        base_exp,
        moves,
        height,
        pokedex,
        evolutions,
    ):
        self.name: str = name
        self.internal_name: str = internal_name
        self.id: str = id
        self.type1: str = type1
        self.type2: str = type2
        self.base_stats: SpeciesStats = base_stats
        self.gender_rate: str = gender_rate
        self.base_exp: str = base_exp
        self.moves: list[Tuple[str, str]] = moves
        self.height: str = height
        self.evolutions: list[str] = evolutions
        self.pokedex: str = pokedex
