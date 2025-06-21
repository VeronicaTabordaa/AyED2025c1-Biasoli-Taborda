# modules/cola_prioridad.py

from modules.mont_binario import MonticuloBinario

class PrioridadQueue:
    def __init__(self):
        self.heap = MonticuloBinario()
        self.contador = 0  # para resolver empates por orden de llegada

    def push(self, item, prioridad):
        # Almacena tupla (prioridad, orden_de_llegada, item)
        self.heap.insert((prioridad, self.contador, item))
        self.contador += 1

    def pop(self):
        if self.heap.is_empty():
            raise IndexError("La cola está vacía")
        return self.heap.extract_min()[-1]  # devolvés solo el item

    def is_empty(self):
        return self.heap.is_empty()

    def size(self):
        return len(self.heap.data)  # opcional
    
    def __iter__(self):
        return (item[2] for item in self.heap.data)  # Devuelve solo el paciente

