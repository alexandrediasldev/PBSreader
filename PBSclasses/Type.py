from dataclasses import dataclass, field
from typing import List

from PBSclasses.BaseData import BaseData


@dataclass
class Type(BaseData):
    id: str = ""
    name: str = ""
    internal_name: str = ""
    is_special_type: str = ""
    weaknesses: List[str] = field(default_factory=list)
    resistances: List[str] = field(default_factory=list)
    immunities: List[str] = field(default_factory=list)
