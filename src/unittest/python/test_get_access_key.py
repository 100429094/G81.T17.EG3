from unittest import TestCase
from pathlib import Path
from src.main.python.secure_all import access_management_exception, access_manager


class TestGetAccessKey(TestCase):

    def test_get_access_key_good(self):

        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_ok.json"
        my_key = access_manager.AccessManager()
        key = my_key.get_access_key(my_file)
        self.assertEqual("55ffd7fbee39975b050ac25fe7abc7d31c996b6cccb2fabecaeb3d5711dd74f2", key)

    def test_get_access_key_bad_campo1_del(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_campo1_del.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_campo1_dup(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_campo1_dup.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_comillas_del(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_comillas_del.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_comillas_dup(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_comillas_dup.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_comillas_mod(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_comillas_mod.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_corchete_final_del(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_corchete_final_del.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_corchete_final_dup(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_corchete_final_dup.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_corchete_final_mod(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_corchete_final_mod.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_corchete_inicial_del(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_corchete_inicial_del.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def tests_get_access_key_bad_corchete_inicial_dup(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_corchete_inicial_dup.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_corchete_inicial_mod(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_corchete_inicial_mod.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_dos_puntos_del(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_dos_puntos_del.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_dos_puntos_dup(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_dos_puntos_dup.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_dos_puntos_mod(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_dos_puntos_mod.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_etq1_del(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_etq1_del.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_etq1_dup(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_etq1_dup.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_etq1_mod(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_etq1_mod.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_json_del(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_json_del.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_json_dup(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_json_dup.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_llave_final_del(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_llave_final_del.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_llave_final_dup(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_llave_final_dup.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_llave_final_mod(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_llave_final_mod.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_llave_inicial_del(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_llave_inicial_del.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_llave_inicial_dup(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_llave_inicial_dup.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_llave_inicial_mod(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_llave_inicial_mod.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_separador_del(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_separador_del.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_separador_dup(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_separador_dup.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_separador_mod(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_separador_mod.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val1_del(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val1_del.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val1_dup(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val1_dup.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val1_mod(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val1_mod.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val2_del(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val2_del.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val2_dup(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val2_dup.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val2_mod(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val2_mod.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val3_del(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val3_del.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val3_dup(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val3_dup.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val3_mod(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val3_mod.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val_dato1_del(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val_dato1_del.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val_dato1_dup(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val_dato1_dup.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val_dato3_del(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val_dato3_del.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val_dato3_dup(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val_dato3_dup.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val_etq1_del(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val_etq1_del.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val_etq1_dup(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val_etq1_dup.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val_etq1_mod(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val_etq1_mod.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val_etq2_del(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val_etq2_del.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val_etq2_dup(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val_etq2_dup.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val_etq2_mod(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val_etq2_mod.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val_etq3_del(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val_etq3_del.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val_etq3_dup(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val_etq3_dup.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)

    def test_get_access_key_bad_val_etq3_mod(self):
        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/Json Files/key_bad_val_etq3_mod.json"
        my_key = access_manager.AccessManager()
        self.assertRaises(access_management_exception.AccessManagementException, my_key.get_access_key, my_file)
