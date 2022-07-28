from typing import List, Callable, Dict

from PBSclasses import Encounter as en, TrainerPokemon as pk
from PBSclasses.MetaData import PlayerMetaDataV15
from PBSclasses.Phone import PhoneV15
from PBSclasses.TownMap import TownPoint
from src.Finder import get_encounter_method_from_name, get_species_from_name
from src.parser.parse_utils import parse_bracket_header, parse_one_line_coma


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


# Trainer
def find_next_trainerv15(lines, start_index):
    nb_pkm = int(lines[start_index + 2][0])
    return start_index + 3 + nb_pkm


def separate_trainersv15(lines):
    line_separated = separate_file(lines, find_next_trainerv15)

    for trainer in line_separated:
        for i in range(len(trainer[3:])):
            trainer[3 + i] = trainer[3 + i][:3] + [trainer[3 + i][3:7]] + trainer[3 + i][7:]

    return line_separated


def find_next_trainerv18(lines, start_index):
    start_index += 1
    while start_index < len(lines):
        pkm = lines[start_index][0]
        if pkm == "Pokemon":
            break
        start_index += 1
    return start_index


def separate_trainersv18(lines):
    separated_trainers = separate_file(lines, find_next_index)
    new_line = []
    for trainers in separated_trainers:
        new_line.append(separate_file(trainers, find_next_trainerv18))
    return new_line


# Encounter
def find_next_encounterv15(lines, start_index):
    start_index += 1
    while start_index < len(lines):
        one = len(lines[start_index]) == 1
        dec = lines[start_index][0][0:3].isdecimal()
        if dec and one:
            break
        start_index += 1
    return start_index


def find_next_encounter_by_methodv15(lines, start_index):
    start_index += 1
    while start_index < len(lines):
        one = len(lines[start_index]) == 1
        if one:
            break
        start_index += 1
    return start_index


def separate_encounters_by_methodsv15(lines):
    return separate_file(lines, find_next_encounter_by_methodv15)


def separate_encountersv15(lines):
    separated_encounters = separate_file(lines, find_next_encounterv15)
    new_line = []
    for encounters in separated_encounters:
        new_line.append(separate_encounters_by_methodsv15(encounters))
    return new_line


def find_next_encounter_by_methodv19(lines, start_index):
    start_index += 1
    while start_index < len(lines):
        lower_than_two = len(lines[start_index]) == 2 or len(lines[start_index]) == 1
        if lower_than_two:
            break
        start_index += 1
    return start_index


def separate_encounters_by_methodsv19(lines):
    return separate_file(lines, find_next_encounter_by_methodv19)


def separate_encountersv19(lines):
    separated_encounters = separate_file(lines, find_next_index)
    new_line = []
    for encounters in separated_encounters:
        new_line.append(separate_encounters_by_methodsv19(encounters))
    return new_line
