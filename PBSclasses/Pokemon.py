from dataclasses import dataclass, field

from PBSclasses.BaseData import BaseData
from PBSclasses.Item import Item
from PBSclasses.Move import Move
from PBSclasses.Species import Species


@dataclass
class Pokemon(BaseData):
    species: str = ""
    level: str = ""
    held_item: str = ""
    move_list: list[str] = field(default_factory=list)
    ability: str = ""
    gender: str = ""
    form: str = ""
    shininess: str = ""
    nature: str = ""
    ivs: str = ""
    hapiness: str = ""
    nickname: str = ""
    shadow: str = ""
    ball_type: str = ""
