#!/usr/bin/env python3
"""
Unittests and Integration Tests: for untils.py
"""
import unittest
from parameterized import parameterized
import utils
from utils import memoize
from unittest.mock import Mock, patch
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
    This class tests the method access_nested_map from the module utils

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

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence, key: str) -> None:
        """
        This method tests access_nested_map method to raise errors
        with certain inputs
        """
        with self.assertRaisesRegex(KeyError, key):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    This class tests the method get_json from the module utils

    Methods:
        test_get_json: tests the method and checks if it returns
        what its supposed to
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Mapping) -> None:
        """
        This method tests get_json using a mock object to patch
        requests.get and predict expected return value
        """
        with patch('utils.requests') as mock_requests:
            mock_response = Mock()
            mock_response.json.return_value = test_payload

            mock_requests.get.return_value = mock_response

            response = utils.get_json(test_url)
            mock_requests.get.assert_called_once_with(test_url)
            self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """
    This class tests the wrapper method memoize from the module utils

    Methods:
    test_memoize: tests the method and checks if it behaves properly
    """
    def test_memoize(self) -> None:
        """
        This method tests memoize wrapper using a mock object to track
        the number of calls and a class to see if memoize does work as
        expected
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method",
                          return_value=42) as mock_a:
            obj = TestClass()
            ans1 = obj.a_property
            ans2 = obj.a_property
            self.assertEqual(ans1, 42)
            self.assertEqual(ans2, 42)
            mock_a.assert_called_once()


if __name__ == "__main__":
    unittest.main()
