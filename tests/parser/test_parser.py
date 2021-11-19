from PBSclasses.TrainerTypes import TrainerType
from PBSclasses.Item import Item
from PBSclasses.Move import Move
from Parser import parse_ability, parse_item, parser_move, parse_trainer_types
from hypothesis import example, given, strategies as st


@given(st.text(), st.text(), st.text(), st.text())
@example("DESCRIPTION", "NAME", "ID", "IDNUMBER")
def test_parse_ability(DESCRIPTION, NAME, ID, IDNUMBER):
    csv_output = [[IDNUMBER, ID, NAME, DESCRIPTION]]
    list_ability = parse_ability(csv_output)
    ability = list_ability[0]
    assert ability.description == DESCRIPTION
    assert ability.name == NAME
    assert ability.id == ID
    assert ability.id_number == IDNUMBER


def parse_item_func(list_item, item_obj, list_dict, version):
    item = list_item[0]
    for d, it in zip(list_dict, item_obj):
        assert item.__dict__[d] == it


@given(st.lists(st.text(), min_size=10))
def test_parse_item16(item_obj):
    csv_output = [item_obj]
    list_dict = Item.get_attr_names()
    version = 16
    list_item = parse_item(csv_output, version)
    parse_item_func(list_item, item_obj, list_dict, version)


@given(st.lists(st.text(), min_size=10))
def test_parse_item15(item_obj):

    csv_output = [item_obj]
    list_dict = Item.get_attr_names()
    list_dict.remove("name_plural")
    version = 15
    list_item = parse_item(csv_output, version)
    parse_item_func(list_item, item_obj, list_dict, version)


@given(st.lists(st.text(), min_size=14))
def test_parse_move(move_obj):
    csv_output = [move_obj]
    list_dict = Move.get_attr_names()
    version = 15
    move_list = parser_move(csv_output)
    parse_item_func(move_list, move_obj, list_dict, version)


@given(st.lists(st.text(), min_size=9))
def test_parse_trainer_types(trainer_types):
    csv_output = [trainer_types]
    list_dict = TrainerType.get_attr_names()
    version = 15
    trainer_list = parse_trainer_types(csv_output)
    parse_item_func(trainer_list, trainer_types, list_dict, version)
