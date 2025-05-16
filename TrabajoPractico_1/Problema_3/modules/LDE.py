
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
        self.__cabeza = None        #con el __ hacemos privados los atributos
        self.__cola = None
        self.__tamanio = 0
    
    #agregamos properties y setter para podes acceder o modificar los atributos privados 

    @property
    def cabeza(self):
        return self.__cabeza
    
    @cabeza.setter
    def cabeza(self, valor):
        self.__cabeza = valor
    
    @property
    def cola(self): 
        return self.__cola
    
    @cola.setter
    def cola(self, valor):
        self.__cola = valor

    @property
    def tamanio(self):
        return self.__tamanio   
    
    @tamanio.setter
    def tamanio(self, valor):
        if valor >= 0:
            self.__tamanio = valor  
        else:
            raise ValueError("El tamaño no puede ser negativo") 
    
    def lista_vacia(self):
        return self.tamanio == 0

    def agregar__al__inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamanio += 1

    def agregar__al__final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.lista_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamanio += 1

    def eliminar_inicio(self):
        if not self.cabeza:
            raise DequeEmptyError("La lista está vacía")
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        if self.cabeza:
            self.cabeza.anterior = None
        else:
            self.cola = None
        self.tamanio -= 1
        return dato

    def __len__(self):
        return self.tamanio

    def __str__(self):
        elementos = []
        actual = self.primero
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return ' '.join(elementos)