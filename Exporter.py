from PBSclasses.BaseData import BaseData
from PBSclasses.Phone import Phone
from PBSclasses.ShadowPokemon import ShadowPokemon


def deserialize_simple_csv(obj: BaseData, attr_dict=None):
    csv = ""
    if not attr_dict:
        attr_dict = obj.get_attr_dict()
    for data in attr_dict:
        value = obj.__dict__[attr_dict[data]]
        csv += value + ","
    return csv[:-1]


def deserialize_shadow(shadow_pokemon: ShadowPokemon):
    csv = shadow_pokemon.species.internal_name + "=" + ",".join(shadow_pokemon.move_list)
    return csv


def deserialize_phone(phone: Phone):
    lines = []
    attr_dict = phone.get_attr_dict()
    for data in attr_dict:
        value = phone.__dict__[attr_dict[data]]
        lines.append("[<" + data + ">]")
        lines.append(value)
    return lines


def deserialize_equal_data(obj: BaseData):
    lines = []
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
