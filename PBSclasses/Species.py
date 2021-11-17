from typing import Tuple

from PBSclasses.BaseData import BaseData
from PBSclasses.SpeciesStats import SpeciesStats


class Species(BaseData):
    def __init__(
        self,
        Id,
        Name,
        InternalName,
        Type1,
        BaseStats,
        GenderRate,
        BaseEXP,
        Moves,
        Height,
        Pokedex,
        Evolutions,
        Type2="",
        Incense="",
    ):
        self.name: str = Name
        self.internal_name: str = InternalName
        self.id: str = Id
        self.type1: str = Type1
        self.type2: str = Type2
        self.base_stats: SpeciesStats = BaseStats
        self.gender_rate: str = GenderRate
        self.base_exp: str = BaseEXP
        self.moves: list[Tuple[str, str]] = Moves
        self.height: str = Height
        self.evolutions: list[str] = Evolutions
        self.pokedex: str = Pokedex
