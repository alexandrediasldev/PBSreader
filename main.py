import itertools
from PBSclasses.Environment import Environment
import Visualization
from Parser import *
import FileLoader
from PBSclasses.EncounterMethod import *
from matplotlib import pyplot as plt

if __name__ == '__main__':
    csv_trainer = FileLoader.file_csv_tolist('PBS/trainers.txt')
    csv_trainer_type = FileLoader.file_csv_tolist('PBS/trainertypes.txt')
    csv_move = FileLoader.file_csv_tolist('PBS/moves.txt')
    csv_item = FileLoader.file_csv_tolist('PBS/items.txt')
    csv_ability = FileLoader.file_csv_tolist('PBS/abilities.txt')
    csv_encounter = FileLoader.file_csv_tolist('PBS/encounters.txt')
    equal_pokemon_species = FileLoader.file_equal_to_list('PBS/pokemon.txt')

    env = Environment()
    env.load_environment(csv_trainer_type,equal_pokemon_species,csv_move,csv_item,csv_trainer,csv_encounter,csv_ability)
    for q in env.ability_list:
        q.print()

    #f, ax = Visualization.plot_all_encounter_map_types(env.encounter_list)
    #f.show()
