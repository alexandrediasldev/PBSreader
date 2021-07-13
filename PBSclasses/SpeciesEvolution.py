class SpeciesEvolution:
    def __init__(self, name, method, evolution_parameter):
        self.name: str = name
        self.method: str = method
        self.evolution_parameter: str = evolution_parameter

    def print(self)->None:
        if(self.name != ""):
            print("Evolution: ",end="")
            print("Name:", self.name," ",end="")
        if(self.method != ""):
              print("Method:", self.method," ",end="")
        if(self.evolution_parameter != ""):
            print("Parameter:", self.evolution_parameter, end="")
        print()
