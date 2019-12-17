import unittest 
from pruebas import validarusuario

class TestvalidarUsuario(unittest, TestCase):
    def testvalidar(self):
        self.assertAlmostEqual(validarusuario('hola'),'felix')
        self.assertAlmostEqual(validarusuario('felix'),'hola')
        self.assertAlmostEqual(validarusuario('felix'),'felix')