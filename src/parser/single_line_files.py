# ["attribute0","attribute1"] -> Object
def attr_list_to_object(line, object_class):
    return object_class(**get_kwargs_from_line_csv(object_class.get_attr_names(), line))


# ["attribute_name","attribute0,attribute1,attribute2"] -> Object
def attr_name_and_str_list_to_object(line, object_class):
    after_equal_expanded = line[1].split(",")
    line_fused = [line[0]] + [after_equal_expanded]
    return object_class(**get_kwargs_from_line_csv(object_class.get_attr_names(), line_fused))


def get_kwargs_from_line_csv(attr_names, lines):
    kwargs = dict()
    for name, value in zip(attr_names, lines):
        kwargs[name] = value
    return kwargs


def parse_csv(lines, object_class):
    list_obj = []
    for line in lines:
        list_obj.append(attr_list_to_object(line, object_class))
    return list_obj


def parse_csv_after_equal(lines, object_class):
    list_obj = []
    for line in lines:
        list_obj.append(attr_name_and_str_list_to_object(line, object_class))
    return list_obj
