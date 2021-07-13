from utils import print_if_value


class SpeciesStats:
    def __init__(self, hp, attack, defense, speed, special_attack, special_defense):
        self.hp: str = hp
        self.attack: str = attack
        self.defense: str = defense
        self.speed: str = speed
        self.special_attack: str = special_attack
        self.special_defense: str = special_defense
    def print(self)->None:
        text_list = ["Hp:", "Attack:","Defense:", "Speed:", "Special attack:","Special Defense:"]
        attribute_list = [self.hp, self.attack, self.defense, self.speed, self.special_attack, self.special_defense]

        for i in range(len(attribute_list)):
            print(text_list[i],attribute_list[i]," ",end="")
        print()
