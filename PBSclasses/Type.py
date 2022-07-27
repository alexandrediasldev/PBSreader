from dataclasses import dataclass, field
from typing import List

from PBSclasses.BaseData import BaseData


@dataclass
class TypeV15(BaseData):
    id: str = ""
    name: str = ""
    internal_name: str = ""
    is_special_type: str = ""
    is_pseudo_type: str = ""
    weaknesses: List[str] = field(default_factory=list)
    resistances: List[str] = field(default_factory=list)
    immunities: List[str] = field(default_factory=list)


@dataclass
class TypeV20(BaseData):
    id: str = ""
    name: str = ""
    icon_position: str = ""
    is_special_type: str = ""
    is_pseudo_type: str = ""
    flags: List[str] = field(default_factory=list)
    weaknesses: List[str] = field(default_factory=list)
    resistances: List[str] = field(default_factory=list)
    immunities: List[str] = field(default_factory=list)
