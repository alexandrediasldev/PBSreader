from utils import *


class TrainerType:
    def __init__(self, idNumber, id, name, baseMoney, battleBGM, victoryME, introME, gender, skillLevel):
        self.idNumber: str = idNumber
        self.id: str = id
        self.name: str = name
        self.baseMoney: str = baseMoney
        self.battleBGM: str = battleBGM
        self.victoryME: str = victoryME
        self.introME: str = introME
        self.gender: str = gender
        self.skillLevel: str = skillLevel

    def print(self):
        textList = ["Number:", "Id:", "Name:", "Base Money:", "Battle BGM:", "Victory ME:",
                    "Intro ME:", "Gender:", "Skill level:"]
        attributeList = [self.idNumber, self.id,self.name,self.baseMoney, self.battleBGM,
                         self.victoryME, self.introME, self.gender, self.skillLevel]
        for i in range(len(attributeList)):
            printIfValue(textList[i], attributeList[i])


    def toTrainerEntryBulbapedia(self):
        return self.id + ".png" + "|" + self.name

