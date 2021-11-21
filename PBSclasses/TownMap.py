from dataclasses import dataclass

from PBSclasses.BaseData import BaseData


@dataclass
class TownMap(BaseData):
    id: str = ""
    name: str = ""
    filename: str = ""
    points: str = ""


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
