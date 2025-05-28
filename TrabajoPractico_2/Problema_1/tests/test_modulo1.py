# Archivo de test para realizar pruebas unitarias del modulo1


import unittest
from modules.Prioridad_Queue import PrioridadQueue

class TestPriorityQueue(unittest.TestCase):
    def test_order(self):
        pq = PrioridadQueue()
        pq.push("A", 2)
        pq.push("B", 1)
        pq.push("C", 3)

        self.assertEqual(pq.pop(), "B")
        self.assertEqual(pq.pop(), "A")
        self.assertEqual(pq.pop(), "C")

if __name__ == '__main__':
    unittest.main()