from dataclasses import dataclass, field
from typing import List

from PBSclasses.BaseData import BaseData
from PBSclasses.Species import Species


@dataclass
class ShadowPokemon(BaseData):
    species: str
    move_list: List[str] = field(default_factory=list)
