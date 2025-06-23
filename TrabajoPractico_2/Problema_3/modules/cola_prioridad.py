#reutilizo del ejercicio 1 con algunas modificaciones

from modules.mont_binario import MonticuloBinario

class PrioridadQueue:
    def __init__(self):
        self.heap = MonticuloBinario()
        self.contador = 0
        self.items = {}  # item: (prioridad, orden, item)

    def push(self, item, prioridad):
        tupla = (prioridad, self.contador, item)
        self.heap.insert(tupla)
        self.items[item] = tupla
        self.contador += 1

    def pop(self):
        if self.heap.is_empty():
            raise IndexError("La cola está vacía")
        prioridad, _, item = self.heap.extract_min()
        del self.items[item]
        return (prioridad, item)

    def is_empty(self):
        return self.heap.is_empty()

    def __contains__(self, item):
        return item in self.items

    def decrementarClave(self, item, nueva_prioridad):
        if item not in self.items:
            raise ValueError("Item no encontrado")
        vieja_tupla = self.items[item]
        _, orden, _ = vieja_tupla
        if nueva_prioridad > vieja_tupla[0]:
            raise ValueError("La nueva prioridad es mayor que la actual")

        self.heap.remove(vieja_tupla)
        nueva_tupla = (nueva_prioridad, orden, item)
        self.heap.insert(nueva_tupla)
        self.items[item] = nueva_tupla

    def construirMonticulo(self, lista):
        self.heap.build_heap(lista)
        self.items = {item: (prio, orden, item) for prio, orden, item in lista}

    def __iter__(self):
        return (t[2] for t in self.heap.data[1:])
