
from rearrange import rearrange_name
import unittest  # este módulo introduce métodos de testeo de código múltiples y unitarios

class TestRearrange(unittest.TestCase): # creamos una clase que implemente el test básico
    def test_basic(self):
        testcase = "Lovelace, Ada" # precisamos los parámetros tanto de entrada, como de salida esperada del código
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self): # test para una cadena vacía
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self): # test para un nombre compuesto
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main() # llamamos a la prueba de forma automática






