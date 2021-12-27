from dataclasses import dataclass

from PBSclasses.BaseData import BaseData


@dataclass
class TrainerType(BaseData):
    id_number: str
    id: str
    name: str
    base_money: str
    battle_bgm: str
    victory_me: str
    intro_me: str
    gender: str
    skill_level: str

    # version v15
    @classmethod
    def get_attr_names(cls):
        return [
            "id_number",
            "id",
            "name",
            "base_money",
            "battle_bgm",
            "victory_me",
            "intro_me",
            "gender",
            "skill_level",
        ]

    @classmethod
    def get_attr_pbs_names(cls):
        return [
            "IdNumber",
            "Id",
            "Name",
            "BaseMoney",
            "BattleBgm",
            "VictoryMe",
            "IntroMe",
            "Gender",
            "SkillLevel",
        ]

    def to_trainer_entry_bulbapedia(self) -> str:
        return self.id + ".png" + "|" + self.name
