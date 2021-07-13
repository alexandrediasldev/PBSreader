from utils import print_if_value


class SpeciesStats:
    def __init__(self, hp, attack, defense, speed, special_attack, special_defense):
        self.hp: str = hp
        self.attack: str = attack
        self.defense: str = defense
        self.speed: str = speed
        self.specialAttack: str = special_attack
        self.specialDefense: str = special_defense
    def print(self):
        text_list = ["Hp:", "Attack:","Defense:", "Speed:", "Special attack:","Special Defense:"]
        attribute_list = [self.hp, self.attack, self.defense, self.speed, self.specialAttack, self.specialDefense]

        for i in range(len(attribute_list)):
            print(text_list[i],attribute_list[i]," ",end="")
        print()
