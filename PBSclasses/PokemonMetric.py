from typing import List

from dataclasses import dataclass, field

from PBSclasses.BaseData import BaseData


@dataclass
class PokemonMetricV20(BaseData):
    id: str = ""
    form: str = ""
    back_sprite: List[str] = field(default_factory=list)
    front_sprite: List[str] = field(default_factory=list)
    front_sprite_altitude: str = ""
    shadow_x: str = ""
    shadow_size: str = ""
