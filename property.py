from constants import (
    ARRAY_START,
    ARRAY_END,
    PROPERTY_SEPARATOR,
    JSON_PROPERTY
    )


class Property:
    def __init__(self, prop: str):
        prop_pos = prop.find(ARRAY_START)
        self.is_array = prop_pos > -1
        if self.is_array:
            self.prop = prop[:prop_pos]
            self.pos = int(prop[prop_pos + 1: prop.find(ARRAY_END)])
        else:
            self.prop = prop

    def access(self, obj: dict) -> JSON_PROPERTY:
        result = obj[self.prop]
        if self.is_array:
            if isinstance(result, list):
                result = result[self.pos]
            else:
                raise TypeError("List expected, got string instead")
        return result


class ChainProperty:

    def __init__(self, chain: str):
        self.properties = chain
        self.chain = chain.split(PROPERTY_SEPARATOR)

    def get_value(self, foo: dict) -> JSON_PROPERTY:
        pos = Property(self.chain.pop(0)).access(foo)
        for n in self.chain:
            pos = Property(n).access(pos)
        return pos

    def __str__(self) -> str:
        return self.properties
