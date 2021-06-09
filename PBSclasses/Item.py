from utils import printIfValue


class Item:
    def __init__(self,idNumber, id, name, namePlural, pocket,price, description,
                 usabilityOutBattle, usabilityInBattle, specialItems, moveName):
        self.description: str = description
        self.price: str = price
        self.pocket: str = pocket
        self.namePlural: str = namePlural
        self.name: str = name
        self.id: str = id
        self.idNumber: str = idNumber
        self.usabilityOutBattle: str = usabilityOutBattle
        self.usabilityInBattle: str = usabilityInBattle
        self.specialItems: str = specialItems
        self.moveName: str = moveName
    def print(self):
        textList = ["ID number:", "Id:", "Name:", "Name plural:", "Pocket:", "Price:", "Desciption:",
                    "Usability outside of battle:", "Usability inside of battle:","Special items:", "Move name:"]
        attributeList = [self.idNumber, self.id, self.name, self.namePlural, self.pocket, self.price, self.description,
                         self.usabilityOutBattle, self.usabilityInBattle, self.specialItems, self.moveName]
        for i in range(len(attributeList)):
            printIfValue(textList[i], attributeList[i])

