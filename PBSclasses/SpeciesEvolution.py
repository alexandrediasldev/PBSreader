from dataclasses import dataclass

from PBSclasses.BaseData import BaseData


@dataclass
class SpeciesEvolution(BaseData):
    name: str = ""
    method: str = ""
    evolution_parameter: str = ""

    # version v15
    @classmethod
    def get_attr_pbs_names(cls):
        return ["Name", "Method", "EvolutionParameter"]
