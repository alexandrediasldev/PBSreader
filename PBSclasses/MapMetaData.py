from dataclasses import dataclass, field
from typing import List

from PBSclasses.BaseData import BaseData


@dataclass
class MapMetaDataV20(BaseData):
    id: str = ""
    name: str = ""
    map_position: str = ""
    map_size: str = ""
    outdoor: str = ""
    weather: str = ""
    show_area: str = ""
    bicycle: str = ""
    bicycle_always: str = ""
    healing_spot: str = ""
    dive_map: str = ""
    dark_map: str = ""
    safari_map: str = ""
    dungeon: str = ""
    snap_edges: str = ""
    battle_back: str = ""
    environment: str = ""
    wild_battle_BGM: str = ""
    wild_victory_BGM: str = ""
    trainer_battle_BGM: str = ""
    trainer_victory_BGM: str = ""
    wild_capture_ME: str = ""
    flags: List[str] = field(default_factory=list)
