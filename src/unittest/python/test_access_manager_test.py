from unittest import TestCase
from src.main.python.secure_all.access_manager import AccessManager
from src.main.python.secure_all.access_management_exception import AccessManagementException
from pathlib import Path


class TestAccessManager(TestCase):

    def test_open_door_clave_no_exp(self):
        my_key = AccessManager()
        result = my_key.open_door("5612e8c1d700d1268481a80600bb19d1529e158de6a7e77e00afd77297337596")
        self.assertEqual(True, result)

    def test_open_door_clave_fecha_0(self):
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as AME:
            result = my_key.open_door("4612e8c1d700d1268481a80600bb19d1529e158de6a7e77e00afd77297337596")
        self.assertEqual(AME.exception.message, "Clave no encontrada o ha expirado")

    def test_open_door_clave_fecha_exp(self):
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as AME:
            result = my_key.open_door("1d637b7964889b2dd952e9858805dd6a4e0a02d60a3ebdb9dcf7b3c494743625")
        self.assertEqual(AME.exception.message, "Clave no encontrada o ha expirado")

    def test_open_door_no_clave(self):
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as AME:
            my_key.open_door("1111111111111111111111111111111111111111111111111111111111111111")
        self.assertEqual(AME.exception.message, "Clave no encontrada o ha expirado")

    def test_open_door_fichero_vacio(self):
        my_key = AccessManager()
        my_key.pathJson = str(Path.cwd()) + "/../../Almacen_solicitudes/"
        with self.assertRaises(AccessManagementException) as AME:
            my_key.open_door("821c9d9cf4ab2255fd53a8365042a12f49f183e82b811f8ae2dc3ebe941b3bb4")
        self.assertEqual(AME.exception.message, "JSON Decode Error - Formato Json incorrecto")

    def test_check_key_clave_valida(self):
        my_key = AccessManager()
        result = my_key.check_key("821c9d9cf4ab2255fd53a8365042a12f49f183e82b811f8ae2dc3ebe941b3bb4")
        self.assertEqual(True, result)

    def test_check_key_clave_invalida(self):
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as AME:
            result = my_key.check_key("x")
        self.assertEqual(AME.exception.message, "Clave invalida")

    def test_read_key_file_fichero_datos(self):
        my_key = AccessManager()
        result = my_key.open_door("821c9d9cf4ab2255fd53a8365042a12f49f183e82b811f8ae2dc3ebe941b3bb4")
        self.assertEqual(True, result)

    def test_read_key_file_no_fichero(self):
        my_key = AccessManager()
        my_key.pathJson = str(Path.cwd()) + "/../../"
        with self.assertRaises(AccessManagementException) as AME:
            my_key.open_door("821c9d9cf4ab2255fd53a8365042a12f49f183e82b811f8ae2dc3ebe941b3bb4")
        self.assertEqual(AME.exception.message, "Archivo incorrecto")

    def test_read_key_file_fichero_mal(self):
        my_key = AccessManager()
        my_key.pathJson = str(Path.cwd()) + "/../../Almacen_solicitudes/"
        with self.assertRaises(AccessManagementException) as AME:
            my_key.open_door("821c9d9cf4ab2255fd53a8365042a12f49f183e82b811f8ae2dc3ebe941b3bb4")
        self.assertEqual(AME.exception.message, "JSON Decode Error - Formato Json incorrecto")

    def test_loop_0_times(self):
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as AME:
            result = my_key.check_key("x")
        self.assertEqual(AME.exception.message, "Clave invalida")

    def test_loop_1_times(self):
        my_key = AccessManager()
        result = my_key.open_door("821c9d9cf4ab2255fd53a8365042a12f49f183e82b811f8ae2dc3ebe941b3bb4")
        self.assertEqual(True, result)

    def test_loop_2_times(self):
        my_key = AccessManager()
        result = my_key.open_door("d08ce21f3b9c2da48445507518c7e556a0e6c6fb94fd6f3ae3f8307e4705b909")
        self.assertEqual(True, result)

    def test_loop_3_times(self):
        my_key = AccessManager()
        result = my_key.open_door("5612e8c1d700d1268481a80600bb19d1529e158de6a7e77e00afd77297337596")
        self.assertEqual(True, result)

    def test_loop_4_times(self):
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as AME:
            result = my_key.open_door("1d637b7964889b2dd952e9858805dd6a4e0a02d60a3ebdb9dcf7b3c494743625")
        self.assertEqual(AME.exception.message, "Clave no encontrada o ha expirado")

