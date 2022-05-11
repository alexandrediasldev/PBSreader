from dataclasses import dataclass, field
from typing import List

from PBSclasses.BaseData import BaseData


@dataclass
class RibbonV19(BaseData):
    id_number: str = ""
    id: str = ""
    name: str = ""
    description: str = ""
