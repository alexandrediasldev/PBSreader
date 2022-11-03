from dataclasses import dataclass, field
from typing import Tuple, List

from PBSclasses.BaseData import BaseData
from PBSclasses.SpeciesEvolution import SpeciesEvolution
from PBSclasses.SpeciesStats import SpeciesStats


@dataclass
class PokemonFormV17(BaseData):
    id: str = ""
    id_number: str = ""
    type1: str = ""
    type2: str = ""
    base_stats: SpeciesStats = field(default_factory=SpeciesStats)
    base_EXP: str = ""
    effort_points: SpeciesStats = field(default_factory=SpeciesStats)
    rareness: str = ""
    happiness: str = ""
    abilities: List[str] = field(default_factory=list)
    hidden_ability: List[str] = field(default_factory=list)
    form_names: List[str] = field(default_factory=list)
    moves: List[Tuple[str, str]] = field(default_factory=list)
    egg_moves: List[str] = field(default_factory=list)
    steps_to_hatch: str = ""
    height: str = ""
    weight: str = ""
    color: str = ""
    habitat: str = ""
    kind: str = ""
    pokedex: str = ""
    wild_item_common: str = ""
    wild_item_uncommon: str = ""
    wild_item_rare: str = ""
    battler_player_y: str = ""
    battler_enemy_y: str = ""
    battler_altitude: str = ""
    evolutions: SpeciesEvolution = field(default_factory=SpeciesEvolution)
    shape: str = ""
    mega_stone: str = ""
    unmega_form: str = ""
    mega_move: str = ""
    mega_message: str = ""


@dataclass
class PokemonFormV18(BaseData):
    id: str = ""
    id_number: str = ""
    type1: str = ""
    type2: str = ""
    base_stats: SpeciesStats = field(default_factory=SpeciesStats)
    base_EXP: str = ""
    effort_points: SpeciesStats = field(default_factory=SpeciesStats)
    rareness: str = ""
    happiness: str = ""
    abilities: List[str] = field(default_factory=list)
    hidden_ability: List[str] = field(default_factory=list)
    form_names: List[str] = field(default_factory=list)
    moves: List[Tuple[str, str]] = field(default_factory=list)
    egg_moves: List[str] = field(default_factory=list)
    compatibility: List[str] = field(default_factory=list)
    steps_to_hatch: str = ""
    height: str = ""
    weight: str = ""
    color: str = ""
    habitat: str = ""
    kind: str = ""
    pokedex: str = ""
    wild_item_common: str = ""
    wild_item_uncommon: str = ""
    wild_item_rare: str = ""
    battler_player_x: str = ""
    battler_player_y: str = ""
    battler_enemy_x: str = ""
    battler_enemy_y: str = ""
    battler_shadow_x: str = ""
    battler_shadow_size: str = ""
    battler_altitude: str = ""
    evolutions: SpeciesEvolution = field(default_factory=SpeciesEvolution)
    shape: str = ""
    mega_stone: str = ""
    unmega_form: str = ""
    mega_move: str = ""
    mega_message: str = ""
    pokedex_form: str = ""


@dataclass
class PokemonFormV19(BaseData):
    id: str = ""
    id_number: str = ""
    type1: str = ""
    type2: str = ""
    base_stats: SpeciesStats = field(default_factory=SpeciesStats)
    base_EXP: str = ""
    effort_points: SpeciesStats = field(default_factory=SpeciesStats)
    rareness: str = ""
    happiness: str = ""
    abilities: List[str] = field(default_factory=list)
    hidden_ability: List[str] = field(default_factory=list)
    form_names: List[str] = field(default_factory=list)
    moves: List[Tuple[str, str]] = field(default_factory=list)
    tutor_moves: List[str] = field(default_factory=list)
    egg_moves: List[str] = field(default_factory=list)
    compatibility: List[str] = field(default_factory=list)
    steps_to_hatch: str = ""
    height: str = ""
    weight: str = ""
    color: str = ""
    habitat: str = ""
    kind: str = ""
    pokedex: str = ""
    generation: str = ""
    wild_item_common: str = ""
    wild_item_uncommon: str = ""
    wild_item_rare: str = ""
    battler_player_x: str = ""
    battler_player_y: str = ""
    battler_enemy_x: str = ""
    battler_enemy_y: str = ""
    battler_shadow_x: str = ""
    battler_shadow_size: str = ""
    battler_altitude: str = ""
    evolutions: SpeciesEvolution = field(default_factory=SpeciesEvolution)
    shape: str = ""
    mega_stone: str = ""
    unmega_form: str = ""
    mega_move: str = ""
    mega_message: str = ""
    pokedex_form: str = ""


@dataclass
class PokemonFormV20(BaseData):
    id: str = ""
    types: List[str] = field(default_factory=list)
    base_stats: SpeciesStats = field(default_factory=SpeciesStats)
    base_EXP: str = ""
    EVs: SpeciesStats = field(default_factory=SpeciesStats)
    catch_rate: str = ""
    happiness: str = ""
    abilities: List[str] = field(default_factory=list)
    hidden_ability: List[str] = field(default_factory=list)
    moves: List[Tuple[str, str]] = field(default_factory=list)
    tutor_moves: List[str] = field(default_factory=list)
    egg_moves: List[str] = field(default_factory=list)
    egg_groups: List[str] = field(default_factory=list)
    hatch_steps: str = ""
    offspring: List[str] = field(default_factory=list)
    height: str = ""
    weight: str = ""
    color: str = ""
    habitat: str = ""
    category: str = ""
    pokedex: str = ""
    form_names: List[str] = field(default_factory=list)
    generation: str = ""
    flags: List[str] = field(default_factory=list)
    wild_item_common: str = ""
    wild_item_uncommon: str = ""
    wild_item_rare: str = ""
    evolutions: SpeciesEvolution = field(default_factory=SpeciesEvolution)
    shape: str = ""
    mega_stone: str = ""
    unmega_form: str = ""
    mega_move: str = ""
    mega_message: str = ""
    pokedex_form: str = ""
