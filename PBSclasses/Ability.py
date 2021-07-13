from utils import print_if_value


class Ability:
    def __init__(self, id_number, id, name, description):
        self.description: str = description
        self.name: str = name
        self.id: str = id
        self.idNumber: str = id_number

    def print(self)->None:
        text_list = ["ID number:", "ID:", "Name:", "Description:"]
        attribute_list = [self.idNumber, self.id, self.name, self.description]
        for i in range(len(attribute_list)):
            print_if_value(text_list[i], attribute_list[i])
