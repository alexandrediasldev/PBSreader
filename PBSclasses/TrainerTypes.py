from utils import *


class TrainerType:
    def __init__(self, id_number, id, name, base_money, battle_bgm, victory_me, intro_me, gender, skill_level):
        self.id_number: str = id_number
        self.id: str = id
        self.name: str = name
        self.base_money: str = base_money
        self.battle_bgm: str = battle_bgm
        self.victory_me: str = victory_me
        self.intro_me: str = intro_me
        self.gender: str = gender
        self.skillLevel: str = skill_level

    def print(self) -> None:
        text_list = ["Number:", "Id:", "Name:", "Base Money:", "Battle BGM:", "Victory ME:",
                    "Intro ME:", "Gender:", "Skill level:"]
        attribute_list = [self.id_number, self.id, self.name, self.base_money, self.battle_bgm,
                          self.victory_me, self.intro_me, self.gender, self.skillLevel]
        for i in range(len(attribute_list)):
            print_if_value(text_list[i], attribute_list[i])


    def to_trainer_entry_bulbapedia(self) -> str:
        return self.id + ".png" + "|" + self.name

