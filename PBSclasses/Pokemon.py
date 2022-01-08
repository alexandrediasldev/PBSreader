from dataclasses import dataclass, field

from PBSclasses.BaseData import BaseData
from PBSclasses.Item import Item
from PBSclasses.Move import Move
from PBSclasses.Species import Species


@dataclass
class Pokemon(BaseData):
    species: str = ""
    level: str = ""
    held_item: str = ""
    move_list: list[str] = field(default_factory=list)
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

    def to_trainer_entry_bulbapedia(self) -> str:
        species_id = ""
        if int(self.species) < 100:
            species_id = "0"
        species_id += str(self.species)
        trainer_entry = species_id + "|" + self.species + "|"
        if self.gender == "":
            trainer_entry += "Both"

        trainer_entry += self.gender + "|" + self.level + "||"

        if self.held_item != "":
            trainer_entry += self.held_item

        trainer_entry += "|" + self.ability + "|"
        if self.move_list:
            for i in range(len(self.move_list)):
                trainer_entry += self.move_list[i] + "|"
        else:
            trainer_entry += "||||"

        return trainer_entry
