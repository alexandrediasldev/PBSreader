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


def _format_name(name):
    return name.replace("_", " ").capitalize()


def _format_parent(parent):
    return parent.replace("_", " ").upper()
