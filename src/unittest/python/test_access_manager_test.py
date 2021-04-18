from unittest import TestCase
from src.main.python.secure_all.access_manager import AccessManager
from src.main.python.secure_all.access_management_exception import AccessManagementException


class TestAccessManager(TestCase):
    def test_open_door_clave_no_exp(self):
        my_key = AccessManager()
        result = my_key.open_door("821c9d9cf4ab2255fd53a8365042a12f49f183e82b811f8ae2dc3ebe941b3bb4")
        self.assertEqual(True, result)

    def test_open_door_no_clave(self):
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as AME:
            my_key.open_door("1111111111111111111111111111111111111111111111111111111111111111")

    def test_check_key_clave_valida(self):
        my_key = AccessManager()
        result = my_key.check_key("821c9d9cf4ab2255fd53a8365042a12f49f183e82b811f8ae2dc3ebe941b3bb4")
        self.assertEqual(True, result)

    def test_check_key_clave_invalida(self):
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as AME:
            result = my_key.check_key("x")

    def test_read_key_file_fichero_datos(self):
        my_key = AccessManager()
        result = my_key.open_door("821c9d9cf4ab2255fd53a8365042a12f49f183e82b811f8ae2dc3ebe941b3bb4")
        self.assertEqual(True, result)
