import PBSclasses.Trainers as tr
import PBSclasses.TrainerPokemon as pk
import PBSclasses.Move as mv
import PBSclasses.Item as it
import PBSclasses.Encounter as en
import PBSclasses.Ability as ab
from PBSclasses.Species import SpeciesV15, SpeciesV17, SpeciesV16, SpeciesV18, SpeciesV19
from PBSclasses.SpeciesEvolution import SpeciesEvolution
from PBSclasses.BerryPlant import BerryPlantV16
from PBSclasses.Connection import ConnectionV15
from PBSclasses.MetaData import MetaDataV15, PlayerMetaData, HomeMetaData, MetaDataV18
from PBSclasses.Phone import PhoneV15
from PBSclasses.ShadowPokemon import ShadowPokemonV15
from PBSclasses.SpeciesStats import SpeciesStats
from PBSclasses.Tm import TmV15

from PBSclasses.TownMap import TownMap, TownPoint
from PBSclasses.TrainerTypes import TrainerTypeV15, TrainerTypeV16
from PBSclasses.Type import TypeV15
from src.parser.parse_utils import parse_bracket_header, parse_one_line_coma, parse_coma_equal_field
from src.parser.schema import separate_equal, separate_trainers, separate_encounters


def get_kwargs_from_line_csv(attr_names, lines):
    kwargs = dict()
    for name, value in zip(attr_names, lines):
        kwargs[name] = value
    return kwargs


def parse_csv(lines, object_class):
    list_obj = []
    for line in lines:
        list_obj.append(
            object_class(**get_kwargs_from_line_csv(object_class.get_attr_names(), line))
        )
    return list_obj


def parse_csv_after_equal(lines, object_class):
    list_obj = []
    for line in lines:
        after_equal_expanded = parse_coma_equal_field(line[1])
        line_fused = [line[0]] + [after_equal_expanded]
        list_obj.append(
            object_class(**get_kwargs_from_line_csv(object_class.get_attr_names(), line_fused))
        )
    return list_obj


def parse_equal_name_value(first, second, object_class):
    attr_pbs_string, attr_pbs_list, attr_pbs_basedata = object_class.get_attr_pbs_by_types()
    if first in attr_pbs_string:
        return second
    elif first in attr_pbs_list:
        return parse_coma_equal_field(second)
    # elif first in attr_pbs_basedata:
    #    sub_class = object_class.get_attr_class(argument_translator[first])
    # return sub_class(
    #    **parse_one_line_coma(sub_class.get_attr_names(), parse_coma_equal_field(second))
    # )


def parse_equal_line(lines, object_class):
    argument_translator = object_class.get_attr_dict()
    kwargs = {}
    kwargs["id"] = parse_bracket_header(lines[0][0])
    for line in lines[1:]:
        value = parse_equal_name_value(line[0], line[1], object_class)
        kwargs[argument_translator[line[0]]] = value
    return object_class(**kwargs)


def parse_tm_line(lines, object_class):
    kwargs = {}
    kwargs["move_name"] = parse_bracket_header(lines[0][0])
    kwargs["pokemon_list"] = parse_coma_equal_field(lines[1][0])
    return object_class(**kwargs)


def parse_tm_full(lines, object_class):
    list_obj = []
    lines_separated = separate_equal(lines)
    for line in lines_separated:
        obj = parse_tm_line(line, object_class)
        list_obj.append(obj)
    return list_obj


def append_value_kwargs(kwargs, first, value, attr_name, argument_translator):
    if first.startswith(attr_name):
        first = attr_name
        if argument_translator[first] not in kwargs:
            kwargs[argument_translator[first]] = []
        kwargs[argument_translator[first]].append(value)
    else:
        kwargs[argument_translator[first]] = value


def parse_equal_line_metadata(lines, object_class):
    argument_translator = object_class.get_attr_dict()
    kwargs = {}
    kwargs["id"] = parse_bracket_header(lines[0][0])
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


def parse_equal_metadata(lines, object_class):
    list_obj = []
    lines_separated = separate_equal(lines)
    for line in lines_separated:
        obj = parse_equal_line_metadata(line, object_class)
        list_obj.append(obj)
    return list_obj


def parse_equal_line_pokemon(lines, object_class):
    argument_translator = object_class.get_attr_dict()
    kwargs = {}
    kwargs["id"] = parse_bracket_header(lines[0][0])
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


def parse_equal_pokemon(lines, object_class):
    list_obj = []
    lines_separated = separate_equal(lines)
    for line in lines_separated:
        obj = parse_equal_line_pokemon(line, object_class)
        list_obj.append(obj)
    return list_obj


def parse_equal_line_townmap(lines, object_class):
    argument_translator = object_class.get_attr_dict()
    kwargs = {}
    kwargs["id"] = parse_bracket_header(lines[0][0])
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


def parse_equal_townmap(lines, object_class):
    list_obj = []
    lines_separated = separate_equal(lines)
    for line in lines_separated:
        obj = parse_equal_line_townmap(line, object_class)
        list_obj.append(obj)
    return list_obj


def parse_equal(lines, object_class):
    list_obj = []
    lines_separated = separate_equal(lines)
    for line in lines_separated:
        obj = parse_equal_line(line, object_class)
        list_obj.append(obj)
    return list_obj


