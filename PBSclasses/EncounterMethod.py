from utils import *
from typing import List


class EncounterMethod:

    def __init__(self, method_name, number_of_entries, probability_of_encounter):
        self.probability_of_encounter: list[str] = probability_of_encounter
        self.number_of_entries: str = number_of_entries
        self.method_name: str = method_name

    def print(self)->None:
        print_if_value("Method Name:", self.method_name)
        print_if_value("Number of Entries:", self.number_of_entries)
        print_if_value("Probability of Encounter:", self.probability_of_encounter)


def get_default_encounter_method_list():
    """
    Default encounter method in base essential
    :return: List of Encounter Methods
    """
    encounter_method_list = []

    probability_type1 = [20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1, 1]
    number_of_entries1 = len(probability_type1)
    encounter_method1 = ["Land", "LandMorning", "LandDay", "LandNight", "Cave", "BugContest"]

    probability_type2 = [60, 30, 5, 4, 1]
    number_of_entries2 = len(probability_type2)
    encounter_method2 = ["Water", "RockSmash"]

    probability_type3 = [70, 30]
    number_of_entries3 = len(probability_type3)
    encounter_method3 = ["OldRod"]

    probability_type4 = [60, 20, 20]
    number_of_entries4 = len(probability_type4)
    encounter_method4 = ["GoodRod"]

    probability_type5 = [40, 40, 15, 4, 1]
    number_of_entries5 = len(probability_type5)
    encounter_method5 = ["SuperRod"]

    probability_type6 = [30, 25, 20, 10, 5, 5, 4, 1]
    number_of_entries6 = len(probability_type6)
    encounter_method6 = ["HeadbuttLow", "HeadbuttHigh"]

    default_methods = [(probability_type1, number_of_entries1, encounter_method1),
                      (probability_type2, number_of_entries2, encounter_method2),
                      (probability_type3, number_of_entries3, encounter_method3),
                      (probability_type4, number_of_entries4, encounter_method4),
                      (probability_type5, number_of_entries5, encounter_method5),
                      (probability_type6, number_of_entries6, encounter_method6)]

    for probability, number, encounterList in default_methods:
        for e in encounterList:
            encounter_method_list.append(EncounterMethod(e, number, probability))
    return encounter_method_list
