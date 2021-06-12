from utils import printIfValue


class SpeciesStats:
    def __init__(self, hp, attack, defense, speed, specialAttack, specialDefense):
        self.hp: str = hp
        self.attack: str = attack
        self.defense: str = defense
        self.speed: str = speed
        self.specialAttack: str = specialAttack
        self.specialDefense: str = specialDefense
    def print(self):
        textList = ["Hp:", "Attack:","Defense:", "Speed:", "Special attack:","Special Defense:"]
        attributeList = [self.hp, self.attack, self.defense, self.speed, self.specialAttack, self.specialDefense]

        for i in range(len(attributeList)):
            print(textList[i],attributeList[i]," ",end="")
        print()
