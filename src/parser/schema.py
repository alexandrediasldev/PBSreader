from typing import List, Callable, Dict

from PBSclasses import Encounter as en, Pokemon as pk
from PBSclasses.MetaData import PlayerMetaData
from PBSclasses.Phone import Phone
from PBSclasses.TownMap import TownPoint
from src.Finder import get_encounter_method_from_name, get_species_from_name
from src.parser.parse_utils import parse_coma_equal_field, parse_bracket_header, parse_one_line_coma


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
            if one_obj == "int":
                self.parsing_index += 1
                for line in self.lines[self.parsing_index :]:
                    num = line[0].split("#")[0].rstrip()
                    if self.parsing_index > max_index or ((len(line) == 1 and num.isnumeric())):
                        break
                    self.parsing_index += 1

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


class ParsingSchemaEncounter(ParsingSchema):
    def __init__(self, lines, object_class, attr_names, environment=None, encounter_methods=None):
        super().__init__(lines, object_class, attr_names, environment)
        self.encounter_methods = encounter_methods
        self.object_definition = ["int"]

    def object_function(self, attr_names, lines):
        comma_line = []
        encounter_list = []

        comma_line.append(lines[0][0])

        index = 1
        if len(lines[index]) == 1:
            encounter_density = ["25", "10", "10"]
        else:
            encounter_density = lines[1]
            index += 1
        encounter_method = None
        comma_line.append(encounter_density)
        index_map = 0
        for line in lines[index:]:
            if len(line) == 1:
                index_map = 0
                encounter_method = get_encounter_method_from_name(line[0], self.encounter_methods)
            else:
                proba = encounter_method.probability_of_encounter[index_map]
                species, level_low = line[0], line[1]
                level_high = line[2] if len(line) > 2 else ""
                encounter_list.append(
                    en.Encounter(
                        proba, encounter_method.method_name, species, level_low, level_high
                    )
                )
                index_map += 1

        comma_line.append(encounter_list)

        kwargs = parse_one_line_coma(attr_names, comma_line)

        return kwargs


class ParsingSchemaTrainer(ParsingSchema):
    def __init__(self, lines, object_class, attr_names, environment=None):
        super().__init__(lines, object_class, attr_names, environment)
        self.object_definition = ["\n", "\n", "val"]

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
