from dataclasses import dataclass

from PBSclasses.BaseData import BaseData


@dataclass
class Ability(BaseData):
    id_number: str
    id: str
    name: str
    description: str
