from dataclasses import dataclass, field
from typing import List

from PBSclasses.BaseData import BaseData


@dataclass
class ItemV15(BaseData):
    id_number: str = ""
    id: str = ""
    name: str = ""
    pocket: str = ""
    price: str = ""
    description: str = ""
    usability_out_battle: str = ""
    usability_in_battle: str = ""
    special_items: str = ""
    move_name: str = ""


@dataclass
class ItemV16(BaseData):
    id_number: str = ""
    id: str = ""
    name: str = ""
    name_plural: str = ""
    pocket: str = ""
    price: str = ""
    description: str = ""
    usability_out_battle: str = ""
    usability_in_battle: str = ""
    special_items: str = ""
    move_name: str = ""


@dataclass
class ItemV20(BaseData):
    id: str = ""
    name: str = ""
    name_plural: str = ""
    pocket: str = ""
    price: str = ""
    sell_price: str = ""
    field_use: str = ""
    battle_use: str = ""
    consumable: str = ""
    flags: List[str] = field(default_factory=list)
    move: str = ""
    description: str = ""
