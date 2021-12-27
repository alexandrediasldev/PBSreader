from dataclasses import dataclass

from PBSclasses.BaseData import BaseData


@dataclass
class Item(BaseData):
    id_number: str = ""
    id: str = ""
    name: str = ""
    name_plural: str = ""
    pocket: str = ""
    price: str = ""
    description: str = ""
    usability_out_battle: str = ""
    usability_in_battle: str = ""
    special_items: str = ""
    move_name: str = ""

    # version v15
    @classmethod
    def get_attr_pbs_names(cls):
        return [
            "IdNumber",
            "Id",
            "Name",
            "NamePlural",
            "Pocket",
            "Price",
            "Description",
            "UsabilityOutBattle",
            "UsabilityInBattle",
            "SpecialItems",
            "MoveName",
        ]
