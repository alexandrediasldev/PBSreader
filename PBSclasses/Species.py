from PBSclasses.SpeciesStats import SpeciesStats
from utils import *


class Species:
    def __init__(self, id, name, internal_name, type1, type2, base_stats, gender_rate, base_exp, moves, height, pokedex,
                 evolutions):
        self.id: str = id
        self.name: str = name
        self.internal_name: str = internal_name
        self.type1: str = type1
        self.type2: str = type2
        self.base_stats: SpeciesStats = base_stats
        self.gender_rate: str = gender_rate
        self.base_exp: str = base_exp
        self.moves: list[Tuple[str, str]] = moves
        self.height: str = height
        self.evolutions: list[str] = evolutions
        self.pokedex: str = pokedex

    def print(self)->None:
        text_list = ["Id:", "Name:", "Internal Name:", "Type1:", "Type2:", "Base Stats:", "Gender Rate:",
                     "Base EXP:", "Moves:", "Height:", "Evolutions:", "Pokedex:"]
        attribute_list = [self.id, self.name, self.internal_name, self.type1, self.type2, self.base_stats,
                          self.gender_rate, self.base_exp, self.moves, self.height, self.evolutions, self.pokedex]
        for i in range(len(attribute_list)):
            if (text_list[i] == "Base Stats:" or text_list[i] == "Evolutions:"):
                attribute_list[i].print()
            else:
                print_if_value(text_list[i], attribute_list[i])
