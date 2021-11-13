from PBSclasses.BaseData import BaseData


class SpeciesEvolution(BaseData):
    def __init__(self, name, method, evolution_parameter):
        self.name: str = name
        self.method: str = method
        self.evolution_parameter: str = evolution_parameter
