from utils import print_if_value


class Item:
    def __init__(self,id_number, id, name, name_plural, pocket,price, description,
                 usability_out_battle, usability_in_battle, special_items, move_name):
        self.description: str = description
        self.price: str = price
        self.pocket: str = pocket
        self.namePlural: str = name_plural
        self.name: str = name
        self.id: str = id
        self.idNumber: str = id_number
        self.usabilityOutBattle: str = usability_out_battle
        self.usabilityInBattle: str = usability_in_battle
        self.specialItems: str = special_items
        self.moveName: str = move_name
    def print(self):
        text_list = ["ID number:", "Id:", "Name:", "Name plural:", "Pocket:", "Price:", "Desciption:",
                    "Usability outside of battle:", "Usability inside of battle:","Special items:", "Move name:"]
        attribute_list = [self.idNumber, self.id, self.name, self.namePlural, self.pocket, self.price, self.description,
                         self.usabilityOutBattle, self.usabilityInBattle, self.specialItems, self.moveName]
        for i in range(len(attribute_list)):
            print_if_value(text_list[i], attribute_list[i])

