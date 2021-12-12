import re

import PBSclasses.Trainers as tr
import PBSclasses.Pokemon as pk
import PBSclasses.Move as mv
import PBSclasses.Item as it
import PBSclasses.Encounter as en
import PBSclasses.EncounterMethod as enm
import PBSclasses.Ability as ab
from Finder import (
    get_encounter_method_from_name,
    get_species_from_name,
    get_item_from_name,
    get_move_from_name,
    get_trainer_type_from_name,
)
from PBSclasses import Species
from PBSclasses.Connection import Connection
from PBSclasses.MetaData import MetaData, PlayerMetaData
from PBSclasses.Phone import Phone
from PBSclasses.ShadowPokemon import ShadowPokemon

from PBSclasses.TownMap import TownMap, TownPoint
from PBSclasses.Type import Type


def parse_one_line_coma(attr_names, line):
    kwargs = dict()
    for name, value in zip(attr_names, line):
        kwargs[name] = value
    return kwargs


def parse_simple_csv(csv_output, object_class, attr_names=None):
    object_list = []
    if not attr_names:
        attr_names = object_class.get_attr_names()
    for line in csv_output:
        kwargs = parse_one_line_coma(attr_names, line)
        obj = object_class(**kwargs)
        # deserialized = deserialize_simple_csv(obj)
        # line_joined = ','.join(line)
        # if deserialized != line_joined:
        #    print("WARNING SERIALIZATION:")
        #    print(line_joined)
        #    print(deserialized)

        object_list.append(obj)

    return object_list


def parse_ability(csv_output) -> list[ab.Ability]:
    return parse_simple_csv(csv_output, ab.Ability)


def parser_move(csv_output) -> list[mv.Move]:
    return parse_simple_csv(csv_output, mv.Move)


def parse_trainer_types(csv_output) -> list[tr.TrainerType]:
    return parse_simple_csv(csv_output, tr.TrainerType)


def parse_connection(csv_output) -> list[Connection]:
    return parse_simple_csv(csv_output, Connection)


def parse_item(csv_output, version) -> list[it.Item]:
    attr_names = it.Item.get_attr_names()
    if version < 16:
        attr_names.remove("name_plural")
    return parse_simple_csv(csv_output, it.Item, attr_names)


def parse_shadow_pokemon(csv_output, environment) -> list[ShadowPokemon]:
    attr_names = ShadowPokemon.get_attr_names()
    kwargs = dict()
    shadow_list = []
    for line in csv_output:
        first, second = line[0], line[1]
        kwargs[attr_names[0]] = get_species_from_name(first, environment.species_list)
        kwargs[attr_names[1]] = parse_coma_equal_field(second)
        shadow_list.append(ShadowPokemon(**kwargs))
    return shadow_list


def parse_phone(csv_output):
    kwargs = dict()
    phone_lines = []
    section_name = None
    argument_translator = Phone.get_attr_dict()
    for line in csv_output:
        first = line[0]
        if parse_bracket_header(first):
            if section_name:
                kwargs[argument_translator[section_name]] = phone_lines
            phone_lines = []
            section_name = parse_bracket_header(first)
            section_name = section_name.removesuffix(">")
            section_name = section_name.removeprefix("<")
        else:
            phone_lines.append(first)
    kwargs[argument_translator[section_name]] = phone_lines

    return Phone(**kwargs)


def _parse_townmap_one_line(first, second, attr_pbs_categories, obj_class, argument_translator):
    value = _parse_object_one_line(
        first, second, attr_pbs_categories, obj_class, argument_translator
    )
    if not value:
        if first in ["Point"]:
            value = TownPoint(
                **parse_one_line_coma(TownPoint.get_attr_names(), parse_coma_equal_field(second))
            )
    return value


def _parse_metadata_one_line(first, second, attr_pbs_categories, obj_class, argument_translator):
    value = _parse_object_one_line(
        first, second, attr_pbs_categories, obj_class, argument_translator
    )
    if not value:
        if first.startswith("Player"):
            value = PlayerMetaData(
                **parse_one_line_coma(
                    PlayerMetaData.get_attr_names(), parse_coma_equal_field(second)
                )
            )
    return value


def _parse_pokemon_one_line(first, second, attr_pbs_categories, obj_class, argument_translator):
    if first == "Moves":
        return parse_pokemon_move(second)
    value = _parse_object_one_line(
        first, second, attr_pbs_categories, obj_class, argument_translator
    )
    return value


def custom_value_handler_townmap(kwargs, argument_translator, first, value):
    if "Point" == first:
        if "points" not in kwargs:
            kwargs["points"] = []
        kwargs["points"].append(value)
    else:
        kwargs[argument_translator[first]] = value


def custom_value_handler_metadata(kwargs, argument_translator, first, value):
    if first.startswith("Player"):
        if "players" not in kwargs:
            kwargs["players"] = []
        kwargs["players"].append(value)
    else:
        kwargs[argument_translator[first]] = value


def equal_value_handler(kwargs, argument_translator, first, value):
    kwargs[argument_translator[first]] = value


def _parse_object_one_line(first, second, attr_pbs_categories, obj_class, argument_translator):
    attr_pbs_string, attr_pbs_list, attr_pbs_basedata = attr_pbs_categories
    if first in attr_pbs_string:
        return second
    elif first in attr_pbs_list:
        return parse_coma_equal_field(second)
    elif first in attr_pbs_basedata:
        sub_class = obj_class.get_attr_class(argument_translator[first])
        return sub_class(
            **parse_one_line_coma(sub_class.get_attr_names(), parse_coma_equal_field(second))
        )
    return None


