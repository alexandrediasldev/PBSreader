from PBSclasses.BaseData import BaseData


class SpeciesStats(BaseData):
    def __init__(self, hp, attack, defense, speed, special_attack, special_defense):
        self.hp: str = hp
        self.attack: str = attack
        self.defense: str = defense
        self.speed: str = speed
        self.special_attack: str = special_attack
        self.special_defense: str = special_defense
