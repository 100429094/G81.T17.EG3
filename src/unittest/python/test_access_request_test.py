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
    """
    def test_AM_FR_01_I1_dni_valido(self):
        ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        pass
    """

    def test_AM_FR_01_I1_8_caracteres(self):
        with self.assertRaises(AccessManagementException) as AME:
            ar = AccessRequest(id_document="1234567Z", full_name="Beatriz Benitez", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)

    """
    def test_something( self ):
        #print("La ruta es: " + RUTA_FICHERO) #Imprimir la ruta actual a utilizar
        self.assertEqual(True, True)
    """

if __name__ == '__main__':
    unittest.main()
