# Archivo de test para realizar pruebas unitarias del modulo1

import unittest
import random

def OrdenamientoBurbuja(lista1):
    for extremo in range(len(lista1)-1, 0, -1):
        for i in range(extremo):
            if lista1[i] > lista1[i+1]:
                lista1[i], lista1[i+1] = lista1[i+1], lista1[i]  # Intercambio
    return lista1

class TestOrdenamientoBurbuja(unittest.TestCase):

    def test_lista_ordenada(self):
        lista = [5, 2, 9, 1, 5, 6]
        lista_ordenada = OrdenamientoBurbuja(lista.copy())  # Copia para no modificar original
        self.assertEqual(lista_ordenada, sorted(lista))

    def test_lista_vacia(self):
        lista = []
        lista_ordenada = OrdenamientoBurbuja(lista.copy())
        self.assertEqual(lista_ordenada, [])

    def test_lista_un_elemento(self):
        lista = [7]
        lista_ordenada = OrdenamientoBurbuja(lista.copy())
        self.assertEqual(lista_ordenada, [7])

    def test_lista_numeros_negativos(self):
        lista = [-3, -1, -4, -2, 0]
        lista_ordenada = OrdenamientoBurbuja(lista.copy())
        self.assertEqual(lista_ordenada, sorted(lista))

    def test_lista_grande(self):
        lista = [random.randint(1, 1000) for _ in range(100)]
        lista_ordenada = OrdenamientoBurbuja(lista.copy())
        self.assertEqual(lista_ordenada, sorted(lista))

if __name__ == '__main__':
    unittest.main()
