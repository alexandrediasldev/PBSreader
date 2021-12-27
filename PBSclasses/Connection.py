from dataclasses import dataclass

from PBSclasses.BaseData import BaseData


@dataclass
class Connection(BaseData):
    first_id_number: str
    first_edge: str
    first_point: str
    second_id_number: str
    second_edge: str
    second_point: str

    # version v15
    @classmethod
    def get_attr_pbs_names(cls):
        return [
            "FirstIdNumber",
            "FirstEdge",
            "FirstPoint",
            "SecondIdNumber",
            "SecondEdge",
            "SecondPoint",
        ]
