from dataclasses import dataclass

from PBSclasses.BaseData import BaseData


@dataclass
class SpeciesStats(BaseData):
    hp: str = ""
    attack: str = ""
    defense: str = ""
    speed: str = ""
    special_attack: str = ""
    special_defense: str = ""
