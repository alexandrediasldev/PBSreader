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
    env.load_environment(csv_trainer_type, equal_pokemon_species, csv_move, csv_item, csv_trainer, csv_encounter,
                         csv_ability)

    spe = get_species_from_name("LUCARIO",env.species_list)
    spe.print()
    tre = get_trainer_type_from_name("EclipseDame",env.trainer_type_list)

    tre.print()

    firestone= get_item_from_name("FIRESTONE", env.item_list)
    env.trainer_list[23].print()
    firestone.print()



    #f, ax = Visualization.plot_all_encounter_map_types(env.encounter_list)
    #f.show()
