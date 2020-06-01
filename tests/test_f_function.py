import json
import pytest
from challenge import f
from .resources import (
    DEFAULT_JSON,
    EMPTY_JSON,
    DEFAULT_PROPS,
    MISSING_VALUE_PROPS,
    MISSING_STRING_RESULT,
    MISSING_VALUE_RESULT,
    STRING_INSTEAD_OF_ARRAY_PROP,
    DEFAULT_RESULT,
    EMPTY_RESULT
    )


@pytest.mark.parametrize("obj, properties, expected",
                         [
                          (DEFAULT_JSON, DEFAULT_PROPS, DEFAULT_RESULT),
                          (DEFAULT_JSON, MISSING_VALUE_PROPS, MISSING_VALUE_RESULT),
                          (DEFAULT_JSON, STRING_INSTEAD_OF_ARRAY_PROP, MISSING_STRING_RESULT),
                          (EMPTY_JSON, DEFAULT_PROPS, EMPTY_RESULT),
                          ])
def test_f_function(obj, properties, expected):
    result = f(obj, properties)
    assert result == expected
