from dataclasses import dataclass, field

from PBSclasses.BaseData import BaseData
from PBSclasses.Pokemon import Pokemon
from src.Finder import get_trainer_type_from_name


@dataclass
class Trainer(BaseData):
    type: str
    name: str
    version_number: str = ""
    item_list: list[str] = field(default_factory=list)
    nb_pokemon: str = ""
    pokemon_list: list[Pokemon] = field(default_factory=list)

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
