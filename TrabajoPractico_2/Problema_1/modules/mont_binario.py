# modules/monticulo_binario.py

class MonticuloBinario:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def insert(self, elemento):
        self.data.append(elemento)
        self.heapify_up(len(self.data) - 1)

    def extract_min(self):
        if self.is_empty():
            raise IndexError("Montículo vacío")

        self.swap(0, len(self.data) - 1)
        min_elemento = self.data.pop()
        self.heapify_down(0)
        return min_elemento

    def heapify_up(self, index):
        padre = (index - 1) // 2
        if index > 0 and self.data[index] < self.data[padre]:
            self.swap(index, padre)
            self.heapify_up(padre)

    def heapify_down(self, index):
        hijo_izq = 2 * index + 1
        hijo_der = 2 * index + 2
        menor = index

        if hijo_izq < len(self.data) and self.data[hijo_izq] < self.data[menor]:
            menor = hijo_izq
        if hijo_der < len(self.data) and self.data[hijo_der] < self.data[menor]:
            menor = hijo_der
        if menor != index:
            self.swap(index, menor)
            self.heapify_down(menor)

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
