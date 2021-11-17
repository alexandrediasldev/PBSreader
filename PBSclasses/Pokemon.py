from PBSclasses.BaseData import BaseData
from PBSclasses.Item import Item
from PBSclasses.Move import Move
from PBSclasses.Species import Species


class Pokemon(BaseData):
    species: Species
    level: str
    held_item: Item
    move_list: list[Move]
    ability: str
    form: str
    gender: str
    shininess: str
    nature: str
    ivs: str
    hapiness: str
    nickname: str
    shadow: str
    ball_type: str

    def __init__(
        self,
        species,
        level,
        held_item="",
        move_list=[],
        ability="",
        form="0",
        gender="",
        shininess="false",
        nature="",
        ivs="10",
        hapiness="70",
        nickname="",
        shadow="",
        ball_type="",
    ):
        self.species = species
        self.level = level
        self.held_item = held_item
        self.move_list = move_list
        self.ability = ability
        self.form = form
        self.gender = gender
        self.shininess = shininess
        self.nature = nature
        self.ivs = ivs
        self.hapiness = hapiness
        self.nickname = nickname
        self.shadow = shadow
        self.ball_type = ball_type

    def to_trainer_entry_bulbapedia(self) -> str:
        species_id = ""
        if self.species.id < 100:
            species_id = "0"
        species_id += str(self.species.id)
        trainer_entry = species_id + "|" + self.species.name + "|"
        if self.gender == "":
            trainer_entry += "Both"

        trainer_entry += self.gender + "|" + self.level + "||"

        if self.held_item != "":
            trainer_entry += self.held_item.name

        trainer_entry += "|" + self.ability + "|"
        if self.move_list:
            for i in range(len(self.move_list)):
                trainer_entry += self.move_list[i].name + "|"
        else:
            trainer_entry += "||||"

        return trainer_entry
