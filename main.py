from Finder import get_species_from_name, get_trainer_type_from_name, get_item_from_name
from PBSclasses.Environment import Environment


import FileLoader


if __name__ == "__main__":
    csv_trainer = FileLoader.file_csv_tolist("PBS/trainers.txt")
    csv_trainer_type = FileLoader.file_csv_tolist("PBS/trainertypes.txt")
    csv_move = FileLoader.file_csv_tolist("PBS/moves.txt")
    csv_item = FileLoader.file_csv_tolist("PBS/items.txt")
    csv_ability = FileLoader.file_csv_tolist("PBS/abilities.txt")
    csv_encounter = FileLoader.file_csv_tolist("PBS/encounters.txt")
    csv_connection = FileLoader.file_csv_tolist("PBS/connections.txt")
    equal_pokemon_species = FileLoader.file_equal_to_list("PBS/pokemon.txt")
    equal_pokemon_shadow = FileLoader.file_equal_to_list("PBS/shadowmoves.txt")
    equal_phone = FileLoader.file_equal_to_list("PBS/phone.txt")
    equal_type = FileLoader.file_equal_to_list("PBS/types.txt")
    equal_townmap = FileLoader.file_equal_to_list("PBS/townmap.txt")
    equal_metadata = FileLoader.file_equal_to_list("PBS/metadata.txt")

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
    tre = get_trainer_type_from_name("EclipseDame", env.trainer_type_list)
    mov = env.move_list[5]
    firestone = get_item_from_name("FIRESTONE", env.item_list)
    tr_type = env.trainer_list[23]
    abi = env.ability_list[8]
    encou = env.encounter_list[3]
    conn = env.connection_list[3]
    shadow = env.shadow_list[4]
    pho = env.phone
    ty = env.type_list[2]
    town = env.townmap_list[0]
    met = env.metadata_list[0]

    # print(met)
    print(spe)

    # f, ax = Visualization.plot_all_encounter_map_types(env.encounter_list)
    # f.show()
