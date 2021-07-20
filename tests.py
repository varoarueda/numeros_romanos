import unittest
from romanos import a_numero

class RomanosTests(unittest.TestCase):
    def test_digitos_romanos(self):
        self.assertEqual(a_numero("I"), 1)
        self.assertEqual(a_numero("V"), 5)

    def test_numeros_completos(self):
        self.assertEqual(a_numero("XXV"), 25)
        self.assertEqual(a_numero("XXIV"), 24)

        with self.assertRaises(ValueError):
            a_numero("VC")
            a_numero("IL")
            a_numero("IM")
            a_numero("IC)
            a_numero("XM")
            a_numero("XD")
            




