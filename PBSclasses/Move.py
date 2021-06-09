from utils import *


class Move:

    def __init__(self, idNumber, id, name, functionCode, basePower, type, damageCategory,
                 accuracy, totalPP, additionalEffectChance, target, priority, flags, description):
        self.name: str = name
        self.accuracy: str = accuracy
        self.description: str = description
        self.flags: str = flags
        self.priority: str = priority
        self.target: str = target
        self.additionalEffectChance: str = additionalEffectChance
        self.totalPP: str = totalPP
        self.damageCategory: str = damageCategory
        self.type: str = type
        self.basePower: str = basePower
        self.id: str = id
        self.idNumber: str = idNumber
        self.functionCode: str = functionCode

    def print(self):
        textList = ["ID number:", "ID:", "Name:", "Function code:", "Base Power:", "Type:", "Damage category:",
                    "Accuracy:",
                    "Total PP:", "Additional effect chance:", "Target:", "Priority:", "Flags:", "Description:"]
        attributeList = [self.idNumber, self.id, self.name, self.functionCode, self.basePower, self.type,
                         self.damageCategory,
                         self.accuracy, self.totalPP, self.additionalEffectChance, self.target, self.priority,
                         self.flags,
                         self.description]
        for i in range(len(attributeList)):
            printIfValue(textList[i], attributeList[i])
