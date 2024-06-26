#!/usr/bin/env python3
"""
11. More involved type annotations
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    This function returns an element from a dictionary if its there
    """
    if key in dct:
        return dct[key]
    else:
        return default
