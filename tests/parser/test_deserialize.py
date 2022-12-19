from PBSclasses import Ability
from PBSclasses.Ability import AbilityV15, AbilityV20
from PBSclasses.BerryPlant import BerryPlantV16, BerryPlantV20
from PBSclasses.Connection import ConnectionV15
from PBSclasses.Item import ItemV15, ItemV16, ItemV20
from PBSclasses.Move import MoveV15, MoveV20
from PBSclasses.RegionalDexes import RegionalDexV19
from PBSclasses.Ribbon import RibbonV19, RibbonV20
from PBSclasses.ShadowPokemon import ShadowPokemonV15, ShadowPokemonV20
from PBSclasses.Tm import TmV15
from PBSclasses.Type import TypeV15, TypeV20
from src import FileLoader
from src.Exporter import (
    deserialize_ability,
    deserialize_item,
    deserialize_connection,
    deserialize_move,
    deserialize_berry_plant,
    deserialize_shadow,
    deserialize_type,
    deserialize_tm,
    deserialize_regional_dex,
    deserialize_ribbon,
)


def generate_object(obj_class):
    for name in obj_class.__dict__:
        if isinstance(obj_class.__dict__[name], list):  # List
            for i in range(0, 3):
                obj_class.__dict__[name].append(name + str(i))

            # if isinstance(obj_class.__dict__[name][0], str):  # List[str]
            # for i in range(len(obj_class.__dict__[name])):
            #    assert name + str(i) == obj_class.__dict__[name][i]
            #    assert "TODO" == 0
            # elif isinstance(obj_class.__dict__[name][0], tuple):  # List[tuple]
            # for i in range(len(obj_class.__dict__[name])):
            #    assert name + str(i) + "left" == obj_class.__dict__[name][i][0]
            #    assert name + str(i) + "right" == obj_class.__dict__[name][i][1]
            #    assert "TODO" == 0
            # else:  # List[Object]
            # for i in range(len(obj_class.__dict__[name])):
            #    check_attributes(obj_class.__dict__[name][i])
            #    assert "TODO" == 0
        elif isinstance(obj_class.__dict__[name], str):  # str
            obj_class.__dict__[name] = name
            # if name != "nb_pokemon" and name != "map_id_number":
            #   assert name == obj_class.__dict__[name]
        else:  # Object
            # check_attributes(obj_class.__dict__[name])
            assert "TODO" == 0
    return obj_class


def check_file(generated_file, file):
    for line in generated_file:
        if not (line in file):
            assert file == generated_file


def compare_export(filename, obj_class, export_function, version):
    file = FileLoader.read_full_file("../PBS/" + filename)
    obj = generate_object(obj_class())
    file_exported = export_function(obj, version)
    check_file(file, file_exported)


class TestAbility:
    def test_abilityv15(self):
        for version in [15, 16, 17, 18, 19]:
            compare_export("abilities.txt", AbilityV15, deserialize_ability, version=version)

    def test_abilityv20(self):
        compare_export("abilitiesv20.txt", AbilityV20, deserialize_ability, 20)


class TestItem:
    def test_itemv15(self):
        compare_export("itemsv15.txt", ItemV15, deserialize_item, version=15)

    def test_itemv16(self):
        for version in [16, 17, 18, 19]:
            compare_export("itemsv16.txt", ItemV16, deserialize_item, version=version)

    def test_itemv20(self):
        compare_export("itemsv20.txt", ItemV20, deserialize_item, version=20)


class TestMove:
    def test_movev15(self):
        for version in [15, 16, 17, 18, 19]:
            compare_export("moves.txt", MoveV15, deserialize_move, version=version)

    def test_movev20(self):
        compare_export("movesv20.txt", MoveV20, deserialize_move, version=20)


class TestConnection:
    def test_connection(self):
        for version in [15, 16, 17, 18, 19, 20]:
            compare_export(
                "connections.txt", ConnectionV15, deserialize_connection, version=version
            )


# class TestTrainerTypes:
#    def test_trainer_typev15(self):
#        csv_check("trainertypesv15.txt", parse_trainer_types, version=15)

#   def test_trainer_typev16(self):
#        for version in [16, 17, 18, 19]:
#            csv_check("trainertypesv16.txt", parse_trainer_types, version=version)

#    def test_trainer_typev20(self):
#        equal_check("trainertypesv20.txt", parse_trainer_types, version=20)


