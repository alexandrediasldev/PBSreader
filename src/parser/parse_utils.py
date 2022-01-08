import re


def parse_coma_equal_field(field):
    coma_list = field.split(",")
    return coma_list


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