# ---- CSV
def parse_ability(csv_output) -> list[ab.AbilityV15]:
    type = ab.AbilityV15
    return parse_csv(csv_output, type)


def parse_move(csv_output) -> list[mv.MoveV15]:
    type = mv.MoveV15
    return parse_csv(csv_output, type)


def parse_berry_plant(csv_output) -> list[BerryPlantV16]:
    type = BerryPlantV16
    return parse_csv(csv_output, type)


def parse_connection(csv_output) -> list[ConnectionV15]:
    type = ConnectionV15
    return parse_csv(csv_output, type)


def parse_trainer_types(csv_output, version) -> list[TrainerTypeV15]:
    if version == 15:
        type = TrainerTypeV15
    else:
        type = TrainerTypeV16
    return parse_csv(csv_output, type)


def parse_item(csv_output, version) -> list[it.ItemV15]:
    if version == 15:
        itemType = it.ItemV15
    else:
        itemType = it.ItemV16
    return parse_csv(csv_output, itemType)


def parse_shadow_pokemon(csv_output) -> list[ShadowPokemonV15]:
    type = ShadowPokemonV15
    return parse_csv_after_equal(csv_output, type)


def parse_tm(csv_output, version):
    type = TmV15
    return parse_tm_full(csv_output, type)


# ------ Equal


def parse_type(equal_output):
    type = TypeV15
    return parse_equal(equal_output, type)


# ----- Phone
def parse_phone(csv_output):
    argument_translator = PhoneV15.get_attr_dict()
    kwargs = dict()
    lines_separated = separate_equal(csv_output)
    for line in lines_separated:
        section_name = parse_bracket_header(line[0][0])
        section_name = section_name.removesuffix(">")
        section_name = section_name.removeprefix("<")
        line_content = []
        for rest_of_the_line in line[1:]:
            line_content.append(rest_of_the_line[0])
        kwargs[argument_translator[section_name]] = line_content
    phone = PhoneV15(**kwargs)
    return phone


def parse_townmap(equal_output):
    type = TownMap
    return parse_equal_townmap(equal_output, type)


def parse_metadata(equal_output, version):
    if version <= 17:
        type = MetaDataV15
    else:
        type = MetaDataV18
    return parse_equal_metadata(equal_output, type)


def parse_pokemon(equal_output, version):
    if version == 15:
        type = SpeciesV15
    elif version == 16:
        type = SpeciesV16
    elif version == 17:
        type = SpeciesV17
    elif version == 18:
        type = SpeciesV18
    else:
        type = SpeciesV19
    return parse_equal_pokemon(equal_output, type)


def parse_trainer_list(csv_output, version) -> list[tr.TrainerV15]:
    def _parse_trainer_pokemon(pokemon_attributes) -> pk.TrainerPokemonV15:
        attr_names = pk.TrainerPokemonV15.get_attr_names()
        moves = pokemon_attributes[3:7]
        pokemon_attributes = pokemon_attributes[:3] + pokemon_attributes[7:]
        attr_names.remove("move_list")
        kwargs = parse_one_line_coma(attr_names, pokemon_attributes)
        kwargs["move_list"] = moves

        return pk.TrainerPokemonV15(**kwargs)

    def parse_one_trainer(lines):
        coma_line = []
        coma_line.append(lines[0][0])
        coma_line.append(lines[1][0])
        coma_line.append(lines[1][1] if len(lines[1]) > 1 else "")
        coma_line.append(lines[2][1:])
        coma_line.append(lines[2][0])
        coma_line.append([_parse_trainer_pokemon(line) for line in lines[3:]])

        kwargs = parse_one_line_coma(tr.TrainerV15.get_attr_names(), coma_line)

        return kwargs

    lines = separate_trainers(csv_output)
    obj_list = []
    for line in lines:
        obj_list.append(tr.TrainerV15(**parse_one_trainer(line)))
    return obj_list


def parse_encounter(csv_output, version: int) -> list[en.EncounterV15]:
    def parse_one_encounter(encounter_by_map_lines):
        coma_line = []
        coma_line.append(encounter_by_map_lines[0][0][0])
        coma_line.append(encounter_by_map_lines[0][1])
        encounter_method_list = []
        for encounter_by_method_lines in encounter_by_map_lines[1:]:
            encounter_method_name = encounter_by_method_lines[0][0]
            pokemon_list = []
            for encounter_pokemon_lines in encounter_by_method_lines[1:]:
                pokemon_list.append(
                    en.EncounterPokemon(
                        **parse_one_line_coma(
                            en.EncounterPokemon.get_attr_names(), encounter_pokemon_lines
                        )
                    )
                )
            encounter_method_list.append(en.EncounterByMethod(encounter_method_name, pokemon_list))
        coma_line.append(encounter_method_list)

        return en.EncounterV15(**parse_one_line_coma(en.EncounterV15.get_attr_names(), coma_line))

    separated_encounter_lines = separate_encounters(csv_output)
    encounter_list = []
    for encounter in separated_encounter_lines:
        encounter_list.append(parse_one_encounter(encounter))

    return encounter_list
