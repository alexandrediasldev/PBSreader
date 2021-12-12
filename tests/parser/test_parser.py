from typing import List

from PBSclasses.Ability import Ability
from PBSclasses.BaseData import BaseData
from PBSclasses.SpeciesStats import SpeciesStats
from PBSclasses.TrainerTypes import TrainerType
from PBSclasses.Item import Item
from PBSclasses.Move import Move
from Parser import (
    parse_ability,
    parse_item,
    parser_move,
    parse_trainer_types,
    parse_pokemon_move,
    parse_pokemon_base_stats,
)
from hypothesis import given, strategies as st


def parse_item_func(list_item, item_obj, list_dict, version):
    item = list_item[0]
    for d, it in zip(list_dict, item_obj):
        ite = item.__dict__[d]
        if not isinstance(ite, BaseData) and not isinstance(ite, List) and ite is not None:
            assert ite == it


def csv_parse_helper(input, obj_class):
    return [input], obj_class.get_attr_names()


@given(st.lists(st.text(), min_size=10))
def test_parse_item16(input):
    csv_output, attr_names = csv_parse_helper(input, Item)
    version = 16
    list_obj = parse_item(csv_output, version)
    parse_item_func(list_obj, input, attr_names, version)


@given(st.lists(st.text(), min_size=10))
def test_parse_item15(input):
    csv_output, attr_names = csv_parse_helper(input, Item)
    version = 15
    attr_names.remove("name_plural")
    list_obj = parse_item(csv_output, version)
    parse_item_func(list_obj, input, attr_names, version)


@given(st.lists(st.text(), min_size=14))
def test_parse_move(input):
    csv_output, attr_names = csv_parse_helper(input, Move)
    version = 15
    list_obj = parser_move(csv_output)
    parse_item_func(list_obj, input, attr_names, version)


@given(st.lists(st.text(), min_size=9))
def test_parse_trainer_types(input):
    csv_output, attr_names = csv_parse_helper(input, TrainerType)
    version = 15
    list_obj = parse_trainer_types(csv_output)
    parse_item_func(list_obj, input, attr_names, version)


@given(st.lists(st.text(), min_size=9))
def test_parse_ability(input):
    csv_output, attr_names = csv_parse_helper(input, Ability)
    version = 15
    list_obj = parse_ability(csv_output)
    parse_item_func(list_obj, input, attr_names, version)


@given(
    st.lists(
        st.tuples(
            st.text(st.characters(blacklist_characters=",")),
            st.text(st.characters(blacklist_characters=",")),
        )
    )
)
def test_parse_pokemon_move(moves_input):
    csv_input = ""
    for level, mov in moves_input:
        csv_input += level + "," + mov + ","
    csv_input = csv_input[:-1]

    mv = parse_pokemon_move(csv_input)
    for t1, t2 in zip(mv, moves_input):
        assert t1 == t2


@given(st.lists(st.text(st.characters(blacklist_characters=",")), min_size=6))
def test_parse_pokemon_stats(stats_input):
    csv_input = ""
    for s in stats_input:
        csv_input += s + ","
    csv_input = csv_input[:-1]

    mv = parse_pokemon_base_stats(csv_input)

    move_list = [mv]
    list_dict = SpeciesStats.get_attr_names()
    parse_item_func(move_list, stats_input, list_dict, 0)


"""
@given(st.lists(st.text()))
def test_parse_pokemon(pokemon_obj):
    assume(pokemon_obj[0])
    equal_input = []
    equal_input.append("["+pokemon_obj[0]+"]")
    pbs_names = Species.get_attr_pbs_names()
    for name, value in zip(pbs_names, pokemon_obj[1:]):
        equal_input.append(name + "=" + value)
    equal_output = csv.reader(equal_input, delimiter="=")
    equal_output = [x for x in equal_output]

    print(equal_output)
    list_dict = Species.get_attr_names()
    #list_dict.remove("id")
    pokemon_obj[1:]
    version = 15
    pokemon_list = parse_pokemon(equal_output)
    print(pokemon_list)
    print(pokemon_obj)
    parse_item_func(pokemon_list, pokemon_obj, list_dict, version)
"""
