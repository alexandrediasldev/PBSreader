from dataclasses import dataclass

from PBSclasses.BaseData import BaseData


@dataclass
class SpeciesEvolution(BaseData):
    name: str = ""
    method: str = ""
    evolution_parameter: str = ""