def parse_section_equal_file(
    equal_output, obj_class, _parse_one_line, value_handler=equal_value_handler
):
    attr_pbs_categories = obj_class.get_attr_pbs_by_types()
    obj_list = []
    kwargs = dict()
    id = -1
    argument_translator = obj_class.get_attr_dict()
    for line in equal_output:
        first = line[0]
        second = None
        if len(line) > 1:
            second = line[1]
        if parse_bracket_header(first):
            if id != -1:
                kwargs["id"] = id
                obj = obj_class(**kwargs)
                obj_list.append(obj)
                kwargs = dict()
            id = parse_bracket_header(first)
        else:
            value = _parse_one_line(
                first, second, attr_pbs_categories, obj_class, argument_translator
            )
            if value:
                value_handler(kwargs, argument_translator, first, value)

    kwargs["id"] = id
    obj = obj_class(**kwargs)
    obj_list.append(obj)

    return obj_list


def parse_type(equal_output):
    return parse_section_equal_file(
        equal_output, obj_class=Type, _parse_one_line=_parse_object_one_line
    )


def parse_townmap(equal_output):
    return parse_section_equal_file(
        equal_output,
        obj_class=TownMap,
        _parse_one_line=_parse_townmap_one_line,
        value_handler=custom_value_handler_townmap,
    )


def parse_metadata(equal_output):
    return parse_section_equal_file(
        equal_output,
        obj_class=MetaData,
        _parse_one_line=_parse_metadata_one_line,
        value_handler=custom_value_handler_metadata,
    )


def parse_pokemon(equal_output) -> list[Species]:
    return parse_section_equal_file(
        equal_output, obj_class=pk.Species, _parse_one_line=_parse_pokemon_one_line
    )


def parse_encounter(
    csv_output, encounter_methods: list[enm.EncounterMethod], environment
) -> list[en.Encounter]:
    encounter_list = []
    len_csv = len(csv_output)
    i = 0
    while i < len_csv:
        line = csv_output[i]
        if len(line) == 1:
            is_map_name = True
            method_tmp = get_encounter_method_from_name(line[0], encounter_methods)
            if method_tmp != "":
                method = method_tmp
                is_map_name = False

            if is_map_name:
                map_name = line[0]
                i += 1
                if i < len_csv:
                    line = csv_output[i]
                    if len(line) == 1:
                        encounter_density = ["25", "10", "10"]
                    else:
                        encounter_density = line

        elif len(line) == 2:
            species = get_species_from_name(line[0], environment.species_list)
            level_low = line[1]
            level_high = ""
            encounter_list.append(
                en.Encounter(map_name, encounter_density, method, species, level_low, level_high)
            )
        else:
            species = get_species_from_name(line[0], environment.species_list)
            level_low = line[1]
            level_high = line[2]
            encounter_list.append(
                en.Encounter(map_name, encounter_density, method, species, level_low, level_high)
            )
        i += 1

    return encounter_list


def parse_pokemon_move(moves):
    moves_and_level = moves.split(",")
    level_moves = []
    for i in range(0, len(moves_and_level), 2):
        level = moves_and_level[i]
        if i + 1 < len(moves_and_level):
            move = moves_and_level[i + 1]
            level_moves.append((level, move))
    return level_moves


def parse_coma_equal_field(field):
    coma_list = field.split(",")
    return coma_list


def parse_bracket_header(line):
    result = re.search("\\[(.*)\\]", line)
    if result:
        return result.group(1)
    return None


def parse_trainer_pokemon(pokemon_attributes, environment) -> pk.Pokemon:
    attr_names = pk.Pokemon.get_attr_names()
    kwargs = dict()
    attribute_index = 0
    for i in range(len(pokemon_attributes)):
        attribute = pokemon_attributes[i]
        if i == 0:
            value = get_species_from_name(attribute, environment.species_list)
        elif i == 1 or (i > 6 and i < 14):
            value = attribute
        elif i == 2:
            value = get_item_from_name(attribute, environment.item_list)
        elif i == 3:
            move_list = []
            for i in range(3, 7):
                if i >= len(pokemon_attributes):
                    break
                move_name = pokemon_attributes[i]
                if move_name != "":
                    move_list.append(get_move_from_name(move_name, environment.move_list))
            value = move_list

        if i < 14:
            kwargs[attr_names[attribute_index]] = value
            attribute_index += 1
    return pk.Pokemon(**kwargs)


def parse_trainer_list(csv_output, environment) -> list[tr.Trainer]:
    line_num = 0
    pokemon_list = []
    trainer_list = []
    item_list: list[str] = []
    for line in csv_output:
        if line_num == 0:
            type = line[0]
        elif line_num == 1:
            name = line[0]
            if len(line) > 1:
                version_number = line[1]
            else:
                version_number = ""
        elif line_num == 2:
            nb_pokemon = line[0]
            if len(line) > 1:
                item_list = []
                for item in line[1:]:
                    item_list.append(item)

        else:
            if int(nb_pokemon) + 2 == line_num:
                pkm = parse_trainer_pokemon(line, environment)
                pokemon_list.append(pkm)

                trainer_type = get_trainer_type_from_name(type, environment.trainer_type_list)
                train = tr.Trainer(
                    trainer_type, name, version_number, item_list, nb_pokemon, pokemon_list
                )
                trainer_list.append(train)

                pokemon_list = []
                line_num = -1
            else:
                pkm = parse_trainer_pokemon(line, environment)
                pokemon_list.append(pkm)
        line_num += 1
    return trainer_list
