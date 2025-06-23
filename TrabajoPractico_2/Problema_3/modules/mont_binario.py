#reutilizo del ejercicio 1 con algunas modificaciones

class MonticuloBinario:
    def __init__(self):
        self.data = [0]  # índice 0 no se usa

    def insert(self, tupla):
        self.data.append(tupla)
        self._subir(len(self.data) - 1)

    def extract_min(self):
        if len(self.data) == 1:
            raise IndexError("Montículo vacío")
        min_elem = self.data[1]
        self.data[1] = self.data[-1]
        self.data.pop()
        if len(self.data) > 1:
            self._bajar(1)
        return min_elem

    def build_heap(self, lista):
        self.data = [0] + lista[:]
        for i in range(len(self.data) // 2, 0, -1):
            self._bajar(i)

    def is_empty(self):
        return len(self.data) <= 1

    def _subir(self, i):
        while i // 2 > 0:
            if self.data[i][0] < self.data[i // 2][0]:
                self.data[i], self.data[i // 2] = self.data[i // 2], self.data[i]
            i = i // 2

    def _bajar(self, i):
        while (i * 2) < len(self.data):
            hijo_min = self._hijo_min(i)
            if self.data[i][0] > self.data[hijo_min][0]:
                self.data[i], self.data[hijo_min] = self.data[hijo_min], self.data[i]
            i = hijo_min

    def _hijo_min(self, i):
        if i * 2 + 1 >= len(self.data):
            return i * 2
        if self.data[i * 2][0] < self.data[i * 2 + 1][0]:
            return i * 2
        return i * 2 + 1

    def remove(self, tupla):
        """Elimina una tupla exacta del montículo (solo si existe)."""
        for i in range(1, len(self.data)):
            if self.data[i] == tupla:
                self.data[i] = self.data[-1]
                self.data.pop()
                if i < len(self.data):
                    self._subir(i)
                    self._bajar(i)
                return
        raise ValueError("Elemento no encontrado")