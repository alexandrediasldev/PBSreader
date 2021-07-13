from typing import Dict, List, Tuple


def print_if_value(text, value):
    if (value != ""):
        print(text, value)


def find_sizes_of_subplots(number_of_plot) -> Tuple[int, int]:
    i = 0
    j = 0
    while i * j < number_of_plot:
        if (i < j):
            i += 1
        else:
            j += 1
    return i, j


def get_dicts_encounters_name_type(encounter_list, skip_number=False) -> Tuple[
    Dict[str, str], Dict[str, str], Dict[str, str]]:
    """

    :param encounterList: the list of wild pokemon encounters
    :param skipNumber: Skip the starting map number
    :return:
    """
    mapNames: List[str] = []
    d_name: Dict[str, str] = dict()
    d_type: Dict[str, str] = dict()
    for e in encounter_list:
        if (skip_number):
            map_name = e.mapIdNumber[6:]
        else:
            map_name = e.mapIdNumber

        if (map_name not in d_name):
            d_name[map_name], d_type[map_name] = [], []
            mapNames.append(map_name)
        if (e.pokemonSpecies.name not in d_name[map_name]):
            d_type[map_name].append(e.pokemonSpecies.type1)
            if (e.pokemonSpecies.type2 != ""):
                d_type[map_name].append(e.pokemonSpecies.type2)
            d_name[map_name].append(e.pokemonSpecies.name)

    return d_name, d_type, mapNames
