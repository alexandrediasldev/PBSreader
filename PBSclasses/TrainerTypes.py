from dataclasses import dataclass

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
