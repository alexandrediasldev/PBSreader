from PBSclasses.TrainerTypes import TrainerType
from PBSclasses.Pokemon import Pokemon
from utils import *


class Trainer:
    pokemon_list: [Pokemon]
    type: TrainerType

    def __init__(self, type, name, nb_pokemon, pokemon_list):
        self.type: TrainerType = type
        self.name: str = name
        self.nb_pokemon: str = nb_pokemon
        self.pokemon_list: list[Pokemon] = pokemon_list

    def print(self) -> None:
        print("Trainer:")
        self.type.print()
        print_if_value("Name:", self.name)
        print_if_value("nbPokemon:", self.nb_pokemon)
        print("pokemonList:")
        for pkm in self.pokemon_list:
            pkm.print()

    def get_win_money(self) -> int:
        """
        The amount of money a trainer gives is decided according to this formula
        baseMoney * highestPokemonLevel
        :return: Win money
        """
        base_money = int(self.type.base_money)
        max_level = 0
        for pkm in self.pokemon_list:
            if (max_level < int(pkm.level)):
                max_level = int(pkm.level)
        return base_money * max_level

    def to_trainer_entry_bulbapedia(self)-> str:
        trainer_entry = "{{Trainer/entry"
        trainer_entry += "|" + self.type.to_trainer_entry_bulbapedia() + "|" + self.name + "|"
        trainer_entry += str(self.get_win_money()) + "|"
        trainer_entry += str(self.nb_pokemon) + "|"
        for p in self.pokemon_list:
            trainer_entry += p.to_trainer_entry_bulbapedia()
        trainer_entry += "}}"
        return trainer_entry
