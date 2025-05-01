
from Nodo import Nodo

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def __len__(self):
        return self.tamanio  # Devolvemos el tamaño actual de la lista

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
        if self.cola is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamanio += 1
        

    def insertar(self,dato,posicion):
        if posicion <0 or posicion>self.tamanio:
            raise Exception("Posición inválida")
        if posicion == 0:
            self.agregar__al__inicio(dato)
        elif posicion == self.tamanio:
            self.agregar__al__final(dato)
        else: 
            nuevo_nodo=Nodo(dato)
            nodo_actual=self.cabeza
            for i in range(posicion):
                nodo_actual = nodo_actual.siguiente
        
        nuevo_nodo.siguiente = nodo_actual
        nuevo_nodo.anterior = nodo_actual.anterior
        nodo_actual.anterior.siguiente = nuevo_nodo
        nodo_actual.anterior = nuevo_nodo
        self.tamanio += 1


    def __add__(self, otra_lista):
        # Crear una nueva lista que será la concatenación de ambas listas
        lista_concatenada = ListaDoblementeEnlazada()

        # Agregar los elementos de la primera lista
        nodo_actual = self.cabeza
        while nodo_actual:
            lista_concatenada.agregar__al__final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente

        # Agregar los elementos de la segunda lista
        nodo_actual = otra_lista.cabeza
        while nodo_actual:
            lista_concatenada.agregar__al__final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return lista_concatenada
    
    def copiar(self):
        lista_copiada = ListaDoblementeEnlazada()
        nodo_actual = self.cabeza
        while nodo_actual:
            lista_copiada.agregar__al__final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return lista_copiada

    def concatenar(self, otra_lista):
        if not otra_lista.cabeza:  # Si la otra lista está vacía, no hace falta concatenar nada
            return

        # Si la lista original está vacía, simplemente asignamos el primer nodo de la otra lista
        if not self.cabeza:
            self.cabeza = otra_lista.cabeza
            self.cola = otra_lista.cola
        else:
            # Si ambas listas tienen elementos, conectamos el último nodo de la lista original
            # al primer nodo de la otra lista
            self.cola.siguiente = otra_lista.cabeza
            otra_lista.cabeza.anterior = self.cola
            self.cola = otra_lista.cola  # Actualizamos el último nodo de la lista original
