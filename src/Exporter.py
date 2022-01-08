from typing import List

from PBSclasses import TrainerTypes
from PBSclasses.Ability import Ability
from PBSclasses.BaseData import BaseData
from PBSclasses.BerryPlant import BerryPlant
from PBSclasses.Connection import Connection
from PBSclasses.Encounter import Encounter, MapEncounter
from PBSclasses.Item import Item
from PBSclasses.Move import Move
from PBSclasses.Phone import Phone
from PBSclasses.ShadowPokemon import ShadowPokemon
from PBSclasses.Species import Species
from PBSclasses.Trainers import Trainer
from PBSclasses.Type import Type


def deserialize_list_string(value):
    return ",".join(value)


def deserialize_list_basedata(value):
    tmp_val = []
    for v in value:
        tmp_val.append(deserialize_basedata(v))
    return ",".join(tmp_val)


def deserialize_basedata(value):
    return deserialize_simple_csv(value)


class TypeDeserializer:
    deserialize_basedata_method = None
    deserialize_list_string_method = None
    deserialize_list_basedata_method = None

    def __init__(
        self,
        deserialize_basedata_method=deserialize_basedata,
        deserialize_list_string_method=deserialize_list_string,
        deserialize_list_basedata_method=deserialize_list_basedata,
    ):
        self.deserialize_basedata_method = deserialize_basedata_method
        self.deserialize_list_basedata_method = deserialize_list_basedata_method
        self.deserialize_list_string_method = deserialize_list_string_method

    def deserialize_value(self, value):
        if not isinstance(value, str):
            if isinstance(value, list):
                if not isinstance(value[0], str):
                    value = self.deserialize_list_basedata_method(value)
                else:
                    value = self.deserialize_list_string_method(value)
            else:
                value = self.deserialize_basedata_method(value)

        return value


def deserialize_simple_csv(obj: BaseData, attr_dict=None, type_deserializer=TypeDeserializer()):
    csv = ""
    if not attr_dict:
        attr_dict = obj.get_attr_dict()
    for data in attr_dict:
        value = obj.__dict__[attr_dict[data]]
        value = type_deserializer.deserialize_value(value)
        csv += value + ","
    return csv[:-1]


def deserialize_ability(ability: Ability):
    return deserialize_simple_csv(ability)


def deserialize_item(item: Item, version):
    attr_dict = item.get_attr_dict()
    if version < 16:
        attr_dict.pop("NamePlural")
    return deserialize_simple_csv(item, attr_dict)


def deserialize_move(move: Move):
    return deserialize_simple_csv(move)


def deserialize_trainer_types(trainer_types: TrainerTypes):
    return deserialize_simple_csv(trainer_types)


def deserialize_connection(connection: Connection):
    return deserialize_simple_csv(connection)


def deserialize_shadow(shadow_pokemon: ShadowPokemon):
    csv = shadow_pokemon.species + "=" + ",".join(shadow_pokemon.move_list)
    return csv


def deserialize_berry_plant(berry_plant: BerryPlant):
    attr_dict = berry_plant.get_attr_dict()
    attr_dict.pop("Name")
    csv = berry_plant.name + "=" + deserialize_simple_csv(berry_plant, attr_dict)
    return csv


def deserialize_phone(phone: Phone):
    lines = []
    attr_dict = phone.get_attr_dict()
    for data in attr_dict:
        value = phone.__dict__[attr_dict[data]]
        lines.append("[<" + data + ">]")
        lines.append(value)
    return lines


def deserialize_equal_data(obj: BaseData, attr_dict=None):
    lines = []
    if not attr_dict:
        attr_dict = obj.get_attr_dict()
    for data in attr_dict:
        value = obj.__dict__[attr_dict[data]]
        if value:
            if attr_dict[data] == "id":
                value = "[" + value + "]"
            else:
                if not isinstance(value, str):
                    if isinstance(value, list):
                        if isinstance(value[0], tuple):
                            tuple_fusion = ""
                            for a, b in value:
                                tuple_fusion += a + "," + b + ","
                            value = tuple_fusion[:-1]
                        else:
                            value = ",".join(value)
                    else:
                        value = deserialize_simple_csv(value)
                value = data + "=" + value
            lines.append(value)
    return lines


def deserialize_species(spe: Species):
    return deserialize_equal_data(spe)


def deserialize_metadata(metadata):
    attr_dict = metadata.get_attr_dict()
    attr_dict.pop("Player")
    meta_data_lines = deserialize_equal_data(metadata, attr_dict)
    if metadata.player:
        lines = []
        letter = "A"
        for player in metadata.player:
            lines.append("Player" + letter + "=" + deserialize_simple_csv(player))
            letter = str(chr((ord(letter) + 1)))
        meta_data_lines = meta_data_lines[:1] + lines + meta_data_lines[1:]

    return meta_data_lines


def deserialize_townmap(townmap):
    attr_dict = townmap.get_attr_dict()
    attr_dict.pop("Point")
    point_lines = deserialize_equal_data(townmap, attr_dict)
    if townmap.point:
        lines = []
        for point in townmap.point:
            lines.append("Point=" + deserialize_simple_csv(point))
        point_lines = point_lines + lines

    return point_lines


def deserialize_type(type: Type):
    return deserialize_equal_data(type)


def deserialize_encounters(encounters: List[Encounter]):
    last_method_name = ""
    last_map_id_number = ""
    lines = []
    for encounter in encounters:
        if encounter.map_id_number != last_map_id_number:
            lines.append(encounter.map_id_number)
            lines.append(",".join(encounter.encounter_densities))
            last_map_id_number = encounter.map_id_number
        if encounter.encounter_method.method_name != last_method_name:
            lines.append(encounter.encounter_method.method_name)
            last_method_name = encounter.encounter_method.method_name
        lines.append(deserialize_encounter(encounter))
    return lines


def deserialize_encounter(encounter: MapEncounter):
    line = []
    line.append(encounter.map_id_number)
    line.append(",".join(encounter.encounter_densities))
    last_method_name = ""
    for encou in encounter.encounters:
        if encou.encounter_method != last_method_name:
            line.append(encou.encounter_method)
        if encou.level_high:
            line.append(encou.pokemon_species + "," + encou.level_low + "," + encou.level_high)
        else:
            line.append(encou.pokemon_species + "," + encou.level_low)
        last_method_name = encou.encounter_method

    return line


def deserialize_trainer(trainer: Trainer):
    def deserialize_basedata_id(value):
        return value.id

    def deserialize_list_basedata_id(value):
        tmp_val = []
        for v in value:
            tmp_val.append(v.id)
        return ",".join(tmp_val)

    lines = []
    lines.append(trainer.type)
    second_line = trainer.name
    if trainer.version_number:
        second_line += "," + trainer.version_number
    lines.append(second_line)

    third_line = trainer.nb_pokemon
    if trainer.item_list:
        third_line += "," + deserialize_list_string(trainer.item_list)

    lines.append(third_line)
    type_deserializer = TypeDeserializer(
        deserialize_basedata_method=deserialize_basedata_id,
        deserialize_list_basedata_method=deserialize_list_basedata_id,
    )

    for pk in trainer.pokemon_list:

        pk_line = deserialize_simple_csv(pk, type_deserializer=type_deserializer)
        lines.append(pk_line)
    return lines
