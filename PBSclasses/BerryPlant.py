from dataclasses import dataclass

from PBSclasses.BaseData import BaseData


@dataclass
class BerryPlantV16(BaseData):
    name: str
    growth_rate: str
    moisture: str
    minimum_yield: str
    maximum_yield: str
