from PBSclasses import Item
from PBSclasses.Species import Species
from PBSclasses.Move import Move
from utils import *
from Finder import *


class Pokemon:
    species: Species
    level: str
    heldItem: Item
    moveList: List[Move]
    ability: str
    form: str
    gender: str
    shininess: str
    nature: str
    IVs: str
    hapiness: str
    nickname: str
    shadow: str
    ballType: str

    def __init__(self, species, level, heldItem, moveList, ability, form, gender, shininess, nature, IVs, hapiness,
                 nickname, shadow, ballType):
        self.species = species
        self.level = level
        self.heldItem = heldItem
        self.moveList = moveList
        self.ability = ability
        self.form = form
        self.gender = gender
        self.shininess = shininess
        self.nature = nature
        self.IVs = IVs
        self.hapiness = hapiness
        self.nickname = nickname
        self.shadow = shadow
        self.ballType = ballType



    def print(self):
        textList = ["Species:", "Level:", "Held item:", "Move list:", "Ability:", "Gender:", "Form:", "Shininess:",
                    "Nature:", "IVs:", "Hapiness:", "Nickname:", "Shadow:", "Ball Type:"]
        attributeList = [self.species, self.level, self.heldItem, self.moveList, self.ability, self.gender, self.form,
                         self.shininess, self.nature, self.IVs, self.hapiness, self.nickname, self.shadow,
                         self.ballType]
        for i in range(len(attributeList)):
            if (textList[i] == "Species:" or textList[i] == "Held item:"):
                if (attributeList[i] != ""):
                    printIfValue(textList[i], attributeList[i].name)
            elif (textList[i] == "Move list:"):
                for j, m in enumerate(attributeList[i]):
                    printIfValue("Move " + str(j + 1) + ":", m.name)
            else:
                printIfValue(textList[i], attributeList[i])

    def toTrainerEntryBulbapedia(self) -> str:
        speciesId = ""
        if (self.species.id < 100):
            speciesId = "0"
        speciesId += str(self.species.id)
        trainerEntry = speciesId + "|" + self.species.name + "|"
        if (self.gender == ""):
            trainerEntry += "Both"

        trainerEntry += self.gender + "|" + self.level + "||"

        if (self.heldItem != ""):
            trainerEntry += self.heldItem.name

        trainerEntry += "|" + self.ability + "|"
        if (self.moveList):
            for i in range(len(self.moveList)):
                trainerEntry += self.moveList[i].name + "|"
        else:
            trainerEntry += "||||"

        return trainerEntry
