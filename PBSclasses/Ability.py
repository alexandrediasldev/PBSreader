from dataclasses import dataclass

from PBSclasses.BaseData import BaseData


@dataclass
class AbilityV15(BaseData):
    id_number: str
    id: str
    name: str
    description: str
