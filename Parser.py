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

    def __init__(self, lines, object_class, attr_names, environment=None):
        self.lines = lines
        self.attr_names = attr_names
        self.object_class = object_class
        self.environment = environment
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
            if one_obj == "val":
                self.parsing_index += int(self.lines[self.parsing_index][0]) + 1
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
        kwargs = self.object_function(self.attr_names, lines)
        parsed_dict.update(kwargs)

        return self.object_class(**parsed_dict)


class ParsingSchemaPhone(ParsingSchema):
    def __init__(self, lines, object_class, attr_names, environment=None):
        super().__init__(lines, object_class, attr_names, environment)
        self.object_definition = ["[]"]

    def parse_object(self):
        kwargs_objects = {}
        obj = self.parse_one_object()
        while obj:
            kwargs_objects.update(obj)
            obj = self.parse_one_object()

        return self.object_class(**kwargs_objects)

    def apply_function_one_object(self, start_index, end_index):
        lines = self.lines[start_index:end_index]
        parsed_dict = {}
        kwargs = self.object_function(self.attr_names, lines)
        parsed_dict.update(kwargs)

        return parsed_dict

    def object_function(self, attr_names, lines):

        kwargs = dict()
        section_name = parse_bracket_header(lines[0][0])
        section_name = section_name.removesuffix(">")
        section_name = section_name.removeprefix("<")

        argument_translator = Phone.get_attr_dict()

        kwargs[argument_translator[section_name]] = lines[1:]
        return kwargs


class ParsingSchemaCsv(ParsingSchema):
    def __init__(self, lines, object_class, attr_names, environment=None):
        super().__init__(lines, object_class, attr_names, environment)
        self.object_definition = ["\n"]

    def object_function(self, attr_names, lines):
        line = lines[0]
        kwargs = dict()
        for name, value in zip(attr_names, line):
            kwargs[name] = value
        return kwargs


class ParsingSchemaTrainer(ParsingSchema):
    def __init__(self, lines, object_class, attr_names, environment=None):
        super().__init__(lines, object_class, attr_names, environment)
        self.object_definition = ["\n", "\n", "val"]

    def object_function(self, attr_names, lines):
        type = lines[0][0]
        name = lines[1][0]
        item_list = []
        pokemon_list = []
        if len(lines[1]) > 1:
            version_number = lines[1][1]
        else:
            version_number = ""

        nb_pokemon = lines[2][0]
        if len(lines[2]) > 1:
            item_list = []
            for item in lines[2][1:]:
                item_list.append(item)

        for line in lines[3:]:
            pkm = parse_trainer_pokemon(line, self.environment)
            pokemon_list.append(pkm)

        trainer_type = get_trainer_type_from_name(type, self.environment.trainer_type_list)
        kwargs = {
            "type": trainer_type,
            "name": name,
            "version_number": version_number,
            "item_list": item_list,
            "nb_pokemon": nb_pokemon,
            "pokemon_list": pokemon_list,
        }

        return kwargs


class ParsingSchemaShadow(ParsingSchema):
    def __init__(self, lines, object_class, attr_names, environment):
        super().__init__(lines, object_class, attr_names, environment)
        self.object_definition = ["\n"]

    def object_function(self, attr_names, lines):
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

    def __init__(self, lines, object_class, attr_names, environment=None):
        super().__init__(lines, object_class, attr_names, environment)
        self.object_definition = ["[]"]

    def object_function(self, attr_names, lines):
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
        value = super().parser_function(
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
        value = super().parser_function(
            first, second, attr_pbs_categories, obj_class, argument_translator
        )
        return value


class ParsingSchemaMetadata(ParsingSchemaEqual):
    def parser_function(self, first, second, attr_pbs_categories, obj_class, argument_translator):
        value = super().parser_function(
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


def parse_schema(lines, object_class, schema_class, attr_names=None, environement=None):
    if not attr_names:
        attr_names = object_class.get_attr_names()
    schema = schema_class(lines, object_class, attr_names, environement)
    return schema.parse_object()


def parse_ability(csv_output) -> list[ab.Ability]:
    return parse_schema(csv_output, ab.Ability, ParsingSchemaCsv)


def parser_move(csv_output) -> list[mv.Move]:
    return parse_schema(csv_output, mv.Move, ParsingSchemaCsv)


def parse_trainer_types(csv_output) -> list[tr.TrainerType]:
    return parse_schema(csv_output, tr.TrainerType, ParsingSchemaCsv)


def parse_connection(csv_output) -> list[Connection]:
    return parse_schema(csv_output, Connection, ParsingSchemaCsv)


def parse_item(csv_output, version) -> list[it.Item]:
    attr_names = it.Item.get_attr_names()
    if version < 16:
        attr_names.remove("name_plural")
    return parse_schema(csv_output, it.Item, ParsingSchemaCsv, attr_names)


def parse_shadow_pokemon(csv_output, environment) -> list[ShadowPokemon]:
    return parse_schema(csv_output, ShadowPokemon, ParsingSchemaShadow, environement=environment)


def parse_phone(csv_output):
    return parse_schema(csv_output, Phone, ParsingSchemaPhone)


def parse_type(equal_output):
    return parse_schema(equal_output, Type, ParsingSchemaEqual)


def parse_townmap(equal_output):
    return parse_schema(equal_output, TownMap, ParsingSchemaTownmap)


def parse_metadata(equal_output):
    return parse_schema(equal_output, MetaData, ParsingSchemaMetadata)


def parse_pokemon(equal_output) -> list[pk.Species]:
    return parse_schema(equal_output, pk.Species, ParsingSchemaPokemon)


def parse_trainer_list(csv_output, environment) -> list[tr.Trainer]:
    return parse_schema(csv_output, tr.Trainer, ParsingSchemaTrainer, environement=environment)


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


def parse_coma_equal_field(field):
    coma_list = field.split(",")
    return coma_list


def parse_bracket_header(line):
    result = re.search("\\[(.*)\\]", line)
    if result:
        return result.group(1)
    return None


def parse_one_line_coma(attr_names, line):
    kwargs = dict()
    for name, value in zip(attr_names, line):
        kwargs[name] = value
    return kwargs
