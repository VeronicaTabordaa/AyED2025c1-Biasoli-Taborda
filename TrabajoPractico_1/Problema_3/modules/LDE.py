
# =========================
# Excepción personalizada
# =========================


class DequeEmptyError(Exception):
    pass


# =========================
# Clase Nodo para la Lista Doblemente Enlazada
# =========================


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None


# =========================
# Clase Lista Doblemente Enlazada
# =========================


class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self._tamanio = 0


    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        if not self.primero:
            self.primero = self.ultimo = nuevo
        else:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo
        self._tamanio += 1


    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if not self.ultimo:
            self.primero = self.ultimo = nuevo
        else:
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        self._tamanio += 1


    def eliminar_inicio(self):
        if not self.primero:
            raise DequeEmptyError("La lista está vacía")
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        if self.primero:
            self.primero.anterior = None
        else:
            self.ultimo = None
        self._tamanio -= 1
        return dato


    def __len__(self):
        return self._tamanio


    def __str__(self):
        elementos = []
        actual = self.primero
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return ' '.join(elementos)
