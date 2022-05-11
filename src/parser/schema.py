from typing import List, Callable, Dict

from PBSclasses import Encounter as en, TrainerPokemon as pk
from PBSclasses.MetaData import PlayerMetaData
from PBSclasses.Phone import PhoneV15
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


def separate_file(lines, find_next_function):
    lines_separated = []
    start_index = 0
    end_index = 0
    max_index = len(lines)
    while end_index < max_index:
        end_index = find_next_function(lines, start_index)
        lines_separated.append(lines[start_index:end_index])
        start_index = end_index
    return lines_separated


def separate_equal(lines):
    return separate_file(lines, find_next_index)


def find_next_trainer(lines, start_index):
    nb_pkm = int(lines[start_index + 2][0])
    return start_index + 3 + nb_pkm


def separate_trainers(lines):
    return separate_file(lines, find_next_trainer)


def find_next_encounter(lines, start_index):
    start_index += 1
    while start_index < len(lines):
        one = len(lines[start_index]) == 1
        dec = lines[start_index][0][0:3].isdecimal()
        if dec and one:
            break
        start_index += 1
    return start_index


def find_next_encounter_by_method(lines, start_index):
    start_index += 1
    while start_index < len(lines):
        one = len(lines[start_index]) == 1
        if one:
            break
        start_index += 1
    return start_index


def separate_encounters(lines):
    separated_encounters = separate_file(lines, find_next_encounter)
    new_line = []
    for encounters in separated_encounters:
        new_line.append(separate_encounters_by_methods(encounters))
    return new_line


def separate_encounters_by_methods(lines):
    return separate_file(lines, find_next_encounter_by_method)
