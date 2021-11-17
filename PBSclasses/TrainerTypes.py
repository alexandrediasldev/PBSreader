from PBSclasses.BaseData import BaseData


class TrainerType(BaseData):
    def __init__(
        self, id_number, id, name, base_money, battle_bgm, victory_me, intro_me, gender, skill_level
    ):
        self.id_number: str = id_number
        self.id: str = id
        self.name: str = name
        self.base_money: str = base_money
        self.battle_bgm: str = battle_bgm
        self.victory_me: str = victory_me
        self.intro_me: str = intro_me
        self.gender: str = gender
        self.skill_level: str = skill_level

    def to_trainer_entry_bulbapedia(self) -> str:
        return self.id + ".png" + "|" + self.name
