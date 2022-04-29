import PBSclasses.Trainers as tr
import PBSclasses.Pokemon as pk
import PBSclasses.Move as mv
import PBSclasses.Item as it
import PBSclasses.Encounter as en
import PBSclasses.EncounterMethod as enm
import PBSclasses.Ability as ab
from PBSclasses.BerryPlant import BerryPlant
from PBSclasses.Connection import Connection
from PBSclasses.MetaData import MetaData
from PBSclasses.Phone import Phone
from PBSclasses.ShadowPokemon import ShadowPokemon

from PBSclasses.TownMap import TownMap
from PBSclasses.TrainerTypes import TrainerTypeV15, TrainerTypeV16
from PBSclasses.Type import Type
from src.parser.parse_utils import parse_bracket_header, parse_one_line_coma, parse_coma_equal_field
from src.parser.schema import (
    ParsingSchemaPhone,
    ParsingSchemaCsv,
    ParsingSchemaEncounter,
    ParsingSchemaTrainer,
    ParsingSchemaEqual,
    ParsingSchemaTownmap,
    ParsingSchemaPokemon,
    ParsingSchemaMetadata,
    FileSpliter,
    separate_equal,
)


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


def parse_equal(lines, object_class):
    list_obj = []
    lines_separated = separate_equal(lines)
    for line in lines_separated:
        obj = parse_equal_line(line, object_class)
        list_obj.append(obj)
    return list_obj


def parse_schema(
    lines, object_class, schema_class, obj_definition, attr_names=None, environement=None, **kwargs
):
    if not attr_names:
        attr_names = object_class.get_attr_names()

    f = FileSpliter(lines, obj_definition)
    obj = f.parse_object()
    sc = schema_class(object_class, attr_names)
    obj_list = []
    for o in obj:
        obj_list.append(sc.apply_function_one_object(o))

    return obj_list


# ---- CSV
def parse_ability(csv_output) -> list[ab.Ability]:
    type = ab.Ability
    return parse_csv(csv_output, type)


def parser_move(csv_output) -> list[mv.Move]:
    type = mv.Move
    return parse_csv(csv_output, type)


def parse_berry_plant(csv_output) -> list[BerryPlant]:
    type = BerryPlant
    return parse_csv(csv_output, type)


def parse_connection(csv_output) -> list[Connection]:
    type = Connection
    return parse_csv(csv_output, type)


def parse_trainer_types(csv_output, version) -> list[tr.TrainerType]:
    if version == 15:
        type = TrainerTypeV15
    else:
        type = TrainerTypeV16
    return parse_csv(csv_output, type)


def parse_item(csv_output, version) -> list[it.Item]:
    if version == 15:
        itemType = it.ItemV15
    else:
        itemType = it.ItemV16
    return parse_csv(csv_output, itemType)


# ------ Equal


def parse_type(equal_output):
    type = Type
    return parse_equal(equal_output, type)


# -----


def parse_shadow_pokemon(csv_output) -> list[ShadowPokemon]:
    type = ShadowPokemon
    return parse_csv_after_equal(csv_output, type)


def parse_phone(csv_output):
    sc = ParsingSchemaPhone(Phone, Phone.get_attr_names())
    f = FileSpliter(csv_output, ["[]"])
    obj = f.parse_object()
    phone = sc.apply_function_one_object(obj)

    return phone


def parse_townmap(equal_output):
    return parse_schema(equal_output, TownMap, ParsingSchemaTownmap, ["[]"])


def parse_metadata(equal_output):
    return parse_schema(equal_output, MetaData, ParsingSchemaMetadata, ["[]"])


def parse_pokemon(equal_output) -> list[pk.Species]:
    return parse_schema(equal_output, pk.Species, ParsingSchemaPokemon, ["[]"])


def parse_trainer_list(csv_output, version) -> list[tr.Trainer]:
    return parse_schema(csv_output, tr.Trainer, ParsingSchemaTrainer, ["\n", "\n", "val"])


def parse_encounter(
    csv_output, encounter_methods: list[enm.EncounterMethod], environment
) -> list[en.Encounter]:
    f = FileSpliter(csv_output, ["int"])
    obj = f.parse_object()
    object_class = en.MapEncounter
    attr_names = object_class.get_attr_names()
    sc = ParsingSchemaEncounter(object_class, attr_names, encounter_methods=encounter_methods)
    obj_list = []
    for o in obj:
        obj_list.append(sc.apply_function_one_object(o))

    return obj_list
