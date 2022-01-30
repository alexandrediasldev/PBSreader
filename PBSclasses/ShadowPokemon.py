from dataclasses import dataclass, field

from PBSclasses.BaseData import BaseData
from PBSclasses.Species import Species


@dataclass
class ShadowPokemon(BaseData):
    species: str
    move_list: list[str] = field(default_factory=list)
