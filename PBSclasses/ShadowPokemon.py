from dataclasses import dataclass, field

from PBSclasses.BaseData import BaseData
from PBSclasses.Species import Species


@dataclass
class ShadowPokemon(BaseData):
    species: Species
    move_list: list[str] = field(default_factory=list)

    # version v15
    @classmethod
    def get_attr_pbs_names(cls):
        return ["Species", "MoveList"]
