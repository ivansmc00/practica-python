import unittest
from lista import estaEnRango

class estaEnRangoTest(unittest.TestCase):
    
    def setUp(self):
        print("Empezando test para función estaEnRango...")

    def tearDown(self):
        print("Test para función estaEnRango finalizada")
    
    def test_validNumber(self):
        result = estaEnRango(10,1,20)
        self.assertTrue(result)

    def test_higherNumber(self):
        result = estaEnRango(21,1,20)
        self.assertFalse(result)

    def test_lowerNumber(self):
        result = estaEnRango(0,1,20)
        self.assertFalse(result)
    
    def test_textInput(self):
        result = estaEnRango("Texto",1,20)
        self.assertFalse(result)
    
    def test_noTextInput(self):
        result = estaEnRango('',1,20)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()