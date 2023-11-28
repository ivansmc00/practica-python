import unittest
from binario import esBinario

class esBinarioTest(unittest.TestCase):
    
    def setUp(self):
        print("Empezando test para función esBinario...")

    def tearDown(self):
        print("Test para función esBinario finalizada")
    
    def test_validNumber(self):
        result = esBinario("1001001")
        self.assertTrue(result)

    def test_noBinaryNumber(self):
        result = esBinario("123456")
        self.assertFalse(result)

    def test_textInput(self):
        result = esBinario("Texto")
        self.assertFalse(result)
    
    def test_noTextInput(self):
        result = esBinario('')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()