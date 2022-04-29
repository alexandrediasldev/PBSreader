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
from src.parser.parse_utils import parse_bracket_header, parse_one_line_coma
from src.parser.schema import (
    ParsingSchemaPhone,
    ParsingSchemaCsv,
    ParsingSchemaEncounter,
    ParsingSchemaTrainer,
    ParsingSchemaShadow,
    ParsingSchemaEqual,
    ParsingSchemaTownmap,
    ParsingSchemaPokemon,
    ParsingSchemaMetadata,
    FileSpliter,
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


# ------


def parse_shadow_pokemon(csv_output) -> list[ShadowPokemon]:
    return parse_schema(csv_output, ShadowPokemon, ParsingSchemaShadow, ["\n"])


def parse_phone(csv_output):
    sc = ParsingSchemaPhone(Phone, Phone.get_attr_names())
    f = FileSpliter(csv_output, ["[]"])
    obj = f.parse_object()
    phone = sc.apply_function_one_object(obj)

    return phone


def parse_type(equal_output):
    return parse_schema(equal_output, Type, ParsingSchemaEqual, ["[]"])


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
