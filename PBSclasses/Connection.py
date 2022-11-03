from dataclasses import dataclass

from PBSclasses.BaseData import BaseData


@dataclass
class ConnectionV15(BaseData):
    first_id_number: str
    first_edge: str
    first_point: str
    second_id_number: str
    second_edge: str
    second_point: str
