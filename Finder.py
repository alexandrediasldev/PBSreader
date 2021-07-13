import Exception as ex


def get_species_from_name(name, species_list):
    if (name == ""):
        return ""
    for s in species_list:
        if (name == s.internalName):
            return s
    # in case of # after name
    for s in species_list:
        if (name.startswith(s.id)):
            return s

    raise ex.UnknownPBSName(name + " not found in species list")


def get_item_from_name(name, item_list):
    if (name == ""):
        return ""
    for item in item_list:
        if (item.id == name):
            return item
    # in case of # after name
    for item in item_list:
        if (name.startswith(item.id)):
            return item
    raise ex.UnknownPBSName(name + " not found in item list")


def get_move_from_name(name, move_list):
    if (name == ""):
        return ""
    for m in move_list:
        if (m.id == name):
            return m
    # in case of # after name
    for m in move_list:
        if (name.startswith(m.id)):
            return m

    raise ex.UnknownPBSName(name + " not found in move list")


def get_encounter_method_from_name(name, encounter_method_list):
    if (name == ""):
        return ""
    for m in encounter_method_list:
        if (m.methodName == name):
            return m
    return ""


def get_trainer_type_from_name(name, trainer_type_list):
    if (name == ""):
        return ""
    for t in trainer_type_list:
        if (t.id == name or name.startswith(t.id)):
            return t
    # in case of # after name
    for t in trainer_type_list:
        if (name.startswith(t.id)):
            return t

    raise ex.UnknownPBSName(name + " not found in trainer type list")
