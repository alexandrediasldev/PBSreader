import PBSclasses.Trainers as tr
import PBSclasses.Pokemon as pk
import PBSclasses.TrainerTypes as tp
import PBSclasses.Species as sp
import PBSclasses.Move as mv
import PBSclasses.Item as it
import PBSclasses.Encounter as en
import PBSclasses.EncounterMethod as enm
import PBSclasses.Ability as ab
from Finder import *
import PBSclasses.Environment as env
from PBSclasses.SpeciesEvolution import SpeciesEvolution
from PBSclasses.SpeciesStats import SpeciesStats


def parse_ability(csv_output) -> list[ab.Ability]:
    ability_list = []
    for line in csv_output:
        ability = ab.Ability(line[0], line[1], line[2], line[3])
        ability_list.append(ability)
    return ability_list


def parse_item(csv_output, has_plural_name=False) -> list[it.Item]:
    item_list = []
    for line in csv_output:
        move_name = ""
        line.append("")
        if (has_plural_name):
            item = it.Item(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8],
                           line[9], line[10])
        else:
            item = it.Item(line[0], line[1], line[2], "", line[3], line[4], line[5], line[6], line[7], line[8],
                           line[9])
        item_list.append(item)

    return item_list


def parse_encounter(csv_output, encounter_methods: list[enm.EncounterMethod], environment) -> list[en.Encounter]:
    encounter_list = []
    l = len(csv_output)
    i = 0
    while i < l:
        line = csv_output[i]
        if (len(line) == 1):
            is_map_name = True
            method_tmp = get_encounter_method_from_name(line[0], encounter_methods)
            if (method_tmp != ""):
                method = method_tmp
                is_map_name = False

            if (is_map_name):
                map_name = line[0]
                i += 1
                if (i < l):
                    line = csv_output[i]
                    if (len(line) == 1):
                        encounter_density = ['25', '10', '10']
                    else:
                        encounter_density = line

        elif (len(line) == 2):
            species = get_species_from_name(line[0], environment.species_list)
            level_low = line[1]
            level_high = ""
            encounter_list.append(en.Encounter(map_name, encounter_density, method, species, level_low, level_high))
        else:
            species = get_species_from_name(line[0], environment.species_list)
            level_low = line[1]
            level_high = line[2]
            encounter_list.append(en.Encounter(map_name, encounter_density, method, species, level_low, level_high))
        i += 1

    return encounter_list


def parser_move(csv_output) -> list[mv.Move]:
    moves_list = []
    for line in csv_output:
        move = mv.Move(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8],
                       line[9], line[10], line[11], line[12], line[13])
        moves_list.append(move)

    return moves_list


def parse_trainer_types(csv_output) -> list[tr.TrainerType]:
    trainer_type_list = []
    for line in csv_output:
        id_number, id, name, base_money, battle_bgm, victory_me, intro_me, gender, skill_level = \
            line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8]

        type = tp.TrainerType(id_number, id, name, base_money, battle_bgm, victory_me, intro_me, gender, skill_level)
        trainer_type_list.append(type)
    return trainer_type_list


def parse_pokemon_move(moves):
    moves_and_level = moves.split(',')
    level_moves = []
    for i in range(0, len(moves_and_level), 2):
        level = moves_and_level[i]
        if (i + 1 < len(moves_and_level)):
            move = moves_and_level[i + 1]
            level_moves.append((level, move))
    return level_moves


def parse_pokemon_base_stats(base_stats) -> SpeciesStats:
    stats = base_stats.split(',')
    if (len(stats) < 5):
        return SpeciesStats(1, 1, 1, 1, 1, 1)

    return SpeciesStats(stats[0], stats[1], stats[2], stats[3], stats[4], stats[5])


def parse_pokemon_evolution(evolution) -> SpeciesEvolution:
    evo = evolution.split(',')
    name = method = parameter = ""
    if (len(evo) >= 1):
        name = evo[0]
    if (len(evo) >= 2):
        method = evo[1]
    if (len(evo) >= 3):
        parameter = evo[2]

    return SpeciesEvolution(name, method, parameter)


def parse_pokemon(equal_output) -> list[Species]:
    id = -1
    species_list = []
    for line in equal_output:
        if (line[0].startswith('\ufeff')):
            line[0] = line[0][1:]
        first = line[0]
        if (len(line) > 1):
            second = line[1]
        if (first.startswith('[') and first.endswith(']')):
            if (id != -1):
                species = sp.Species(id, name, internal_name, type1, type2, base_stats, gender_rate, base_exp, moves,
                                     height, pokedex, evolutions)

                species_list.append(species)
                id = name = internal_name = type1 = type2 = base_stats = gender_rate \
                    = base_exp = moves = height = pokedex = evolutions = ""

            id = int(first[1:-1])

        elif (first == "Name"):
            name = second
        elif (first == "InternalName"):
            internal_name = second
        elif (first == "Type1"):
            type1 = second
        elif (first == "Type2"):
            type2 = second
        elif (first == "BaseStats"):
            base_stats = parse_pokemon_base_stats(second)
        elif (first == "GenderRate"):
            gender_rate = second
        elif (first == "BaseEXP"):
            base_exp = second
        elif (first == "Moves"):
            moves = parse_pokemon_move(second)
        elif (first == "Height"):
            height = second
        elif (first == "Pokedex"):
            pokedex = second
        elif (first == "Evolutions"):
            evolutions = parse_pokemon_evolution(second)

    species = sp.Species(id, name, internal_name, type1, type2, base_stats, gender_rate, base_exp, moves, height,
                         pokedex,
                         evolutions)
    species_list.append(species)
    return species_list


def parse_trainer_pokemon(pokemon_attributes, environment) -> pk.Pokemon:
    species = level = held_item = move_list = ability = \
        gender = form = shininess = nature = i_vs = hapiness = \
        nickname = shadow = ball_type = ""
    for i in range(len(pokemon_attributes)):
        attribute = pokemon_attributes[i]
        if (i == 0):
            species = get_species_from_name(attribute, environment.species_list)
        elif (i == 1):
            level = attribute
        elif (i == 2):
            held_item = get_item_from_name(attribute, environment.item_list)
        elif (i == 3):
            move_list = []
            for i in range(3, 7):
                if (i >= len(pokemon_attributes)):
                    break
                move_name = pokemon_attributes[i]
                if (move_name != ""):
                    move_list.append(get_move_from_name(move_name, environment.move_list))
        elif (i == 7):
            ability = attribute
        elif (i == 8):
            gender = attribute
        elif (i == 9):
            form = attribute
        elif (i == 10):
            shininess = attribute
        elif (i == 11):
            nature = attribute
        elif (i == 12):
            i_vs = attribute
        elif (i == 13):
            hapiness = attribute
        elif (i == 14):
            nickname = attribute
        elif (i == 15):
            shadow = attribute
        elif (i == 16):
            ball_type = attribute
    return pk.Pokemon(species, level, held_item, move_list, ability, form, gender,
                      shininess, nature, i_vs, hapiness, nickname, shadow, ball_type)


def parse_trainer_list(csv_output, environment) -> list[tr.Trainer]:
    line_num = 0
    pokemon_list = []
    trainer_list = []
    for line in csv_output:
        if (line_num == 0):
            type = line[0]
        elif (line_num == 1):
            name = line[0]
        elif (line_num == 2):
            nb_pokemon = int(line[0])
        else:
            if (nb_pokemon + 2 == line_num):
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
