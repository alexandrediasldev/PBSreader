from utils import printIfValue


class Ability:
    def __init__(self, idNumber, id, name, description):
        self.description : str = description
        self.name :str = name
        self.id :str = id
        self.idNumber :str= idNumber


    def print(self):
        textList = ["ID number:", "ID:", "Name:", "Description:"]
        attributeList = [self.idNumber, self.id, self.name, self.description]
        for i in range(len(attributeList)):
            printIfValue(textList[i], attributeList[i])