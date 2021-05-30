from PBSclasses.TrainerTypes import TrainerType
from PBSclasses.Pokemon import Pokemon
from utils import *
class Trainer:
    pokemonList: [Pokemon]
    type: TrainerType

    def __init__(self, type, name, nbPokemon, pokemonList):
        self.type = type
        self.name = name
        self.nbPokemon = nbPokemon
        self.pokemonList = pokemonList

    def print(self):
        print("Trainer:")
        self.type.print()
        printIfValue("Name:", self.name)
        printIfValue("nbPokemon:", self.nbPokemon)
        print("pokemonList:")
        for pkm in self.pokemonList:
            pkm.print()

    def getWinMoney(self):
        baseMoney = int(self.type.baseMoney)
        maxLevel = 0
        for pkm in self.pokemonList:
            if (maxLevel < int(pkm.level)):
                maxLevel = int(pkm.level)
        return baseMoney * maxLevel

    def toTrainerEntryBulbapedia(self):
        trainerEntry = "{{Trainer/entry"
        trainerEntry += "|"+self.type.toTrainerEntryBulbapedia() + "|" + self.name + "|"
        trainerEntry += str(self.getWinMoney()) + "|"
        trainerEntry += str(self.nbPokemon) + "|"
        for p in self.pokemonList:
            trainerEntry += p.toTrainerEntryBulbapedia()
        trainerEntry += "}}"
        return trainerEntry
