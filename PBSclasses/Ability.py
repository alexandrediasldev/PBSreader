from dataclasses import dataclass

from PBSclasses.BaseData import BaseData


@dataclass
class Ability(BaseData):
    id_number: str
    id: str
    name: str
    description: str

    # version v15
    @classmethod
    def get_attr_pbs_names(cls):
        return ["IdNumber", "Id", "Name", "Description"]
