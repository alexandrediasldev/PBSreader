from typing import List, Callable, Dict

from PBSclasses import Encounter as en, Pokemon as pk
from PBSclasses.MetaData import PlayerMetaData
from PBSclasses.Phone import Phone
from PBSclasses.TownMap import TownPoint
from src.Finder import get_encounter_method_from_name, get_species_from_name
from src.parser.parse_utils import parse_coma_equal_field, parse_bracket_header, parse_one_line_coma


def find_next_index(lines, start_index):
    max_index = len(lines)
    index = start_index
    while index < max_index and not parse_bracket_header(lines[index][0]):
        index += 1
    index += 1
    while index < max_index and not parse_bracket_header(lines[index][0]):
        index += 1
    return index


def separate_equal(lines):
    lines_separated = []
    start_index = 0
    end_index = 0
    max_index = len(lines)
    while end_index < max_index:
        end_index = find_next_index(lines, start_index)
        lines_separated.append(lines[start_index:end_index])
        start_index = end_index
    return lines_separated


class FileSpliter:
    def __init__(self, lines, object_definition):
        self.lines = lines
        self.object_definition = object_definition
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
        if start_index >= len(self.lines):
            return None
        for one_obj in self.object_definition:
            start_index, end_index = self.move_index(one_obj, start_index, end_index)

        return self.lines[start_index : self.parsing_index]

    def move_index(self, move_type, start_index, end_index):
        max_index = len(self.lines)
        if move_type == "\n":
            self.parsing_index += 1
        if move_type == "val":
            self.parsing_index += int(self.lines[self.parsing_index][0]) + 1
        if move_type == "[]":
            while end_index < max_index and not parse_bracket_header(self.lines[end_index][0]):
                start_index += 1
                end_index += 1
            end_index += 1
            while end_index < max_index and not parse_bracket_header(self.lines[end_index][0]):
                end_index += 1
            self.parsing_index = end_index
        if move_type == "int":
            self.parsing_index += 1
            for line in self.lines[self.parsing_index :]:
                num = line[0].split("#")[0].rstrip()
                if self.parsing_index > max_index or ((len(line) == 1 and num.isnumeric())):
                    break
                self.parsing_index += 1
        if move_type == "single":
            self.parsing_index += 1
            for line in self.lines[self.parsing_index :]:
                if self.parsing_index > max_index or (len(line) == 1):
                    break
                self.parsing_index += 1

        return start_index, end_index


class ParsingSchema:
    object_function: Callable
    attr_names: Dict
    object_class: str

    def __init__(self, object_class, attr_names, environment=None):
        self.attr_names = attr_names
        self.object_class = object_class
        self.environment = environment

    def apply_function_one_object(self, lines):
        parsed_dict = {}
        kwargs = self.object_function(self.attr_names, lines)
        parsed_dict.update(kwargs)

        return self.object_class(**parsed_dict)


class ParsingSchemaPhone(ParsingSchema):
    def apply_function_one_object(self, lines):
        parsed_dict = {}
        for line in lines:
            kwargs = self.object_function(self.attr_names, line)
            parsed_dict.update(kwargs)

        return self.object_class(**parsed_dict)

    def object_function(self, attr_names, lines):

        kwargs = dict()
        section_name = parse_bracket_header(lines[0][0])
        section_name = section_name.removesuffix(">")
        section_name = section_name.removeprefix("<")

        argument_translator = Phone.get_attr_dict()

        kwargs[argument_translator[section_name]] = lines[1:]
        return kwargs


class ParsingSchemaCsv(ParsingSchema):
    def object_function(self, attr_names, lines):
        line = lines[0]
        kwargs = dict()
        for name, value in zip(attr_names, line):
            kwargs[name] = value
        return kwargs


class ParsingSchemaEncounter(ParsingSchema):
    def __init__(self, object_class, attr_names, environment=None, encounter_methods=None):
        super().__init__(object_class, attr_names, environment)
        self.encounter_methods = encounter_methods

    def object_function(self, attr_names, lines):
        encounter_density = ["25", "10", "10"] if len(lines[1]) == 1 else lines[1]
        starting_index = 1 if len(lines[1]) == 1 else 2

        f = FileSpliter(lines[starting_index:], ["single"])
        sc = ParsingSchemaCsv(en.Encounter, en.Encounter.get_attr_names())

        encounter_list = []
        for encounter_zone in f.parse_object():
            encou_method = encounter_zone[0][0]
            probability_index = 0
            for encounter_line in encounter_zone[1:]:
                encounter_method = get_encounter_method_from_name(
                    encou_method, self.encounter_methods
                )
                encounter_probability = encounter_method.probability_of_encounter[probability_index]
                csv_encounter_line = [[str(encounter_probability), encou_method] + encounter_line]
                encounter_list.append(sc.apply_function_one_object(csv_encounter_line))
                probability_index += 1

        kwargs = parse_one_line_coma(attr_names, [lines[0][0], encounter_density, encounter_list])

        return kwargs


