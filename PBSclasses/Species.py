from dataclasses import dataclass, field
from typing import Tuple, List

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
    base_stats: SpeciesStats = field(default_factory=SpeciesStats)
    gender_rate: str = ""
    growth_rate: str = ""
    base_EXP: str = ""
    effort_points: SpeciesStats = field(default_factory=SpeciesStats)
    rareness: str = ""
    happiness: str = ""
    abilities: List[str] = field(default_factory=list)
    moves: List[Tuple[str, str]] = field(default_factory=list)
    egg_moves: List[str] = field(default_factory=list)
    compatibility: List[str] = field(default_factory=list)
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
    evolutions: SpeciesEvolution = field(default_factory=SpeciesEvolution)
    incense: str = ""

    @classmethod
    def get_attr_pbs_names(cls):
        return [
            "Id",
            "Name",
            "InternalName",
            "Type1",
            "Type2",
            "BaseStats",
            "GenderRate",
            "GrowthRate",
            "BaseEXP",
            "EffortPoints",
            "Rareness",
            "Happiness",
            "Abilities",
            "Moves",
            "EggMoves",
            "Compatibility",
            "StepsToHatch",
            "Height",
            "Weight",
            "Color",
            "Habitat",
            "Kind",
            "Pokedex",
            "BattlerPlayerY",
            "BattlerEnemyY",
            "BattlerAltitude",
            "Evolutions",
            "Incense",
        ]
