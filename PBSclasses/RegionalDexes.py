from dataclasses import field
from typing import List

from attr import dataclass

from PBSclasses.BaseData import BaseData


@dataclass
class RegionalDexV19(BaseData):
    regional_dex_number: str = ""
    pokemon_list: List[str] = field(default_factory=list)
