"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.default_api import DefaultApi  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user_users_post(self):
        """Test case for create_user_users_post

        Create User  # noqa: E501
        """
        pass

    def test_delete_user_users_user_id_delete(self):
        """Test case for delete_user_users_user_id_delete

        Delete User  # noqa: E501
        """
        pass

    def test_read_user_users_user_id_get(self):
        """Test case for read_user_users_user_id_get

        Read User  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()