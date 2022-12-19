from PBSclasses.Ability import AbilityV15, AbilityV20
from src import FileLoader
from src.Exporter import deserialize_ability


def generate_object(obj_class):
    for name in obj_class.__dict__:
        if isinstance(obj_class.__dict__[name], list):  # List
            for i in range(0, 3):
                obj_class.__dict__[name].append(name + str(i))

            # if isinstance(obj_class.__dict__[name][0], str):  # List[str]
            # for i in range(len(obj_class.__dict__[name])):
            #    assert name + str(i) == obj_class.__dict__[name][i]
            #    assert "TODO" == 0
            # elif isinstance(obj_class.__dict__[name][0], tuple):  # List[tuple]
            # for i in range(len(obj_class.__dict__[name])):
            #    assert name + str(i) + "left" == obj_class.__dict__[name][i][0]
            #    assert name + str(i) + "right" == obj_class.__dict__[name][i][1]
            #    assert "TODO" == 0
            # else:  # List[Object]
            # for i in range(len(obj_class.__dict__[name])):
            #    check_attributes(obj_class.__dict__[name][i])
            #    assert "TODO" == 0
        elif isinstance(obj_class.__dict__[name], str):  # str
            obj_class.__dict__[name] = name
            # if name != "nb_pokemon" and name != "map_id_number":
            #   assert name == obj_class.__dict__[name]
        else:  # Object
            # check_attributes(obj_class.__dict__[name])
            assert "TODO" == 0
    return obj_class


def check_file(generated_file, file):
    for line in generated_file:
        if not (line in file):
            assert file == generated_file


def compare_export_to_csv_file(filename, obj_class, export_function, version):
    file = FileLoader.read_full_file("../PBS/" + filename)
    obj = generate_object(obj_class())
    file_exported = export_function(obj, version)
    check_file(file, file_exported)


class TestAbility:
    def test_abilityv15(self):
        # for version in [15, 16, 17, 18, 19]:
        #    csv_check("abilities.txt", parse_ability, version=version)
        # equal_check("abilitiesv20.txt", parse_ability, version=20)
        compare_export_to_csv_file("abilities.txt", AbilityV15, deserialize_ability, 15)

    def test_abilityv20(self):
        # equal_check("abilitiesv20.txt", parse_ability, version=20)
        compare_export_to_csv_file("abilitiesv20.txt", AbilityV20, deserialize_ability, 20)
