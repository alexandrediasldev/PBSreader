from dataclasses import dataclass, field
from typing import List

from PBSclasses.BaseData import BaseData


@dataclass
class TownPoint(BaseData):
    position_x: str = ""
    position_y: str = ""
    name: str = ""
    point_of_interest: str = ""
    fly_destination_id: str = ""
    fly_destiation_x: str = ""
    fly_destiation_y: str = ""
    switch: str = ""


@dataclass
class TownMap(BaseData):
    id: str = ""
    name: str = ""
    filename: str = ""
    points: List[TownPoint] = field(default_factory=TownPoint)

    # version v15
    @classmethod
    def get_attr_pbs_names(cls):
        return ["Id", "Name", "Filename", "Points"]
