import re
from typing import List, Callable, Dict

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


class ParsingSchema:
    object_definition: List[str]
    object_function: List[Callable]
    attr_names: Dict
    object_class: str
    lines: List[str]
    parsing_index: int

    def __init__(self, lines, object_class, attr_names):
        self.lines = lines
        self.attr_names = attr_names
        self.object_class = object_class
        self.parsing_index = 0

    def parse_object(self):
        parsed_object = []
        obj = self.parse_one_object()
        while obj:
            parsed_object.append(obj)
            obj = self.parse_one_object()

        return parsed_object

    def parse_one_object(self):
        start_index = self.parsing_index
        end_index = start_index
        max_index = len(self.lines)
        if start_index >= len(self.lines):
            return None
        for one_obj in self.object_definition:
            if one_obj == "\n":
                self.parsing_index += 1
            if one_obj == "[]":
                while end_index < max_index and not parse_bracket_header(self.lines[end_index][0]):
                    start_index += 1
                    end_index += 1
                end_index += 1
                while end_index < max_index and not parse_bracket_header(self.lines[end_index][0]):
                    end_index += 1
                self.parsing_index = end_index

        return self.apply_function_one_object(start_index, self.parsing_index)

    def apply_function_one_object(self, start_index, end_index):
        lines = self.lines[start_index:end_index]
        parsed_dict = {}
        for function in self.object_function:
            kwargs = function(self.attr_names, lines)
            parsed_dict.update(kwargs)

        return self.object_class(**parsed_dict)


class ParsingSchemaCsv(ParsingSchema):
    def __init__(self, lines, object_class, attr_names):
        super().__init__(lines, object_class, attr_names)
        self.object_definition = ["\n"]
        self.object_function = [self.parse_one_line_coma]

    def parse_one_line_coma(self, attr_names, lines):
        line = lines[0]
        kwargs = dict()
        for name, value in zip(attr_names, line):
            kwargs[name] = value
        return kwargs


class ParsingSchemaShadow(ParsingSchema):
    def __init__(self, lines, object_class, attr_names, environment):
        super().__init__(lines, object_class, attr_names)
        self.environment = environment
        self.object_definition = ["\n"]
        self.object_function = [self.parse_one_line_shadow]

    def parse_one_line_shadow(self, attr_names, lines):
        kwargs = dict()
        line = lines[0]
        first, second = line[0], line[1]
        kwargs[attr_names[0]] = get_species_from_name(first, self.environment.species_list)
        kwargs[attr_names[1]] = parse_coma_equal_field(second)
        return kwargs


class ParsingSchemaEqual(ParsingSchema):
    def value_handler(self, kwargs, argument_translator, first, value):
        kwargs[argument_translator[first]] = value

    def parser_function(self, first, second, attr_pbs_categories, obj_class, argument_translator):
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

    def __init__(self, lines, object_class, attr_names):
        super().__init__(lines, object_class, attr_names)
        self.object_definition = ["[]"]
        self.object_function = [self.parse_one_line_equal]

    def parse_one_line_equal(self, attr_names, lines):
        attr_pbs_categories = self.object_class.get_attr_pbs_by_types()
        argument_translator = self.object_class.get_attr_dict()
        kwargs = dict()

        kwargs["id"] = parse_bracket_header(lines[0][0])
        for line in lines[1:]:
            first, second = line[0], line[1]
            value = self.parser_function(
                first, second, attr_pbs_categories, self.object_class, argument_translator
            )
            if value:
                self.value_handler(kwargs, argument_translator, first, value)
        return kwargs


class ParsingSchemaTownmap(ParsingSchemaEqual):
    def parser_function(self, first, second, attr_pbs_categories, obj_class, argument_translator):
        value = _parse_object_one_line(
            first, second, attr_pbs_categories, obj_class, argument_translator
        )
        if not value:
            if first in ["Point"]:
                value = TownPoint(
                    **parse_one_line_coma(
                        TownPoint.get_attr_names(), parse_coma_equal_field(second)
                    )
                )
        return value

    def value_handler(self, kwargs, argument_translator, first, value):
        if "Point" == first:
            if "points" not in kwargs:
                kwargs["points"] = []
            kwargs["points"].append(value)
        else:
            kwargs[argument_translator[first]] = value


class ParsingSchemaPokemon(ParsingSchemaEqual):
    def parser_function(self, first, second, attr_pbs_categories, obj_class, argument_translator):
        if first == "Moves":
            return parse_pokemon_move(second)
        value = _parse_object_one_line(
            first, second, attr_pbs_categories, obj_class, argument_translator
        )
        return value


class ParsingSchemaMetadata(ParsingSchemaEqual):
    def parser_function(self, first, second, attr_pbs_categories, obj_class, argument_translator):
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

    def value_handler(self, kwargs, argument_translator, first, value):
        if first.startswith("Player"):
            if "players" not in kwargs:
                kwargs["players"] = []
            kwargs["players"].append(value)
        else:
            kwargs[argument_translator[first]] = value


def equal_value_handler(kwargs, argument_translator, first, value):
    kwargs[argument_translator[first]] = value


def parse_schema_equal(lines, object_class, schema_class=ParsingSchemaEqual, attr_names=None):
    if not attr_names:
        attr_names = object_class.get_attr_names()
    schema = schema_class(lines, object_class, attr_names)
    return schema.parse_object()


def parse_schema_csv(lines, object_class, attr_names=None):

    if not attr_names:
        attr_names = object_class.get_attr_names()
    schema = ParsingSchemaCsv(lines, object_class, attr_names)
    return schema.parse_object()


def parse_schema_shadow(lines, object_class, environment, attr_names=None):
    if not attr_names:
        attr_names = object_class.get_attr_names()
    schema = ParsingSchemaShadow(lines, object_class, attr_names, environment)
    return schema.parse_object()


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
    return parse_schema_csv(csv_output, ab.Ability)


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
    return parse_schema_csv(csv_output, it.Item, attr_names)


def parse_shadow_pokemon(csv_output, environment) -> list[ShadowPokemon]:
    return parse_schema_shadow(csv_output, ShadowPokemon, environment=environment)


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
    return parse_schema_equal(equal_output, Type)


def parse_townmap(equal_output):
    return parse_schema_equal(equal_output, TownMap, ParsingSchemaTownmap)


def parse_metadata(equal_output):
    return parse_schema_equal(equal_output, MetaData, ParsingSchemaMetadata)


def parse_pokemon(equal_output) -> list[pk.Species]:
    return parse_schema_equal(equal_output, pk.Species, ParsingSchemaPokemon)


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
