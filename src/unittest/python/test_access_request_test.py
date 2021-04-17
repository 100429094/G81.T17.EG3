from unittest import TestCase
import unittest
from src.main.python.secure_all.access_request import AccessRequest
from src.main.python.secure_all.access_management_exception import AccessManagementException


class TestAccessRequest(TestCase):

    def test_AM_FR_01_I1_dni_valido(self):
        ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                           access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(ar.access_code, "299350376deadf07044aaa5035f93a6f")

    def test_AM_FR_01_I1_8_caracteres(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="1234567Z", full_name="Beatriz Benitez",
                          access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(AME.exception.message, "EXCEPTION: El DNI recibido no es valido o no tiene un formato valido")

    def test_AM_FR_01_I1_10_caracteres(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="123456789Z", full_name="Beatriz Benitez",
                          access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(AME.exception.message, "EXCEPTION: El DNI recibido no es valido o no tiene un formato valido")

    def test_AM_FR_01_I1_0_letras(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="123456789", full_name="Beatriz Benitez",
                          access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(AME.exception.message, "EXCEPTION: El DNI recibido no es valido o no tiene un formato valido")

    def test_AM_FR_01_I1_2_letras(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="1234567AA", full_name="Beatriz Benitez",
                          access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(AME.exception.message, "EXCEPTION: El DNI recibido no es valido o no tiene un formato valido")

    def test_AM_FR_01_I1_type(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document=132.23, full_name="Beatriz Benitez",
                          access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(AME.exception.message, "EXCEPTION: El DNI recibido no es valido o no tiene un formato valido")

    def test_AM_FR_01_I1_letra_invalida(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="12345678D", full_name="Beatriz Benitez",
                          access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(AME.exception.message, "EXCEPTION: El DNI recibido no es valido o no tiene un formato valido")

    def test_AM_FR_01_I2_resident(self):
        ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                           access_type="Resident", email_address="100429094@alumnos.uc3m.es", validity=0)
        self.assertEqual(ar.access_code, "eeadab980b4ae41412aed7a991750fab")

    def test_AM_FR_01_I2_guest(self):
        ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                           access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(ar.access_code, "299350376deadf07044aaa5035f93a6f")

    def test_AM_FR_01_I2_other(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                          access_type="Other", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(AME.exception.message, "EXCEPTION: El tipo de acceso solicitado no es valido")

    def test_AM_FR_01_I3_nombre_apellido(self):
        ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                           access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(ar.access_code, "299350376deadf07044aaa5035f93a6f")

    def test_AM_FR_01_I3_nombres_apellido(self):
        ar = AccessRequest(id_document="12345678Z", full_name="Beatriz x Benitez",
                           access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)

    def test_AM_FR_01_I3_solo_nombre(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="12345678Z", full_name="Beatriz",
                          access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(AME.exception.message, "EXCEPTION: La cadena de nombre y apellido no es válida")

    def test_AM_FR_01_I3_nombres_apellidos(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="12345678Z", full_name="Beatriz x Benitez Blazquez",
                          access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(AME.exception.message, "EXCEPTION: La cadena de nombre y apellido no es válida")

    def test_AM_FR_01_I3_espacio_delante(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="12345678Z", full_name=" Beatriz Benitez",
                          access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(AME.exception.message, "EXCEPTION: La cadena de nombre y apellido no es válida")

    def test_AM_FR_01_I3_espacio_detras(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez ",
                          access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(AME.exception.message, "EXCEPTION: La cadena de nombre y apellido no es válida")

    def test_AM_FR_01_I3_masdeunespacio(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="12345678Z", full_name="Beatriz     Benitez",
                          access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(AME.exception.message, "EXCEPTION: La cadena de nombre y apellido no es válida")

    def test_AM_FR_01_I4_email_valido(self):
        ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                           access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(ar.access_code, "299350376deadf07044aaa5035f93a6f")

    def test_AM_FR_01_I4_email_vacio(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                          access_type="Guest", email_address="", validity=3)
        self.assertEqual(AME.exception.message, "EXCEPTION: El formato de correo electrónico no es válido")

    def test_AM_FR_01_I4_email_sin_nombre(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                          access_type="Guest", email_address="@alumnos.uc3m.es", validity=3)
        self.assertEqual(AME.exception.message, "EXCEPTION: El formato de correo electrónico no es válido")

    def test_AM_FR_01_I4_email_sin_arroba(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                          access_type="Guest", email_address="100429094alumnos.uc3m.es", validity=3)
        self.assertEqual(AME.exception.message, "EXCEPTION: El formato de correo electrónico no es válido")

    def test_AM_FR_01_I4_email_sin_company(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                          access_type="Guest", email_address="100429094@.es", validity=3)
        self.assertEqual(AME.exception.message, "EXCEPTION: El formato de correo electrónico no es válido")

    def test_AM_FR_01_I4_email_sin_punto(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                          access_type="Guest", email_address="100429094@alumnoses", validity=3)
        self.assertEqual(AME.exception.message, "EXCEPTION: El formato de correo electrónico no es válido")

    def test_AM_FR_01_I4_email_sin_com(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                          access_type="Guest", email_address="100429094@alumnos.", validity=3)
        self.assertEqual(AME.exception.message, "EXCEPTION: El formato de correo electrónico no es válido")

    def test_AM_FR_01_I4_email_caracter_invalido(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                          access_type="Guest", email_address="100429094@alum!os.uc3m.es", validity=3)
        self.assertEqual(AME.exception.message, "EXCEPTION: El formato de correo electrónico no es válido")

    def test_AM_FR_01_I5_validity_guest_1(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                          access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=1)
        self.assertEqual(AME.exception.message, "EXCEPTION: El número de días no tiene un valor válido")

    def test_AM_FR_01_I5_validity_guest_2(self):
        ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                           access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=2)
        self.assertEqual(ar.access_code, "4bbd21090fb63e6810eb67adc3fcdcee")

    def test_AM_FR_01_I5_validity_guest_3(self):
        ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                           access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(ar.access_code, "299350376deadf07044aaa5035f93a6f")

    def test_AM_FR_01_I5_validity_guest_14(self):
        ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                           access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=14)
        self.assertEqual(ar.access_code, "2c3332d44cc5ef4c63af11fefd9b4f18")

    def test_AM_FR_01_I5_validity_guest_15(self):
        ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                           access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=15)
        self.assertEqual(ar.access_code, "e5148debcfde73b070d3bc94849a0834")

    def test_AM_FR_01_I5_validity_guest_16(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                          access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=16)
        self.assertEqual(AME.exception.message, "EXCEPTION: El número de días no tiene un valor válido")

    def test_AM_FR_01_I5_validity_resident_0(self):
        ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                           access_type="Resident", email_address="100429094@alumnos.uc3m.es", validity=0)
        self.assertEqual(ar.access_code, "eeadab980b4ae41412aed7a991750fab")

    def test_AM_FR_01_I5_validity_resident_1(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                          access_type="Resident", email_address="100429094@alumnos.uc3m.es", validity=1)
        self.assertEqual(AME.exception.message, "EXCEPTION: El número de días no tiene un valor válido")

    def test_AM_FR_01_I5_validity_resident_2(self):
        with self.assertRaises(AccessManagementException) as AME:
            AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                          access_type="Resident", email_address="100429094@alumnos.uc3m.es", validity=2)
        self.assertEqual(AME.exception.message, "EXCEPTION: El número de días no tiene un valor válido")

    def test_AM_FR_01_O1_valido(self):
        ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                           access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(ar.access_code, "299350376deadf07044aaa5035f93a6f")

    def test_AM_FR_01_O1_invalido(self):
        ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez",
                           access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertNotEqual(ar.access_code, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    def test_AM_FR_01_O2_dni(self):
        with self.assertRaises(AccessManagementException) as AME:
            ar = AccessRequest(id_document="1234567Z", full_name="Beatriz Benitez", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(AME.exception.message, AccessRequest.MENSAJE_EXCEPCION_DNI)

    def test_AM_FR_01_O2_access_type(self):
        with self.assertRaises(AccessManagementException) as AME:
            ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez", access_type="Other", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(AME.exception.message, AccessRequest.MENSAJE_EXCEPCION_ACCESS_TYPE)

    def test_AM_FR_01_O2_name(self):
        with self.assertRaises(AccessManagementException) as AME:
            ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez x y z", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=3)
        self.assertEqual(AME.exception.message, AccessRequest.MENSAJE_EXCEPCION_NAME)

    def test_AM_FR_01_O2_email(self):
        with self.assertRaises(AccessManagementException) as AME:
            ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez", access_type="Guest", email_address="alumnos.uc3m.es", validity=3)
        self.assertEqual(AME.exception.message, AccessRequest.MENSAJE_EXCEPCION_EMAIL)

    def test_AM_FR_01_O2_validity(self):
        with self.assertRaises(AccessManagementException) as AME:
            ar = AccessRequest(id_document="12345678Z", full_name="Beatriz Benitez", access_type="Guest", email_address="100429094@alumnos.uc3m.es", validity=500)
        self.assertEqual(AME.exception.message, AccessRequest.MENSAJE_EXCEPCION_VALIDITY)


if __name__ == '__main__':
    unittest.main()