class TestBerryPlant:
    def test_berryplantv16(self):
        for version in [16, 17, 18, 19]:
            compare_export(
                "berryplants.txt", BerryPlantV16, deserialize_berry_plant, version=version
            )

    def test_berryplantv20(self):
        compare_export("berryplantsv20.txt", BerryPlantV20, deserialize_berry_plant, version=20)


class TestShadow:
    def test_shadowv15(self):
        for version in [15, 16, 17, 18, 19]:
            compare_export("shadowmoves.txt", ShadowPokemonV15, deserialize_shadow, version=version)

    def test_shadowv20(self):
        compare_export("shadowmovesv20.txt", ShadowPokemonV20, deserialize_shadow, version=20)


# ---- Equal


class TestType:
    def test_typev15(self):
        for version in [15, 16, 17, 18, 19]:
            compare_export("types.txt", TypeV15, deserialize_type, version=version)

    def test_typev20(self):
        compare_export("typesv20.txt", TypeV20, deserialize_type, version=20)


# class TestMetadata:
#    def test_metadatav15(self):
#        for version in [15, 16, 17]:
#            equal_check("metadatav15.txt", parse_metadata, version=version)

#    def test_metadatav18(self):
#        for version in [18, 19]:
#            equal_check("metadatav18.txt", parse_metadata, version=version)

#    def test_metadatav20(self):
#        equal_check("metadatav20.txt", parse_metadata, version=20)


# class TestMapMetadata:
#    def test_mapmetadatav20(self):
#        equal_check("mapmetadatav20.txt", parse_map_metadata, version=20)


# class TestTownmap:
#    def test_townmap(self):
#        for version in [15, 16, 17, 18, 19, 20]:
#            equal_check("townmap.txt", parse_townmap, version=version)


# class TestPokemon:
#    def test_pokemonv15(self):
#        equal_check("pokemonv15.txt", parse_pokemon, version=15)

#    def test_pokemonv16(self):
#        equal_check("pokemonv16.txt", parse_pokemon, version=16)

#    def test_pokemonv17(self):
#        equal_check("pokemonv17.txt", parse_pokemon, version=17)

#    def test_pokemonv18(self):
#        equal_check("pokemonv18.txt", parse_pokemon, version=18)

#    def test_pokemonv19(self):
#        equal_check("pokemonv19.txt", parse_pokemon, version=19)

#    def test_pokemonv20(self):
#        equal_check("pokemonv20.txt", parse_pokemon, version=20)


# class TestPokemonForm:
#    def test_pokemonformv17(self):
#        equal_check("pokemonformsv17.txt", parse_pokemon_form, version=17)

#    def test_pokemonformv18(self):
#        equal_check("pokemonformsv18.txt", parse_pokemon_form, version=18)

#    def test_pokemonformv19(self):
#        equal_check("pokemonformsv19.txt", parse_pokemon_form, version=19)

#    def test_pokemonformv20(self):
#        equal_check("pokemonformsv20.txt", parse_pokemon_form, version=20)


# class TestPokemonMetric:
#    def test_pokemonmetricv20(self):
#        equal_check("pokemonmetricsv20.txt", parse_pokemon_metric, version=20)


# class TestTrainer:
#    def test_trainersv15(self):
#        for version in [15, 16, 17]:
#            csv_check("trainersv15.txt", parse_trainer_list, version=version)

#    def test_trainersv18(self):
#        for version in [18, 19]:
#            equal_check("trainersv18.txt", parse_trainer_list, version=version)

#    def test_trainersv20(self):
#        equal_check("trainersv20.txt", parse_trainer_list, version=20)


# class TestPhone:
#    def test_phone(self):
#        for version in [15, 16, 17, 18, 19, 20]:
#            equal_check("phone.txt", parse_phone, version=version)


class TestTm:
    def test_tm(self):
        for version in [15, 16, 17]:
            compare_export("tm.txt", TmV15, deserialize_tm, version=version)


# class TestRegionalDexes:
#    def test_regional_dexes(self):
#        for version in [19, 20]:
#            compare_export("regionaldexes.txt", RegionalDexV19,deserialize_regional_dex, version=version)


class TestRibbon:
    def test_ribbonv19(self):
        compare_export("ribbons.txt", RibbonV19, deserialize_ribbon, version=19)

    def test_ribbonv20(self):
        compare_export("ribbonsv20.txt", RibbonV20, deserialize_ribbon, version=20)


# class TestEncounter:
#    def test_encountersv15(self):
#        for version in [15, 16, 17, 18]:
#            csv_check("encountersv15.txt", parse_encounter, version=version)

#    def test_encountersv19(self):
#        for version in [19, 20]:
#            csv_check("encountersv19.txt", parse_encounter, version=version)
