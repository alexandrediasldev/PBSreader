from dataclasses import dataclass

from PBSclasses.BaseData import BaseData


@dataclass
class Move(BaseData):
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
