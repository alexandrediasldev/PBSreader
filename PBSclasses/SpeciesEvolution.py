class SpeciesEvolution:
    def __init__(self, name, method, evolutionParameter):
        self.name: str = name
        self.method: str = method
        self.evolutionParameter: str = evolutionParameter

    def print(self):
        if(self.name != ""):
            print("Evolution: ",end="")
            print("Name:", self.name," ",end="")
        if(self.method != ""):
              print("Method:", self.method," ",end="")
        if(self.evolutionParameter != ""):
            print("Parameter:", self.evolutionParameter,end="")
        print()