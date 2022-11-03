from dataclasses import dataclass, field
from typing import List

from PBSclasses.BaseData import BaseData


@dataclass
class TmV15(BaseData):
    move_name: str = ""
    pokemon_list: List[str] = field(default_factory=list)
