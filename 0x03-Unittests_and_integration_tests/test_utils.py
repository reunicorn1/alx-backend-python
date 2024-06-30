#!/usr/bin/env python3
"""
Unittests and Integration Tests: for untils.py
"""
import unittest
from parameterized import parameterized
import utils
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
    Union
)


class TestAccessNestedMap(unittest.TestCase):
    """
    This class tests the method access_nested_map from the module untils

    Methods:
        test_access_nested_map: tests the method and checks if it returns
        what its supposed to
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Union[Mapping, int]) -> None:
        """
        Thus method tests access_nested_map method of utils and checks if
        it returns what its supposed to
        """
        result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected)
