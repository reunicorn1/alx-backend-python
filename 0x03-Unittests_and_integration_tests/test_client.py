#!/usr/bin/env python3
"""
Unittests and Integration Tests: client.py
"""
import unittest
from parameterized import parameterized, parameterized_class
import client
import fixtures
from unittest.mock import Mock, patch, PropertyMock
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
    Union
)


class TestGithubOrgClient(unittest.TestCase):
    """
    This class tests the class GithubOrgClient of client module

    Methods:
    -------
    test_org: this methods tests that GithubOrgClient.org returns the
    correct value.
    """
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False})
    ])
    @patch("client.get_json")
    def test_org(self, input_value: str, result: Mapping,
                 mock_get: Mock) -> None:
        """
        this methods tests that GithubOrgClient.org returns the
        correct value.
        """
        org_url = "https://api.github.com/orgs/{org}"

        mock_get.return_value = result

        output = client.GithubOrgClient(input_value).org
        mock_get.assert_called_once_with(org_url.format(org=input_value))
        self.assertEqual(output, result)

    def test_public_repos_url(self):
        """
        This method tests that GithubOrgClient._public_repos_url returns
        the expected value
        """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            payload = {"repos_url": "https://api.github.com/orgs/google/repo"}
            mock_org.return_value = payload
            output = client.GithubOrgClient("Google")._public_repos_url
            self.assertEqual(output, payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_get: Mock):
        """
        This method tests the GithubOrgClient.public_repos method
        that returns a list
        """
        mock_get.return_value = [
                {
                    'id': 123,
                    'name': 'first',
                    'license': {
                        'key': 'apache-2.0'
                        }
                    },
                {
                    'id': 456,
                    'name': 'second',
                    'license': {
                        'key': 'apache-2.0'
                        }
                    },
                {
                    'id': 789,
                    'name': 'third',
                    'license': {
                        'key': 'apache-1.0'
                        }
                    }
            ]
        url = "https://api.github.com/orgs/google/repos"
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_url:
            mock_public_url.return_value = url
            expected = ["first", "second"]
            output = client.GithubOrgClient("g").public_repos("apache-2.0")
            mock_get.assert_called_once()
            mock_public_url.assert_called_once()
            self.assertEqual(output, expected)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo: Dict[str, Dict], license_key: str,
                         expected: bool) -> None:
        """
        This method tests the GithubOrgClient.has_license method
        that returns a bool
        """
        output = client.GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(output, expected)


@parameterized_class([
    {
        "org_payload": fixtures.TEST_PAYLOAD[0][0],
        "repos_payload": fixtures.TEST_PAYLOAD[0][1],
        "expected_repos": fixtures.TEST_PAYLOAD[0][2],
        "apache2_repos": fixtures.TEST_PAYLOAD[0][3]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    This is an Integration test for the method
    GithubOrgClient.public_repos only mocking the external requests
    """

    @classmethod
    def setUpClass(cls):
        """ Set up class
        """
        config = {'return_value.json.side_effect': [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload,
        ]}
        cls.get_patcher = patch('requests.get', **config)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ Tear down class
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Integration test: public repos"""
        test_class = client.GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("SomeLicence"), [])
        self.mock_get.assert_called()

    def test_public_repos_with_license(self):
        """ Integration test for public repos with License """
        test_class = client.GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("SomeLicence"), [])
        self.assertEqual(
                test_class.public_repos("apache-2.0"), self.apache2_repos)
        self.mock_get.assert_called()


if __name__ == "__main__":
    unittest.main()
