from utils import  *
class Move:
    def __init__(self, idNumber, id, name, functionCode, basePower, type, damageCategory,
                 accuracy, totalPP, additionalEffectChance, target, priority, flags, description):
        self.name = name
        self.accuracy = accuracy
        self.description = description
        self.flags = flags
        self.priority = priority
        self.target = target
        self.additionalEffectChance = additionalEffectChance
        self.totalPP = totalPP
        self.damageCategory = damageCategory
        self.type = type
        self.basePower = basePower
        self.id = id
        self.idNumber = idNumber
        self.functionCode = functionCode

    def print(self):
        textList = ["ID number:", "ID:", "Name:", "Function code:", "Base Power:", "Type:", "Damage category:", "Accuracy:",
                    "Total PP:", "Additional effect chance:", "Target:", "Priority:", "Flags:", "Description:"]
        attributeList = [self.idNumber, self.id, self.name, self.functionCode, self.basePower, self.type, self.damageCategory,
                         self.accuracy, self.totalPP, self.additionalEffectChance, self.target, self.priority, self.flags,
                         self.description]
        for i in range(len(attributeList)):
                printIfValue(textList[i], attributeList[i])