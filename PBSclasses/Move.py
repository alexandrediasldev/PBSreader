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
        self.additional_effect_chance: str = additional_effect_chance
        self.total_pp: str = total_pp
        self.damage_category: str = damage_category
        self.type: str = type
        self.base_power: str = base_power
        self.id: str = id
        self.id_number: str = id_number
        self.function_code: str = function_code

    def print(self)->None:
        text_list = ["ID number:", "ID:", "Name:", "Function code:", "Base Power:", "Type:", "Damage category:",
                     "Accuracy:",
                     "Total PP:", "Additional effect chance:", "Target:", "Priority:", "Flags:", "Description:"]
        attribute_list = [self.id_number, self.id, self.name, self.function_code, self.base_power, self.type,
                          self.damage_category,
                          self.accuracy, self.total_pp, self.additional_effect_chance, self.target, self.priority,
                          self.flags,
                          self.description]
        for i in range(len(attribute_list)):
            print_if_value(text_list[i], attribute_list[i])
