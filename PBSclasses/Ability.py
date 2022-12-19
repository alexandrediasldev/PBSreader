from dataclasses import dataclass, field
from typing import List

from PBSclasses.BaseData import BaseData


@dataclass
class AbilityV15(BaseData):
    id_number: str = ""
    id: str = ""
    name: str = ""
    description: str = ""


@dataclass
class AbilityV20(BaseData):
    id: str = ""
    name: str = ""
    flags: List[str] = field(default_factory=list)
    description: str = ""
