from utils import *


class EncounterMethod:

    def __init__(self, methodName, numberOfEntries, probabilityOfEncounter):
        self.probabilityOfEncounter: list[str] = probabilityOfEncounter
        self.numberOfEntries: str = numberOfEntries
        self.methodName: str = methodName

    def print(self):
        printIfValue("Method Name:", self.methodName)
        printIfValue("Number of Entries:", self.numberOfEntries)
        printIfValue("Probability of Encounter:", self.probabilityOfEncounter)


def getDefaultEncounterMethodList():
    encounterMethodList = []

    probabilityType1 = [20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1, 1]
    numberOfEntries1 = len(probabilityType1)
    encounterMethod1 = ["Land", "LandMorning", "LandDay", "LandNight", "Cave", "BugContest"]

    probabilityType2 = [60, 30, 5, 4, 1]
    numberOfEntries2 = len(probabilityType2)
    encounterMethod2 = ["Water", "RockSmash"]

    probabilityType3 = [70, 30]
    numberOfEntries3 = len(probabilityType3)
    encounterMethod3 = ["OldRod"]

    probabilityType4 = [60, 20, 20]
    numberOfEntries4 = len(probabilityType4)
    encounterMethod4 = ["GoodRod"]

    probabilityType5 = [40, 40, 15, 4, 1]
    numberOfEntries5 = len(probabilityType5)
    encounterMethod5 = ["SuperRod"]

    probabilityType6 = [30, 25, 20, 10, 5, 5, 4, 1]
    numberOfEntries6 = len(probabilityType6)
    encounterMethod6 = ["HeadbuttLow", "HeadbuttHigh"]

    defaultMethods = [(probabilityType1, numberOfEntries1, encounterMethod1),
                      (probabilityType2, numberOfEntries2, encounterMethod2),
                      (probabilityType3, numberOfEntries3, encounterMethod3),
                      (probabilityType4, numberOfEntries4, encounterMethod4),
                      (probabilityType5, numberOfEntries5, encounterMethod5),
                      (probabilityType6, numberOfEntries6, encounterMethod6)]

    for probability, number, encounterList in defaultMethods:
        for e in encounterList:
            encounterMethodList.append(EncounterMethod(e, number, probability))
    return encounterMethodList
