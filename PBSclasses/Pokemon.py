from dataclasses import dataclass, field
from typing import List

from PBSclasses.BaseData import BaseData
from PBSclasses.Item import Item
from PBSclasses.Move import Move
from PBSclasses.Species import Species


@dataclass
class Pokemon(BaseData):
    pokemon: str = ""
    level: str = ""
    item: str = ""
    moves: List[str] = field(default_factory=list)
    ability: str = ""
    form: str = ""
    gender: str = ""
    shiny: str = ""
    nature: str = ""
    IV: str = ""
    hapiness: str = ""
    nickname: str = ""
    shadow: str = ""
    ball: str = ""
