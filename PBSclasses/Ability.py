from PBSclasses.BaseData import BaseData


class Ability(BaseData):
    def __init__(self, id_number, id, name, description):
        self.description: str = description
        self.name: str = name
        self.id: str = id
        self.id_number: str = id_number
