from dataclasses import dataclass
from typing import List

from PBSclasses.BaseData import BaseData


@dataclass
class PhoneV15(BaseData):
    greetings: List[str]
    greetings_morning: List[str]
    greetings_evening: List[str]
    bodies1: List[str]
    bodies2: List[str]
    generics: List[str]
    battle_requests: List[str]
