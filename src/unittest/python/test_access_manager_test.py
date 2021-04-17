from unittest import TestCase

from secure_all import AccessRequest
from src.main.python.secure_all import access_management_exception, access_manager


class TestAccessManager(TestCase):
    def test_open_door_clave_no_exp(self):
        my_key = access_manager.AccessManager()
        result = my_key.open_door("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.assertEqual(True, result)
