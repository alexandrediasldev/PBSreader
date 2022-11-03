from dataclasses import dataclass, field
from typing import List

from PBSclasses.BaseData import BaseData


@dataclass
class RibbonV19(BaseData):
    id_number: str = ""
    id: str = ""
    name: str = ""
    description: str = ""


@dataclass
class RibbonV20(BaseData):
    id: str = ""
    name: str = ""
    icon_position: str = ""
    flags: List[str] = field(default_factory=list)
    description: str = ""
