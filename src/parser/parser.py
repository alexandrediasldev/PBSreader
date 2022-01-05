import PBSclasses.Trainers as tr
import PBSclasses.Pokemon as pk
import PBSclasses.Move as mv
import PBSclasses.Item as it
import PBSclasses.Encounter as en
import PBSclasses.EncounterMethod as enm
import PBSclasses.Ability as ab
from PBSclasses.Connection import Connection
from PBSclasses.MetaData import MetaData
from PBSclasses.Phone import Phone
from PBSclasses.ShadowPokemon import ShadowPokemon

from PBSclasses.TownMap import TownMap
from PBSclasses.Type import Type
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
)


def parse_schema(lines, object_class, schema_class, attr_names=None, environement=None, **kwargs):
    if not attr_names:
        attr_names = object_class.get_attr_names()
    schema = schema_class(lines, object_class, attr_names, environement, **kwargs)
    return schema.parse_object()


def parse_ability(csv_output) -> list[ab.Ability]:
    return parse_schema(csv_output, ab.Ability, ParsingSchemaCsv)


def parser_move(csv_output) -> list[mv.Move]:
    return parse_schema(csv_output, mv.Move, ParsingSchemaCsv)


def parse_trainer_types(csv_output) -> list[tr.TrainerType]:
    return parse_schema(csv_output, tr.TrainerType, ParsingSchemaCsv)


def parse_connection(csv_output) -> list[Connection]:
    return parse_schema(csv_output, Connection, ParsingSchemaCsv)


def parse_item(csv_output, version) -> list[it.Item]:
    attr_names = it.Item.get_attr_names()
    if version < 16:
        attr_names.remove("name_plural")
    return parse_schema(csv_output, it.Item, ParsingSchemaCsv, attr_names)


def parse_shadow_pokemon(csv_output, environment) -> list[ShadowPokemon]:
    return parse_schema(csv_output, ShadowPokemon, ParsingSchemaShadow, environement=environment)


def parse_phone(csv_output):
    return parse_schema(csv_output, Phone, ParsingSchemaPhone)


def parse_type(equal_output):
    return parse_schema(equal_output, Type, ParsingSchemaEqual)


def parse_townmap(equal_output):
    return parse_schema(equal_output, TownMap, ParsingSchemaTownmap)


def parse_metadata(equal_output):
    return parse_schema(equal_output, MetaData, ParsingSchemaMetadata)


def parse_pokemon(equal_output) -> list[pk.Species]:
    return parse_schema(equal_output, pk.Species, ParsingSchemaPokemon)


def parse_trainer_list(csv_output, environment) -> list[tr.Trainer]:
    return parse_schema(csv_output, tr.Trainer, ParsingSchemaTrainer, environement=environment)


def parse_encounter(
    csv_output, encounter_methods: list[enm.EncounterMethod], environment
) -> list[en.Encounter]:

    object_class = en.MapEncounter
    attr_names = object_class.get_attr_names()
    schema = ParsingSchemaEncounter(
        csv_output, object_class, attr_names, encounter_methods=encounter_methods
    )
    return schema.parse_object()
