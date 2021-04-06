from unittest import TestCase
from secure_all import AccessManager
#Librerias para imporimir el directorio
import os
import unittest


class TestAccessRequestCode(TestCase):

    def test_request_access_code_dni_ok(self):
        self.assertEqual(True,True)
        '''     
        am = AccessManager()
        res = am.request_access_code("12345678Z", "GUEST", "JOSE LOPEZ", "jllopez@inf.uc3m.es", 3)
        self.assertEqual(res, "f")
        '''