import pytest

from PBSclasses.EncounterMethod import get_default_encounter_method_list
from src import FileLoader
from src.Exception import UnsupportedVersionError
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
    parse_pokemon_metric,
    parse_map_metadata,
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


class TestUnsuportedVersion:
    def catch_exception(self, parse_function, version):
        with pytest.raises(UnsupportedVersionError):
            file_check(None, parse_function, version=version)

    def test_simple(self):
        all_parse_function = [
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
            parse_pokemon_metric,
            parse_map_metadata,
        ]
        for parse_function in all_parse_function:
            self.catch_exception(parse_function, 14)
            self.catch_exception(parse_function, 21)

    def test_introduced_later(self):
        self.catch_exception(parse_berry_plant, 15)
        self.catch_exception(parse_pokemon_form, 16)
        self.catch_exception(parse_regional_dex, 18)
        self.catch_exception(parse_ribbon, 18)
        self.catch_exception(parse_map_metadata, 19)
        self.catch_exception(parse_pokemon_metric, 19)

    def test_removed(self):
        self.catch_exception(parse_tm, 19)


class TestAbility:
    def test_abilityv15(self):
        for version in [15, 16, 17, 18, 19]:
            csv_check("abilities.txt", parse_ability, version=version)

    def test_abilityv20(self):
        equal_check("abilitiesv20.txt", parse_ability, version=20)


class TestItem:
    def test_itemv15(self):
        csv_check("itemsv15.txt", parse_item, version=15)

    def test_itemv16(self):
        for version in [16, 17, 18, 19]:
            csv_check("itemsv16.txt", parse_item, version=version)

    def test_itemv20(self):
        equal_check("itemsv20.txt", parse_item, version=20)


class TestMove:
    def test_movev15(self):
        for version in [15, 16, 17, 18, 19]:
            csv_check("moves.txt", parse_move, version=version)

    def test_movev20(self):
        equal_check("movesv20.txt", parse_move, version=20)


class TestConnection:
    def test_connection(self):
        for version in [15, 16, 17, 18, 19, 20]:
            csv_check("connections.txt", parse_connection, version=version)


class TestTrainerTypes:
    def test_trainer_typev15(self):
        csv_check("trainertypesv15.txt", parse_trainer_types, version=15)

    def test_trainer_typev16(self):
        for version in [16, 17, 18, 19]:
            csv_check("trainertypesv16.txt", parse_trainer_types, version=version)

    def test_trainer_typev20(self):
        equal_check("trainertypesv20.txt", parse_trainer_types, version=20)


class TestBerryPlant:
    def test_berryplantv16(self):
        for version in [16, 17, 18, 19]:
            equal_coma_check("berryplants.txt", parse_berry_plant, version=version)

    def test_berryplantv20(self):
        equal_check("berryplantsv20.txt", parse_berry_plant, version=20)


class TestShadow:
    def test_shadowv15(self):
        for version in [15, 16, 17, 18, 19]:
            equal_check("shadowmoves.txt", parse_shadow_pokemon, version=version)

    def test_shadowv20(self):
        equal_check("shadowmovesv20.txt", parse_shadow_pokemon, version=20)


# ---- Equal


class TestType:
    def test_typev15(self):
        for version in [15, 16, 17, 18, 19]:
            equal_check("types.txt", parse_type, version=version)

    def test_typev20(self):
        equal_check("typesv20.txt", parse_type, version=20)


class TestMetadata:
    def test_metadatav15(self):
        for version in [15, 16, 17]:
            equal_check("metadatav15.txt", parse_metadata, version=version)

    def test_metadatav18(self):
        for version in [18, 19]:
            equal_check("metadatav18.txt", parse_metadata, version=version)

    def test_metadatav20(self):
        equal_check("metadatav20.txt", parse_metadata, version=20)


class TestMapMetadata:
    def test_mapmetadatav20(self):
        equal_check("mapmetadatav20.txt", parse_map_metadata, version=20)


class TestTownmap:
    def test_townmap(self):
        for version in [15, 16, 17, 18, 19, 20]:
            equal_check("townmap.txt", parse_townmap, version=version)


class TestPokemon:
    def test_pokemonv15(self):
        equal_check("pokemonv15.txt", parse_pokemon, version=15)

    def test_pokemonv16(self):
        equal_check("pokemonv16.txt", parse_pokemon, version=16)

    def test_pokemonv17(self):
        equal_check("pokemonv17.txt", parse_pokemon, version=17)

    def test_pokemonv18(self):
        equal_check("pokemonv18.txt", parse_pokemon, version=18)

    def test_pokemonv19(self):
        equal_check("pokemonv19.txt", parse_pokemon, version=19)

    def test_pokemonv20(self):
        equal_check("pokemonv20.txt", parse_pokemon, version=20)


class TestPokemonForm:
    def test_pokemonformv17(self):
        equal_check("pokemonformsv17.txt", parse_pokemon_form, version=17)

    def test_pokemonformv18(self):
        equal_check("pokemonformsv18.txt", parse_pokemon_form, version=18)

    def test_pokemonformv19(self):
        equal_check("pokemonformsv19.txt", parse_pokemon_form, version=19)

    def test_pokemonformv20(self):
        equal_check("pokemonformsv20.txt", parse_pokemon_form, version=20)


class TestPokemonMetric:
    def test_pokemonmetricv20(self):
        equal_check("pokemonmetricsv20.txt", parse_pokemon_metric, version=20)


class TestTrainer:
    def test_trainersv15(self):
        for version in [15, 16, 17]:
            csv_check("trainersv15.txt", parse_trainer_list, version=version)

    def test_trainersv18(self):
        for version in [18, 19]:
            equal_check("trainersv18.txt", parse_trainer_list, version=version)

    def test_trainersv20(self):
        equal_check("trainersv20.txt", parse_trainer_list, version=20)


class TestPhone:
    def test_phone(self):
        for version in [15, 16, 17, 18, 19, 20]:
            equal_check("phone.txt", parse_phone, version=version)


class TestTm:
    def test_tm(self):
        for version in [15, 16, 17]:
            equal_check("tm.txt", parse_tm, version=version)


class TestRegionalDexes:
    def test_regional_dexes(self):
        for version in [19, 20]:
            equal_check("regionaldexes.txt", parse_regional_dex, version=version)


class TestRibbon:
    def test_ribbonv19(self):
        csv_check("ribbons.txt", parse_ribbon, version=19)

    def test_ribbonv20(self):
        equal_check("ribbonsv20.txt", parse_ribbon, version=20)


class TestEncounter:
    def test_encountersv15(self):
        for version in [15, 16, 17, 18]:
            csv_check("encountersv15.txt", parse_encounter, version=version)

    def test_encountersv19(self):
        for version in [19, 20]:
            csv_check("encountersv19.txt", parse_encounter, version=version)
