from dataclasses import dataclass, field
from typing import List

from PBSclasses.BaseData import BaseData
from PBSclasses.TrainerPokemon import TrainerPokemonV15, TrainerPokemonV18
from src.Finder import get_trainer_type_from_name


@dataclass
class TrainerV15(BaseData):
    type: str
    name: str
    version_number: str = ""
    item_list: List[str] = field(default_factory=list)
    nb_pokemon: str = ""
    pokemon_list: List[TrainerPokemonV15] = field(default_factory=list)

    def get_win_money(self, trainer_types_list) -> int:
        """
        The amount of money a trainer gives is decided according to this formula
        baseMoney * highestPokemonLevel
        :return: Win money
        """
        trainer_type = get_trainer_type_from_name(self.type, trainer_types_list)
        base_money = int(trainer_type.base_money)
        max_level = 0
        for pkm in self.pokemon_list:
            if max_level < int(pkm.level):
                max_level = int(pkm.level)
        return base_money * max_level


@dataclass
class TrainerV18(BaseData):
    type: str
    name: str
    version_number: str = ""
    items: List[str] = field(default_factory=list)
    lose_text: str = ""
    pokemon: List[TrainerPokemonV18] = field(default_factory=list)
