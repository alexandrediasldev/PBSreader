from dataclasses import dataclass, field

from PBSclasses.BaseData import BaseData
from PBSclasses.Item import Item
from PBSclasses.Move import Move
from PBSclasses.Species import Species


@dataclass
class Pokemon(BaseData):
    species: Species
    level: str
    held_item: Item = None
    move_list: list[Move] = field(default_factory=list)
    ability: str = ""
    form: str = ""
    gender: str = ""
    shininess: str = ""
    nature: str = ""
    ivs: str = ""
    hapiness: str = ""
    nickname: str = ""
    shadow: str = ""
    ball_type: str = ""

    # version v15
    @classmethod
    def get_attr_pbs_names(cls):
        return [
            "Species",
            "Level",
            "HeldItem",
            "MoveList",
            "Ability",
            "Form",
            "Gender",
            "Shininess",
            "Nature",
            "Ivs",
            "Hapiness",
            "Nickname",
            "Shadow",
            "BallType",
        ]

    def to_trainer_entry_bulbapedia(self) -> str:
        species_id = ""
        if int(self.species.id) < 100:
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
