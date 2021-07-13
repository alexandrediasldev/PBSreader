from PBSclasses import Item
from PBSclasses.Species import Species
from PBSclasses.Move import Move
from typing import List
from utils import *
from Finder import *


class Pokemon:
    species: Species
    level: str
    held_item: Item
    move_list: list[Move]
    ability: str
    form: str
    gender: str
    shininess: str
    nature: str
    i_vs: str
    hapiness: str
    nickname: str
    shadow: str
    ball_type: str

    def __init__(self, species, level, held_item, move_list, ability, form, gender, shininess, nature, i_vs, hapiness,
                 nickname, shadow, ball_type):
        self.species = species
        self.level = level
        self.held_item = held_item
        self.move_list = move_list
        self.ability = ability
        self.form = form
        self.gender = gender
        self.shininess = shininess
        self.nature = nature
        self.i_vs = i_vs
        self.hapiness = hapiness
        self.nickname = nickname
        self.shadow = shadow
        self.ball_type = ball_type

    def print(self)->None:
        text_list = ["Species:", "Level:", "Held item:", "Move list:", "Ability:", "Gender:", "Form:", "Shininess:",
                     "Nature:", "IVs:", "Hapiness:", "Nickname:", "Shadow:", "Ball Type:"]
        attribute_list = [self.species, self.level, self.held_item, self.move_list, self.ability, self.gender,
                          self.form,
                          self.shininess, self.nature, self.i_vs, self.hapiness, self.nickname, self.shadow,
                          self.ball_type]
        for i in range(len(attribute_list)):
            if (text_list[i] == "Species:" or text_list[i] == "Held item:"):
                if (attribute_list[i] != ""):
                    print_if_value(text_list[i], attribute_list[i].name)
            elif (text_list[i] == "Move list:"):
                for j, m in enumerate(attribute_list[i]):
                    print_if_value("Move " + str(j + 1) + ":", m.name)
            else:
                print_if_value(text_list[i], attribute_list[i])

    def to_trainer_entry_bulbapedia(self) -> str:
        species_id = ""
        if (self.species.id < 100):
            species_id = "0"
        species_id += str(self.species.id)
        trainer_entry = species_id + "|" + self.species.name + "|"
        if (self.gender == ""):
            trainer_entry += "Both"

        trainer_entry += self.gender + "|" + self.level + "||"

        if (self.held_item != ""):
            trainer_entry += self.held_item.name

        trainer_entry += "|" + self.ability + "|"
        if (self.move_list):
            for i in range(len(self.move_list)):
                trainer_entry += self.move_list[i].name + "|"
        else:
            trainer_entry += "||||"

        return trainer_entry
