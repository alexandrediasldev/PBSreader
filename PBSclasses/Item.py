from utils import print_if_value


class Item:
    def __init__(self, id_number, id, name, name_plural, pocket, price, description,
                 usability_out_battle, usability_in_battle, special_items, move_name):
        self.description: str = description
        self.price: str = price
        self.pocket: str = pocket
        self.name_plural: str = name_plural
        self.name: str = name
        self.id: str = id
        self.id_number: str = id_number
        self.usability_out_battle: str = usability_out_battle
        self.usability_in_battle: str = usability_in_battle
        self.special_items: str = special_items
        self.move_name: str = move_name

    def print(self) -> None:
        text_list = ["ID number:", "Id:", "Name:", "Name plural:", "Pocket:", "Price:", "Desciption:",
                     "Usability outside of battle:", "Usability inside of battle:", "Special items:", "Move name:"]
        attribute_list = [self.id_number, self.id, self.name, self.name_plural, self.pocket, self.price, self.description,
                          self.usability_out_battle, self.usability_in_battle, self.special_items, self.move_name]
        for i in range(len(attribute_list)):
            print_if_value(text_list[i], attribute_list[i])
