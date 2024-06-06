#!/usr/bin/env python3
"""
11. More involved type annotations
"""
from typing import TypeVar, Mapping, Any, Union

V = TypeVar('V')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[V, None] = None) -> Union[Any, V]:
    """
    This function returns an element from a dictionary if its there
    """
    if key in dct:
        return dct[key]
    else:
        return default