class ParsingSchemaTrainer(ParsingSchema):
    def _parse_trainer_pokemon(self, pokemon_attributes) -> pk.Pokemon:
        attr_names = pk.Pokemon.get_attr_names()
        moves = pokemon_attributes[3:7]
        pokemon_attributes = pokemon_attributes[:3] + pokemon_attributes[7:]
        attr_names.remove("move_list")
        kwargs = parse_one_line_coma(attr_names, pokemon_attributes)
        kwargs["move_list"] = moves

        return pk.Pokemon(**kwargs)

    def object_function(self, attr_names, lines):
        coma_line = []
        coma_line.append(lines[0][0])
        coma_line.append(lines[1][0])
        coma_line.append(lines[1][1] if len(lines[1]) > 1 else "")
        coma_line.append(lines[2][1:])
        coma_line.append(lines[2][0])
        coma_line.append([self._parse_trainer_pokemon(line) for line in lines[3:]])

        kwargs = parse_one_line_coma(attr_names, coma_line)

        return kwargs


class ParsingSchemaEqual(ParsingSchema):
    def value_handler(self, kwargs, argument_translator, first, value):
        kwargs[argument_translator[first]] = value

    def value_inside_bracket(self, kwargs, argument_translator, value):
        self.value_handler(kwargs, argument_translator, "Id", value)

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

    def object_function(self, attr_names, lines):
        attr_pbs_categories = self.object_class.get_attr_pbs_by_types()
        argument_translator = self.object_class.get_attr_dict()
        kwargs = dict()

        self.value_inside_bracket(kwargs, argument_translator, parse_bracket_header(lines[0][0]))
        for line in lines[1:]:
            first, second = line[0], line[1]
            value = self.parser_function(
                first, second, attr_pbs_categories, self.object_class, argument_translator
            )
            if value:
                self.value_handler(kwargs, argument_translator, first, value)
        return kwargs


def value_handler_append(kwargs, argument_translator, first, value, attr_name):
    if first.startswith(attr_name):
        first = attr_name
        if argument_translator[first] not in kwargs:
            kwargs[argument_translator[first]] = []
        kwargs[argument_translator[first]].append(value)
    else:
        kwargs[argument_translator[first]] = value


class ParsingSchemaTownmap(ParsingSchemaEqual):
    def parser_function(self, first, second, attr_pbs_categories, obj_class, argument_translator):
        if first == "Point":
            return TownPoint(
                **parse_one_line_coma(TownPoint.get_attr_names(), parse_coma_equal_field(second))
            )
        value = super().parser_function(
            first, second, attr_pbs_categories, obj_class, argument_translator
        )
        return value

    def value_handler(self, kwargs, argument_translator, first, value):
        return value_handler_append(kwargs, argument_translator, first, value, "Point")


class ParsingSchemaMetadata(ParsingSchemaEqual):
    def parser_function(self, first, second, attr_pbs_categories, obj_class, argument_translator):
        if first.startswith("Player"):
            return PlayerMetaData(
                **parse_one_line_coma(
                    PlayerMetaData.get_attr_names(), parse_coma_equal_field(second)
                )
            )
        value = super().parser_function(
            first, second, attr_pbs_categories, obj_class, argument_translator
        )
        return value

    def value_handler(self, kwargs, argument_translator, first, value):
        return value_handler_append(kwargs, argument_translator, first, value, "Player")


class ParsingSchemaPokemon(ParsingSchemaEqual):
    def parser_function(self, first, second, attr_pbs_categories, obj_class, argument_translator):
        if first == "Moves":
            return self._parse_pokemon_move(second)
        value = super().parser_function(
            first, second, attr_pbs_categories, obj_class, argument_translator
        )
        return value

    def _parse_pokemon_move(self, moves):
        moves_and_level = moves.split(",")
        level_moves = []
        for i in range(0, len(moves_and_level), 2):
            level = moves_and_level[i]
            if i + 1 < len(moves_and_level):
                move = moves_and_level[i + 1]
                level_moves.append((level, move))
        return level_moves
