from utils import printIfValue


class Item:
    def __init__(self,idNumber, id, name, namePlural, pocket,price, description,
                 usabilityOutBattle, usabilityInBattle, specialItems, moveName):
        self.description = description
        self.price = price
        self.pocket = pocket
        self.namePlural = namePlural
        self.name = name
        self.id = id
        self.idNumber = idNumber
        self.usabilityOutBattle = usabilityOutBattle
        self.usabilityInBattle = usabilityInBattle
        self.specialItems = specialItems
        self.moveName = moveName
    def print(self):
        textList = ["ID number:", "Id:", "Name:", "Name plural:", "Pocket:", "Price:", "Desciption:",
                    "Usability outside of battle:", "Usability inside of battle:","Special items:", "Move name:"]
        attributeList = [self.idNumber, self.id, self.name, self.namePlural, self.pocket, self.price, self.description,
                         self.usabilityOutBattle, self.usabilityInBattle, self.specialItems, self.moveName]
        for i in range(len(attributeList)):
            printIfValue(textList[i], attributeList[i])

