from pathlib import Path

from src.Finder import get_species_from_name, get_trainer_type_from_name, get_item_from_name
from PBSclasses.Environment import Environment

from src import FileLoader
from src.Exporter import (
    deserialize_encounter,
    deserialize_ability,
    deserialize_trainer_types,
    deserialize_move,
    deserialize_item,
    deserialize_metadata,
    deserialize_species,
    deserialize_phone,
    deserialize_type,
    deserialize_townmap,
    deserialize_shadow,
    deserialize_trainer,
    deserialize_connection,
)

if __name__ == "__main__":
    pbs_location = "./PBS/"
    csv_trainer = FileLoader.file_csv_tolist(pbs_location + "trainers.txt")
    csv_trainer_type = FileLoader.file_csv_tolist(pbs_location + "trainertypes.txt")
    csv_move = FileLoader.file_csv_tolist(pbs_location + "moves.txt")
    csv_item = FileLoader.file_csv_tolist(pbs_location + "items.txt")
    csv_ability = FileLoader.file_csv_tolist(pbs_location + "abilities.txt")
    csv_encounter = FileLoader.file_csv_tolist(pbs_location + "encounters.txt")
    csv_connection = FileLoader.file_csv_tolist(pbs_location + "connections.txt")
    equal_pokemon_species = FileLoader.file_equal_to_list(pbs_location + "pokemon.txt")
    equal_pokemon_shadow = FileLoader.file_equal_to_list(pbs_location + "shadowmoves.txt")
    equal_phone = FileLoader.file_equal_to_list(pbs_location + "phone.txt")
    equal_type = FileLoader.file_equal_to_list(pbs_location + "types.txt")
    equal_townmap = FileLoader.file_equal_to_list(pbs_location + "townmap.txt")
    equal_metadata = FileLoader.file_equal_to_list(pbs_location + "metadata.txt")

    env = Environment()
    env.load_environment(
        csv_trainer_type,
        equal_pokemon_species,
        csv_move,
        csv_item,
        csv_trainer,
        csv_encounter,
        csv_ability,
        csv_connection,
        equal_pokemon_shadow,
        equal_phone,
        equal_type,
        equal_townmap,
        equal_metadata,
    )

    spe = get_species_from_name("RIOLU", env.species_list)
    tr_type = get_trainer_type_from_name("EclipseDame", env.trainer_type_list)
    mov = env.move_list[5]
    firestone = get_item_from_name("FIRESTONE", env.item_list)
    tra = env.trainer_list[23]
    abi = env.ability_list[8]
    encou = env.encounter_list[3]
    conn = env.connection_list[3]
    shadow = env.shadow_list[4]
    pho = env.phone
    ty = env.type_list[2]
    town = env.townmap_list[0]
    met = env.metadata_list[0]

    print(deserialize_species(spe))
    print(deserialize_trainer_types(tr_type))
    print(deserialize_move(mov))
    print(deserialize_item(firestone, 15))
    print(deserialize_trainer(tra))
    print(deserialize_ability(abi))
    print(deserialize_encounter(encou))
    print(deserialize_connection(conn))
    print(deserialize_shadow(shadow))
    print(deserialize_phone(pho))
    print(deserialize_type(ty))
    print(deserialize_townmap(town))
    print(deserialize_metadata(met))

    # print(deserialize_trainer(tra))
    # print(deserialize_encounters(env.encounter_list))

    # f, ax = Visualization.plot_all_encounter_map_types(env.encounter_list)
    # f.show()
