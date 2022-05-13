# convert line to format
from PBSclasses.Encounter import EncounterPokemon, EncounterByMethod
from PBSclasses.MetaData import PlayerMetaData, HomeMetaData
from PBSclasses.SpeciesEvolution import SpeciesEvolution
from PBSclasses.SpeciesStats import SpeciesStats
from PBSclasses.TownMap import TownPoint
from src.parser.parse_utils import (
    parse_bracket_header,
    append_value_kwargs,
    parse_equal_name_value,
    parse_one_line_coma,
)
from src.parser.single_line_files import get_kwargs_from_line_csv


def parse_all_section(
    lines, object_class, parse_one_section_header_function, parse_one_section_body_function
):
    list_obj = []
    for line in lines:
        kwargs = parse_one_section_header_function(line, object_class)
        obj = parse_one_section_body_function(line, object_class, kwargs)
        list_obj.append(obj)
    return list_obj


# HEADER
# [value]
def parse_bracket_section_header(lines, object_class):
    kwargs = {}
    kwargs[object_class.get_attr_names()[0]] = parse_bracket_header(lines[0][0])
    return kwargs


# value
def parse_full_section_header(lines, object_class):
    kwargs = {}
    kwargs[object_class.get_attr_names()[0]] = lines[0][0]
    return kwargs


def parse_pokemon_form_section_header(lines, object_class):
    kwargs = {}
    header = parse_bracket_header(lines[0][0])
    if "-" in header:
        header = header.split("-")
    elif "," in header:
        header = header.split(",")
    else:
        header = header.split(" ")
    kwargs["id"] = header[0]
    kwargs["id_number"] = header[1]
    return kwargs


def parse_encounter_map_section_header(lines, object_class):
    kwargs = {}
    kwargs[object_class.get_attr_names()[0]] = lines[0][0][0]
    kwargs[object_class.get_attr_names()[1]] = lines[0][1]
    return kwargs


# BODY
def parse_one_line_coma_section_body(lines, object_class, kwargs):
    next_lines = ""
    for line in lines[1:]:
        if line[0][-1] != "," and next_lines:
            next_lines += ","
        next_lines += line[0]

    kwargs[object_class.get_attr_names()[1]] = next_lines.split(",")
    return object_class(**kwargs)


def parse_metadata_section_body(lines, object_class, kwargs):
    argument_translator = object_class.get_attr_dict()
    for line in lines[1:]:
        if line[0] == "Home":
            value = HomeMetaData(
                **get_kwargs_from_line_csv(HomeMetaData.get_attr_names(), line[1].split(","))
            )
            kwargs[argument_translator[line[0]]] = value
        elif line[0].startswith("Player"):
            pmd = PlayerMetaData.get_attr_names()
            p = PlayerMetaData(**get_kwargs_from_line_csv(pmd, line[1].split(",")))
            append_value_kwargs(kwargs, line[0], p, "Player", argument_translator)
        else:
            value = parse_equal_name_value(line[0], line[1], object_class)
            kwargs[argument_translator[line[0]]] = value
    return object_class(**kwargs)


def parse_pokemon_section_body(lines, object_class, kwargs):
    argument_translator = object_class.get_attr_dict()
    for line in lines[1:]:
        if line[0] == "Moves":
            moves_and_level = line[1].split(",")
            value = []
            for i in range(0, len(moves_and_level), 2):
                level = moves_and_level[i]
                if i + 1 < len(moves_and_level):
                    move = moves_and_level[i + 1]
                    value.append((level, move))
            kwargs[argument_translator[line[0]]] = value
        elif line[0] in ["BaseStats", "EffortPoints", "Evolutions"]:
            if line[0] == "BaseStats" or line[0] == "EffortPoints":
                sub_class = SpeciesStats
            else:
                sub_class = SpeciesEvolution
            value = sub_class(
                **get_kwargs_from_line_csv(sub_class.get_attr_names(), line[1].split(","))
            )
            kwargs[argument_translator[line[0]]] = value
        else:
            value = parse_equal_name_value(line[0], line[1], object_class)
            kwargs[argument_translator[line[0]]] = value
    return object_class(**kwargs)


def parse_townmap_section_body(lines, object_class, kwargs):
    argument_translator = object_class.get_attr_dict()
    for line in lines[1:]:
        if line[0] == "Point":
            value = TownPoint(
                **get_kwargs_from_line_csv(TownPoint.get_attr_names(), line[1].split(","))
            )

            append_value_kwargs(kwargs, line[0], value, "Point", argument_translator)
        else:
            value = parse_equal_name_value(line[0], line[1], object_class)
            kwargs[argument_translator[line[0]]] = value
    return object_class(**kwargs)


def parse_equal_section_body(lines, object_class, kwargs):
    argument_translator = object_class.get_attr_dict()
    for line in lines[1:]:
        value = parse_equal_name_value(line[0], line[1], object_class)
        kwargs[argument_translator[line[0]]] = value
    return object_class(**kwargs)


def parse_encounter_method_section_body(lines, object_class, kwargs):
    encounter_method_name = lines[0][0]
    pokemon_list = []
    for encounter_pokemon_lines in lines[1:]:
        pokemon_list.append(
            EncounterPokemon(
                **parse_one_line_coma(EncounterPokemon.get_attr_names(), encounter_pokemon_lines)
            )
        )
    return object_class(encounter_method_name, pokemon_list)


def parse_encounter_map_section_body(lines, object_class, kwargs):
    kwargs[object_class.get_attr_names()[2]] = parse_all_section(
        lines[1:], EncounterByMethod, parse_full_section_header, parse_encounter_method_section_body
    )
    return object_class(**kwargs)
