import unittest
from lista import estaEnLista

lista = [6, 14, 11, 3, 2, 1, 15, 19]

class estaEnListaTest(unittest.TestCase):

    def setUp(self):
        print("Empezando test para función estaEnLista...")

    def tearDown(self):
        print("Test para función estaEnLista finalizada")
    
    def test_numberInLista(self):
        global lista
        result = estaEnLista(1, lista)
        self.assertTrue(result)

    def test_numberNotInLista(self):
        global lista
        result = estaEnLista(7777777, lista)
        self.assertFalse(result)
    
    def test_textInput(self):
        global lista
        result = estaEnLista("Texto", lista)
        self.assertFalse(result)
    
    def test_noTextInput(self):
        global lista
        result = estaEnLista('', lista)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()