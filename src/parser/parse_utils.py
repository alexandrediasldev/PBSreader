import re


# [first,second] ->
def parse_equal_name_value(first, second, object_class):
    attr_pbs_string, attr_pbs_list, attr_pbs_basedata = object_class.get_attr_pbs_by_types()
    if first in attr_pbs_string:
        return second
    elif first in attr_pbs_list:
        return second.split(",")
    # elif first in attr_pbs_basedata:
    #    sub_class = object_class.get_attr_class(argument_translator[first])
    # return sub_class(
    #    **parse_one_line_coma(sub_class.get_attr_names(), parse_coma_equal_field(second))
    # )


def parse_bracket_header(line):
    result = re.search("\\[(.*)\\]", line)
    if result:
        return result.group(1)
    return None


def parse_one_line_coma(attr_names, line):
    kwargs = dict()
    for name, value in zip(attr_names, line):
        kwargs[name] = value
    return kwargs


def append_value_kwargs(kwargs, first, value, attr_name, argument_translator):
    if first.startswith(attr_name):
        first = attr_name
        if argument_translator[first] not in kwargs:
            kwargs[argument_translator[first]] = []
        kwargs[argument_translator[first]].append(value)
    else:
        kwargs[argument_translator[first]] = value
