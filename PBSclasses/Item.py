from PBSclasses.BaseData import BaseData


class Item(BaseData):
    def __init__(
        self,
        id_number,
        id,
        name,
        name_plural,
        pocket,
        price,
        description,
        usability_out_battle,
        usability_in_battle,
        special_items,
        move_name,
    ):
        self.description: str = description
        self.price: str = price
        self.pocket: str = pocket
        self.name_plural: str = name_plural
        self.name: str = name
        self.id: str = id
        self.id_number: str = id_number
        self.usability_out_battle: str = usability_out_battle
        self.usability_in_battle: str = usability_in_battle
        self.special_items: str = special_items
        self.move_name: str = move_name
