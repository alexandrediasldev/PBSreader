from utils import *


class Move:

    def __init__(self, id_number, id, name, function_code, base_power, type, damage_category,
                 accuracy, total_pp, additional_effect_chance, target, priority, flags, description):
        self.name: str = name
        self.accuracy: str = accuracy
        self.description: str = description
        self.flags: str = flags
        self.priority: str = priority
        self.target: str = target
        self.additionalEffectChance: str = additional_effect_chance
        self.totalPP: str = total_pp
        self.damageCategory: str = damage_category
        self.type: str = type
        self.basePower: str = base_power
        self.id: str = id
        self.idNumber: str = id_number
        self.functionCode: str = function_code

    def print(self):
        text_list = ["ID number:", "ID:", "Name:", "Function code:", "Base Power:", "Type:", "Damage category:",
                     "Accuracy:",
                     "Total PP:", "Additional effect chance:", "Target:", "Priority:", "Flags:", "Description:"]
        attribute_list = [self.idNumber, self.id, self.name, self.functionCode, self.basePower, self.type,
                          self.damageCategory,
                          self.accuracy, self.totalPP, self.additionalEffectChance, self.target, self.priority,
                          self.flags,
                          self.description]
        for i in range(len(attribute_list)):
            print_if_value(text_list[i], attribute_list[i])
