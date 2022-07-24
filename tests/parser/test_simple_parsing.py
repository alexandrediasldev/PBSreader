from PBSclasses.EncounterMethod import get_default_encounter_method_list
from src import FileLoader
from src.parser.parser import (
    parse_ability,
    parse_item,
    parse_move,
    parse_berry_plant,
    parse_connection,
    parse_trainer_types,
    parse_shadow_pokemon,
    parse_type,
    parse_phone,
    parse_metadata,
    parse_townmap,
    parse_pokemon,
    parse_trainer_list,
    parse_encounter,
    parse_tm,
    parse_regional_dex,
    parse_ribbon,
    parse_pokemon_form,
)


def check_attributes(obj):
    for name in obj.__dict__:
        if isinstance(obj.__dict__[name], list):  # List
            if isinstance(obj.__dict__[name][0], str):  # List[str]
                for i in range(len(obj.__dict__[name])):
                    assert name + str(i) == obj.__dict__[name][i]
            elif isinstance(obj.__dict__[name][0], tuple):  # List[tuple]
                for i in range(len(obj.__dict__[name])):
                    assert name + str(i) + "left" == obj.__dict__[name][i][0]
                    assert name + str(i) + "right" == obj.__dict__[name][i][1]
            else:  # List[Object]
                for i in range(len(obj.__dict__[name])):
                    check_attributes(obj.__dict__[name][i])
        elif isinstance(obj.__dict__[name], str):  # str
            if name != "nb_pokemon" and name != "map_id_number":
                assert name == obj.__dict__[name]
        else:  # Object
            check_attributes(obj.__dict__[name])


def file_check(file, parse_function, version):
    if version:
        list_obj = parse_function(file, version)
    else:
        list_obj = parse_function(file)
    if isinstance(list_obj, list):
        assert len(list_obj) == 1
        check_attributes(list_obj[0])
    else:
        check_attributes(list_obj)


def csv_check(filename, parse_function, version=None):
    file = FileLoader.file_csv_tolist("../PBS/" + filename)
    file_check(file, parse_function, version)


def equal_coma_check(filename, parse_function, version=None):
    file = FileLoader.file_equal_coma_to_list("../PBS/" + filename)
    file_check(file, parse_function, version)


def equal_check(filename, parse_function, version=None):
    file = FileLoader.file_equal_to_list("../PBS/" + filename)
    file_check(file, parse_function, version)


def test_ability():
    csv_check("abilities.txt", parse_ability)


def test_itemv15():
    csv_check("itemsv15.txt", parse_item, version=15)


def test_itemv16():
    csv_check("itemsv16.txt", parse_item, version=16)


def test_move():
    csv_check("moves.txt", parse_move)


def test_connection():
    csv_check("connections.txt", parse_connection)


def test_trainer_typev15():
    csv_check("trainertypesv15.txt", parse_trainer_types, version=15)


def test_trainer_typev16():
    csv_check("trainertypesv16.txt", parse_trainer_types, version=16)


def test_berryplant():
    equal_coma_check("berryplants.txt", parse_berry_plant)


def test_shadow():
    equal_check("shadowmoves.txt", parse_shadow_pokemon)


# ---- Equal


def test_type():
    equal_check("types.txt", parse_type)


def test_metadatav15():
    equal_check("metadatav15.txt", parse_metadata, version=15)


def test_metadatav18():
    equal_check("metadatav18.txt", parse_metadata, version=18)


def test_townmap():
    equal_check("townmap.txt", parse_townmap)


def test_pokemonv15():
    equal_check("pokemonv15.txt", parse_pokemon, version=15)


def test_pokemonv16():
    equal_check("pokemonv16.txt", parse_pokemon, version=16)


def test_pokemonv17():
    equal_check("pokemonv17.txt", parse_pokemon, version=17)


def test_pokemonv18():
    equal_check("pokemonv18.txt", parse_pokemon, version=18)


def test_pokemonv19():
    equal_check("pokemonv19.txt", parse_pokemon, version=19)


def test_pokemonformv17():
    equal_check("pokemonformsv17.txt", parse_pokemon_form, version=17)


def test_pokemonformv18():
    equal_check("pokemonformsv18.txt", parse_pokemon_form, version=18)


def test_pokemonformv19():
    equal_check("pokemonformsv19.txt", parse_pokemon_form, version=19)


def test_trainersv15():
    csv_check("trainersv15.txt", parse_trainer_list, version=15)


def test_trainersv18():
    equal_check("trainersv18.txt", parse_trainer_list, version=18)


def test_phone():
    equal_check("phone.txt", parse_phone)


def test_tm():
    equal_check("tm.txt", parse_tm, version=15)


def test_regional_dexes():
    equal_check("regionaldexes.txt", parse_regional_dex, version=19)


def test_ribbon():
    csv_check("ribbons.txt", parse_ribbon, version=19)


def test_encountersv15():
    csv_check("encountersv15.txt", parse_encounter, version=15)


def test_encountersv19():
    csv_check("encountersv19.txt", parse_encounter, version=19)
