from unittest import TestCase
import unittest
from secure_all import AccessRequest, AccessManagementException

'''
Librerias para imprimir el directorio
import os
import unittest

RUTA_FICHERO = os.getcwd() + "/" #Para conseguir el directorio actual con getcwd
'''


class TestAccessRequest(TestCase):
    def test_AM_FR_01_I1_dni_valido(self):
        ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(ar.access_code, "235f046512eed071c55175bc43f98097")

    def test_AM_FR_01_I1_8_caracteres(self):
        with self.assertRaises(AccessManagementException) as AME:
            ar = AccessRequest(id_document="1234567Z", full_name="Beatriz Benitez", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)

    def test_AM_FR_01_I1_10_caracteres(self):
        with self.assertRaises(AccessManagementException) as AME:
            ar = AccessRequest(id_document="123456789Z", full_name="Beatriz Benitez", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)

    def test_AM_FR_01_I1_0_letras(self):
        with self.assertRaises(AccessManagementException) as AME:
            ar = AccessRequest(id_document="123456789", full_name="Beatriz Benitez", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)

    def test_AM_FR_01_I1_2_letras(self):
        with self.assertRaises(AccessManagementException) as AME:
            ar = AccessRequest(id_document="1234567AA", full_name="Beatriz Benitez", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)

    def test_AM_FR_01_I1_type(self):
        with self.assertRaises(AccessManagementException) as AME:
            ar = AccessRequest(id_document=132.23, full_name="Beatriz Benitez", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)

    def test_AM_FR_01_I1_letra_invalida(self):
        with self.assertRaises(AccessManagementException) as AME:
            ar = AccessRequest(id_document="12345678D", full_name="Beatriz Benitez", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)

    def test_AM_FR_01_I2_resident(self):
        ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez", access_type="Resident", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(ar.access_code, "3a786e58d213566eacb406680b17c427")

    def test_AM_FR_01_I2_guest(self):
        ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(ar.access_code, "235f046512eed071c55175bc43f98097")

    def test_AM_FR_01_I2_other(self):
        with self.assertRaises(AccessManagementException) as AME:
            ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez", access_type="Other", email_address="100429094@alumnos.uc3m.es", validity=3)

    def test_AM_FR_01_I3_nombre_apellido(self):
        ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(ar.access_code, "235f046512eed071c55175bc43f98097")

    def test_AM_FR_01_I3_nombres_apellido(self):
        ar = AccessRequest(id_document="12345678Z", full_name="Beatriz x Benitez", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)

    def test_AM_FR_01_I3_solo_nombre(self):
        with self.assertRaises(AccessManagementException) as AME:
            ar = AccessRequest(id_document="12345678Z", full_name="Beatriz", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)

    def test_AM_FR_01_I3_nombres_apellidos(self):
        with self.assertRaises(AccessManagementException) as AME:
            ar = AccessRequest(id_document="12345678Z", full_name="Beatriz x Benitez Blazquez", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)

    def test_AM_FR_01_I3_espacio_delante(self):
        with self.assertRaises(AccessManagementException) as AME:
            ar = AccessRequest(id_document="12345678Z", full_name=" Beatriz Benitez", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)

    def test_AM_FR_01_I3_espacio_detras(self):
        with self.assertRaises(AccessManagementException) as AME:
            ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez ", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)

    def test_AM_FR_01_I3_masdeunespacio(self):
        with self.assertRaises(AccessManagementException) as AME:
            ar = AccessRequest(id_document="12345678Z", full_name="Beatriz     Benitez", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)


    """
    def test_something( self ):
        #print("La ruta es: " + RUTA_FICHERO) #Imprimir la ruta actual a utilizar
        self.assertEqual(True, True)
    """


if __name__ == '__main__':
    unittest.main()
