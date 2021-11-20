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
    type2: str = ""
    base_stats: SpeciesStats = SpeciesStats("1", "1", "1", "1", "1", "1")
    gender_rate: str = ""
    growth_rate: str = ""
    base_EXP: str = ""
    effort_points: SpeciesStats = SpeciesStats("0", "0", "0", "0", "0", "0")
    rareness: str = ""
    happiness: str = ""
    abilities: list[str] = field(default_factory=list)
    moves: list[Tuple[str, str]] = field(default_factory=list)
    egg_moves: list[str] = field(default_factory=list)
    compatibility: list[str] = field(default_factory=list)
    steps_to_hatch: str = ""
    height: str = ""
    weight: str = ""
    color: str = ""
    habitat: str = ""
    kind: str = ""
    pokedex: str = ""
    battler_player_y: str = ""
    battler_enemy_y: str = ""
    battler_altitude: str = ""
    evolutions: SpeciesEvolution = None
    incense: str = ""
