from dataclasses import dataclass, field
from typing import List

from PBSclasses.BaseData import BaseData


@dataclass
class TrainerPokemonV15(BaseData):
    species: str = ""
    level: str = ""
    held_item: str = ""
    move_list: List[str] = field(default_factory=list)
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
