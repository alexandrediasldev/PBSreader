from dataclasses import dataclass, field

from PBSclasses.BaseData import BaseData


@dataclass
class PlayerMetaData(BaseData):
    trainer_type: str = ""
    walking_charset: str = ""
    cycling_charset: str = ""
    surfing_charset: str = ""
    running_charset: str = ""
    diving_charset: str = ""
    fishing_while_standing_charset: str = ""
    fishing_while_surfing_charset: str = ""


@dataclass
class HomeMetaData(BaseData):
    map_id: str = ""
    position_x: str = ""
    position_y: str = ""
    direction: str = ""


@dataclass
class MetaData(BaseData):
    id: str = ""
    players: list[PlayerMetaData] = field(default_factory=list)
    home: HomeMetaData = field(default_factory=HomeMetaData)
    bycycle_BGM: str = ""
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
