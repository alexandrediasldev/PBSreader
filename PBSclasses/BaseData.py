from dataclasses import dataclass


@dataclass()
class BaseData:
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
    def get_attr_class(cls, attr_name):
        return cls.__annotations__[attr_name]

    @classmethod
    def get_attr_pbs_by_types(cls):
        attr_string, attr_list, attr_basedata = cls.get_attr_by_types()
        attr_pbs_string, attr_pbs_list, attr_pbs_basedata = [], [], []
        for k in attr_string:
            attr_pbs_string.append(_format_pbs(k))
        for k in attr_list:
            attr_pbs_list.append(_format_pbs(k))
        for k in attr_basedata:
            attr_pbs_basedata.append(_format_pbs(k))

        return attr_pbs_string, attr_pbs_list, attr_pbs_basedata

    @classmethod
    def get_attr_by_types(cls):
        attr_names = cls.get_attr_names()
        attr_string = []
        attr_list = []
        attr_basedata = []
        for n in attr_names:
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
