from dataclasses import dataclass, field
from typing import List

from PBSclasses.BaseData import BaseData


@dataclass
class TrainerTypeV15(BaseData):
    id_number: str = ""
    id: str = ""
    name: str = ""
    base_money: str = ""
    battle_bgm: str = ""
    victory_me: str = ""
    intro_me: str = ""
    gender: str = ""
    skill_level: str = ""


@dataclass
class TrainerTypeV16(BaseData):
    id_number: str = ""
    id: str = ""
    name: str = ""
    base_money: str = ""
    battle_bgm: str = ""
    victory_me: str = ""
    intro_me: str = ""
    gender: str = ""
    skill_level: str = ""
    skill_codes: str = ""


@dataclass
class TrainerTypeV20(BaseData):
    id: str = ""
    name: str = ""
    gender: str = ""
    base_money: str = ""
    skill_level: str = ""
    flags: List[str] = field(default_factory=list)
    battle_BGM: str = ""
    victory_BGM: str = ""
    intro_BGM: str = ""
