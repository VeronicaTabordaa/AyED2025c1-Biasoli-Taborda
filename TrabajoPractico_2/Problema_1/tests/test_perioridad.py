# Archivo de test para realizar pruebas unitarias del modulo1


import unittest
from modules.Prioridad_Queue import PrioridadQueue

class TestPrioridadQueue(unittest.TestCase):
    def test_orden(self):
        pq = PrioridadQueue()
        pq.push("A", 2)
        pq.push("B", 1)
        pq.push("C", 3)

        self.assertEqual(pq.pop(), "B")
        self.assertEqual(pq.pop(), "A")
        self.assertEqual(pq.pop(), "C")

    def test_orden_de_llegada(self):
        pq = PrioridadQueue()
        pq.push("A", 1)
        pq.push("B", 1)
        pq.push("C", 1)

        self.assertEqual(pq.pop(), "A")
        self.assertEqual(pq.pop(), "B")
        self.assertEqual(pq.pop(), "C")


if __name__ == '__main__':
    unittest.main()