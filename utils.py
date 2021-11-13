from typing import Dict, List, Tuple


def find_sizes_of_subplots(number_of_plot) -> Tuple[int, int]:
    i = 0
    j = 0
    while i * j < number_of_plot:
        if i < j:
            i += 1
        else:
            j += 1
    return i, j


def get_dicts_encounters_name_type(
    encounter_list, skip_number=False
) -> Tuple[Dict[str, List[str]], Dict[str, List[str]], List[str]]:
    """

    :param encounterList: the list of wild pokemon encounters
    :param skipNumber: Skip the starting map number
    :return:
    """
    mapNames: List[str] = []
    d_name: Dict[str, List[str]] = dict()
    d_type: Dict[str, List[str]] = dict()
    for e in encounter_list:
        if skip_number:
            map_name = e.map_id_number[6:]
        else:
            map_name = e.map_id_number

        if map_name not in d_name:
            d_name[map_name], d_type[map_name] = [], []
            mapNames.append(map_name)
        if e.pokemon_species.name not in d_name[map_name]:
            d_type[map_name].append(e.pokemon_species.type1)
            if e.pokemon_species.type2 != "":
                d_type[map_name].append(e.pokemon_species.type2)
            d_name[map_name].append(e.pokemon_species.name)

    return d_name, d_type, mapNames
