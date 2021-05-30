from utils import *


class TrainerType:
    def __init__(self, idNumber, id, name, baseMoney, battleBGM, victoryME, introME, gender, skillLevel):
        self.idNumber = idNumber
        self.id = id
        self.name = name
        self.baseMoney = baseMoney
        self.battleBGM = battleBGM
        self.victoryME = victoryME
        self.introME = introME
        self.gender = gender
        self.skillLevel = skillLevel

    def print(self):
        textList = ["Number:", "Id:", "Name:", "Base Money:", "Battle BGM:", "Victory ME:",
                    "Intro ME:", "Gender:", "Skill level:"]
        attributeList = [self.idNumber, self.id,self.name,self.baseMoney, self.battleBGM,
                         self.victoryME, self.introME, self.gender, self.skillLevel]
        for i in range(len(attributeList)):
            printIfValue(textList[i], attributeList[i])


    def toTrainerEntryBulbapedia(self):
        return self.id + ".png" + "|" + self.name

