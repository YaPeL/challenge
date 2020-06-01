import json
import pytest
from challenge.challenge import f
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
                          # Regular case
                          (DEFAULT_JSON, DEFAULT_PROPS, DEFAULT_RESULT),
                          # Test what happens if we have a property missing on the json
                          (DEFAULT_JSON, MISSING_VALUE_PROPS, MISSING_VALUE_RESULT),
                          # check special case where prop hints at an array, but the json contains a string
                          (DEFAULT_JSON, STRING_INSTEAD_OF_ARRAY_PROP, MISSING_STRING_RESULT),
                          # check what happens with an empty json
                          (EMPTY_JSON, DEFAULT_PROPS, EMPTY_RESULT),
                          ])
def test_f_function(obj, properties, expected):
    result = f(obj, properties)
    assert result == expected
