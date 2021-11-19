import PBSclasses.Trainers as tr
import PBSclasses.Pokemon as pk
import PBSclasses.TrainerTypes as tp
import PBSclasses.Species as sp
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

from PBSclasses.SpeciesEvolution import SpeciesEvolution
from PBSclasses.SpeciesStats import SpeciesStats


def parse_ability(csv_output) -> list[ab.Ability]:
    ability_list = []
    for line in csv_output:
        ability = ab.Ability(line[0], line[1], line[2], line[3])

        ability_list.append(ability)
    return ability_list


def parse_item(csv_output, version) -> list[it.Item]:
    item_list = []
    for line in csv_output:
        line.append("")
        if version >= 16:
            item = it.Item(
                line[0],
                line[1],
                line[2],
                line[3],
                line[4],
                line[5],
                line[6],
                line[7],
                line[8],
                line[9],
                line[10],
            )
        else:
            item = it.Item(
                line[0],
                line[1],
                line[2],
                "",
                line[3],
                line[4],
                line[5],
                line[6],
                line[7],
                line[8],
                line[9],
            )
        item_list.append(item)

    return item_list


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


def parser_move(csv_output) -> list[mv.Move]:
    moves_list = []
    for line in csv_output:
        move = mv.Move(
            line[0],
            line[1],
            line[2],
            line[3],
            line[4],
            line[5],
            line[6],
            line[7],
            line[8],
            line[9],
            line[10],
            line[11],
            line[12],
            line[13],
        )
        moves_list.append(move)

    return moves_list


def parse_trainer_types(csv_output) -> list[tr.TrainerType]:
    trainer_type_list = []
    for line in csv_output:
        id_number, id, name, base_money, battle_bgm, victory_me, intro_me, gender, skill_level = (
            line[0],
            line[1],
            line[2],
            line[3],
            line[4],
            line[5],
            line[6],
            line[7],
            line[8],
        )

        type = tp.TrainerType(
            id_number, id, name, base_money, battle_bgm, victory_me, intro_me, gender, skill_level
        )
        trainer_type_list.append(type)
    return trainer_type_list


def parse_pokemon_move(moves):
    moves_and_level = moves.split(",")
    level_moves = []
    for i in range(0, len(moves_and_level), 2):
        level = moves_and_level[i]
        if i + 1 < len(moves_and_level):
            move = moves_and_level[i + 1]
            level_moves.append((level, move))
    return level_moves


def parse_pokemon_base_stats(base_stats) -> SpeciesStats:
    stats = base_stats.split(",")
    if len(stats) < 5:
        return SpeciesStats(1, 1, 1, 1, 1, 1)

    return SpeciesStats(stats[0], stats[1], stats[2], stats[3], stats[4], stats[5])


def parse_pokemon_evolution(evolution) -> SpeciesEvolution:
    evo = evolution.split(",")
    name = method = parameter = ""
    if len(evo) >= 1:
        name = evo[0]
    if len(evo) >= 2:
        method = evo[1]
    if len(evo) >= 3:
        parameter = evo[2]

    return SpeciesEvolution(name, method, parameter)


def parse_pokemon(equal_output) -> list[Species]:
    kwargs = dict()
    id = -1
    species_list = []
    argument_translator = {
        "Name": "name",
        "InternalName": "internal_name",
        "Type1": "type1",
        "Type2": "type2",
        "GenderRate": "gender_rate",
        "BaseEXP": "base_Exp",
        "Height": "height",
        "Pokedex": "pokedex",
        "Incense": "incense",
        "Evolutions": "evolutions",
        "Moves": "moves",
        "BaseStats": "base_stats",
    }
    for line in equal_output:
        if line[0].startswith("\ufeff"):
            line[0] = line[0][1:]
        first = line[0]
        if len(line) > 1:
            second = line[1]
        if first.startswith("[") and first.endswith("]"):
            if id != -1:
                kwargs["id"] = id
                species = sp.Species(**kwargs)
                species_list.append(species)
                kwargs = dict()
            id = int(first[1:-1])
        elif first in [
            "Name",
            "InternalName",
            "Type1",
            "Type2",
            "GenderRate",
            "BaseEXP",
            "Height",
            "Pokedex",
            "Incense",
        ]:
            kwargs[argument_translator[first]] = second
        elif first == "BaseStats":
            kwargs[argument_translator[first]] = parse_pokemon_base_stats(second)
        elif first == "Moves":
            kwargs[argument_translator[first]] = parse_pokemon_move(second)
        elif first == "Evolutions":
            kwargs[argument_translator[first]] = parse_pokemon_evolution(second)
    kwargs["id"] = id
    species = sp.Species(**kwargs)
    species_list.append(species)
    return species_list


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
    for line in csv_output:
        if line_num == 0:
            type = line[0]
        elif line_num == 1:
            name = line[0]
        elif line_num == 2:
            nb_pokemon = int(line[0])
        else:
            if nb_pokemon + 2 == line_num:
                pkm = parse_trainer_pokemon(line, environment)
                pokemon_list.append(pkm)

                trainer_type = get_trainer_type_from_name(type, environment.trainer_type_list)
                train = tr.Trainer(trainer_type, name, nb_pokemon, pokemon_list)
                trainer_list.append(train)

                pokemon_list = []
                line_num = -1
            else:
                pkm = parse_trainer_pokemon(line, environment)
                pokemon_list.append(pkm)
        line_num += 1
    return trainer_list
