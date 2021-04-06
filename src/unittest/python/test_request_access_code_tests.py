import unittest
from secure_all import AccessManager
#Librerias para imporimir el directorio
import os
import unittest

RUTA_FICHERO = os.getcwd() + "/" #Para conseguir el directorio actual con getcwd


class MyTestCase(unittest.TestCase):
    def test_something( self ):
        print("La ruta es: " + RUTA_FICHERO) #Imprimir la ruta actual a utilizar
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
