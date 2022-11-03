from dataclasses import dataclass
from typing import List

from PBSclasses.BaseData import BaseData


@dataclass
class MoveV15(BaseData):
    id_number: str
    id: str
    name: str
    function_code: str
    base_power: str
    type: str
    damage_category: str
    accuracy: str
    total_pp: str
    additional_effect_chance: str
    target: str
    priority: str
    flags: str
    description: str


@dataclass
class MoveV20(BaseData):
    id: str
    name: str
    type: str
    category: str
    base_damage: str
    accuracy: str
    total_PP: str
    target: str
    priority: str
    function_code: str
    flags: List[str]
    effect_chance: str
    description: str
