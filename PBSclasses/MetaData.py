from dataclasses import dataclass, field
from typing import List

from PBSclasses.BaseData import BaseData


@dataclass
class HomeMetaData(BaseData):
    map_id: str = ""
    position_x: str = ""
    position_y: str = ""
    direction: str = ""


@dataclass
class PlayerMetaDataV15(BaseData):
    trainer_type: str = ""
    walking_charset: str = ""
    cycling_charset: str = ""
    surfing_charset: str = ""
    running_charset: str = ""
    diving_charset: str = ""
    fishing_while_standing_charset: str = ""
    fishing_while_surfing_charset: str = ""


@dataclass
class MetaDataV15(BaseData):
    id: str = ""
    player: List[PlayerMetaDataV15] = field(default_factory=list)
    home: HomeMetaData = field(default_factory=HomeMetaData)
    bicycle_BGM: str = ""
    surf_BGM: str = ""
    wild_battle_BGM: str = ""
    trainer_battle_BGM: str = ""
    wild_victory_ME: str = ""
    trainer_victory_ME: str = ""
    # Map specific metadata
    outdoor: str = ""
    bicycle: str = ""
    bicycle_always: str = ""
    healing_spot: str = ""
    map_position: str = ""
    map_size: str = ""
    show_area: str = ""
    weather: str = ""
    dark_map: str = ""
    dive_map: str = ""
    safari_map: str = ""
    snap_edges: str = ""
    dungeon: str = ""
    battle_back: str = ""


@dataclass
class MetaDataV18(BaseData):
    id: str = ""
    player: List[PlayerMetaDataV15] = field(default_factory=list)
    home: HomeMetaData = field(default_factory=HomeMetaData)
    bicycle_BGM: str = ""
    surf_BGM: str = ""
    wild_battle_BGM: str = ""
    trainer_battle_BGM: str = ""
    wild_victory_ME: str = ""
    trainer_victory_ME: str = ""
    wild_capture_ME: str = ""
    # Map specific metadata
    outdoor: str = ""
    bicycle: str = ""
    bicycle_always: str = ""
    healing_spot: str = ""
    map_position: str = ""
    map_size: str = ""
    show_area: str = ""
    weather: str = ""
    dark_map: str = ""
    dive_map: str = ""
    safari_map: str = ""
    snap_edges: str = ""
    dungeon: str = ""
    battle_back: str = ""
    environment: str = ""


@dataclass
class MetaDataV20(BaseData):
    id: str = ""
    home: HomeMetaData = field(default_factory=HomeMetaData)
    start_money: str = ""
    start_item_storage: List[str] = field(default_factory=list)
    storage_creator: str = ""
    wild_battle_BGM: str = ""
    trainer_battle_BGM: str = ""
    wild_victory_BGM: str = ""
    trainer_victory_BGM: str = ""
    wild_capture_ME: str = ""
    surf_BGM: str = ""
    bicycle_BGM: str = ""
    # Player metadata
    trainer_type: str = ""
    walk_charset: str = ""
    run_charset: str = ""
    cycle_charset: str = ""
    surf_charset: str = ""
    dive_charset: str = ""
    fish_charset: str = ""
    surf_fish_charset: str = ""
