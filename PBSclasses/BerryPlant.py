from dataclasses import dataclass

from PBSclasses.BaseData import BaseData


@dataclass
class BerryPlant(BaseData):
    name: str
    growth_rate: str
    moisture: str
    minimum_yield: str
    maximum_yield: str
