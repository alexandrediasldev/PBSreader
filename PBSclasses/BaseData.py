from dataclasses import dataclass


@dataclass()
class BaseData:
    def string(self, line_ending="\n"):
        representation = ""
        for name in self.__dict__:
            value = self.__dict__[name]
            if value:

                if isinstance(value, BaseData):
                    child_value = value.string(line_ending=", ")
                    if child_value:
                        representation += _format_parent(name) + " <" + child_value + ">"
                else:
                    if isinstance(value, list) and isinstance(value[0], BaseData):
                        representation += _format_name(name) + ": "
                        representation += "["
                        for v in value:
                            representation += " <" + v.string(line_ending=", ") + ">"
                        representation += "]"
                    else:
                        representation += _format_name(name) + ": " + str(value)
                representation += line_ending

        representation = representation.removesuffix(line_ending)
        return representation

    def print(self):
        print(self.string())

    @classmethod
    def get_attr_names(cls):
        return list(cls.__annotations__.keys())

    @classmethod
    def get_attr_pbs_names(cls):
        attr_pbs_names = []
        for k in cls.__annotations__.keys():
            attr_pbs_names.append(_format_pbs(k))
        return attr_pbs_names

    @classmethod
    def get_attr_dict(cls):
        return dict(zip(cls.get_attr_pbs_names(), cls.get_attr_names()))

    @classmethod
    def get_attr_types(cls):
        attr_pbs_names = cls.get_attr_names()
        attr_string = []
        attr_list = []
        attr_basedata = []
        for n in attr_pbs_names:
            anot = cls.__annotations__[n]
            if isinstance(anot, type):
                if issubclass(anot, BaseData):
                    attr_basedata.append(n)
                elif anot is str:
                    attr_string.append(n)
            else:
                attr_list.append(n)
        return attr_string, attr_list, attr_basedata


def _format_pbs(name):
    return "".join(word[0].upper() + word[1:] for word in name.split("_"))


def _format_name(name):
    return name.replace("_", " ").capitalize()


def _format_parent(parent):
    return parent.replace("_", " ").upper()
