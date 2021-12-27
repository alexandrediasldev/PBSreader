from dataclasses import dataclass
from typing import List

from PBSclasses.BaseData import BaseData


@dataclass
class Phone(BaseData):
    greetings: List[str]
    greetings_morning: List[str]
    greetings_evening: List[str]
    bodies1: List[str]
    bodies2: List[str]
    generics: List[str]
    battle_requests: List[str]

    # version v15
    @classmethod
    def get_attr_pbs_names(cls):
        return [
            "Greetings",
            "GreetingsMorning",
            "GreetingsEvening",
            "Bodies1",
            "Bodies2",
            "Generics",
            "BattleRequests",
        ]
