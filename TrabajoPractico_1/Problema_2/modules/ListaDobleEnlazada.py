
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from nodo import Nodo

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
 
    #a partir de aca no se usan los __ para los atributos ya que se utilizan las properties y los setters

    def lista_vacia(self):
        return self.tamanio == 0

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
        if self.lista_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamanio += 1
        
    def insertar(self,dato,posicion):
        if posicion < 0 or posicion > self.tamanio:
            raise Exception("Posición inválida")
        
        if posicion == 0:
            self.agregar__al__inicio(dato)
            return
        
        elif posicion == self.tamanio:
            self.agregar__al__final(dato)
            return
        
        nuevo_nodo=Nodo(dato)
        nodo_actual = self.cabeza         
        for _ in range(posicion - 1):  # Recorremos hasta la posición anterior
            nodo_actual = nodo_actual.siguiente
        # Ajuste de punteros para insertar en medio
        nuevo_nodo.siguiente = nodo_actual.siguiente
        nuevo_nodo.anterior = nodo_actual
        
        if nodo_actual.siguiente:  # Si existe un nodo después, lo enlazamos correctamente
            nodo_actual.siguiente.anterior = nuevo_nodo
        nodo_actual.siguiente = nuevo_nodo
        self.tamanio += 1  # Aumentamos el tamaño de la lista

    def __iter__(self):
        self._nodo_actual = self.cabeza  # Iniciamos desde la cabeza
        return self

    def __next__(self):
        if self._nodo_actual is None:
            raise StopIteration  # Detener iteración cuando ya no hay nodos
        dato = self._nodo_actual.dato  # Devolver el dato, no el nodo
        self._nodo_actual = self._nodo_actual.siguiente  # Avanzar al siguiente nodo
        return dato

    def __add__(self, otra_lista):
        if not isinstance(otra_lista, ListaDoblementeEnlazada):
            raise TypeError("Se requiere otra instancia de ListaDoblementeEnlazada")
        nueva_lista = ListaDoblementeEnlazada()
        for lista in (self, otra_lista):
            nodo = lista.cabeza
            while nodo:
                nueva_lista.agregar__al__final(nodo.dato)
                nodo = nodo.siguiente
        return nueva_lista

    def copiar(self):
        lista_copiada = ListaDoblementeEnlazada()
        nodo_actual = self.cabeza
        while nodo_actual:
            lista_copiada.agregar__al__final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return lista_copiada
        
    def concatenar(self, otra_lista):
        if otra_lista.lista_vacia():
            return

        nodo_actual = otra_lista.cabeza
        while nodo_actual:
            nuevo_nodo = Nodo(nodo_actual.dato)  # Asumo que tus nodos se crean así
            self.agregar__al__final(nuevo_nodo.dato)
            nodo_actual = nodo_actual.siguiente

    # Método para extraer un elemento de una posición dada
    def extraer(self, posicion=None):
        if self.lista_vacia():
            raise Exception("La lista está vacía")
        
        if posicion is None:
            # Si no se proporciona una posición, extraer el último nodo
            posicion = self.tamanio - 1
        
        if posicion == -1:
            posicion = self.tamanio - 1

        if posicion < 0 or posicion >= self.tamanio:
            raise Exception("Posición fuera de rango")

        # Si la posición es 0 (extraer el primer nodo)
        if posicion == 0:
            dato_extraido = self.cabeza.dato
            if self.cabeza.siguiente:
                self.cabeza = self.cabeza.siguiente
                self.cabeza.anterior = None
            else:
                self.cabeza = None
                self.cola = None
            self.tamanio -= 1
            return dato_extraido

        # Si la posición es la última (extraer el último nodo)
        if posicion == self.tamanio - 1:
            dato_extraido = self.cola.dato
            if self.cola.anterior:
                self.cola = self.cola.anterior
                self.cola.siguiente = None
            else:
                self.cabeza = None
                self.cola = None
            self.tamanio -= 1
            return dato_extraido

        # Extraer un nodo intermedio
        actual = self.cabeza
        for i in range(posicion):
            actual = actual.siguiente

        dato_extraido = actual.dato
        actual.anterior.siguiente = actual.siguiente
        actual.siguiente.anterior = actual.anterior
        self.tamanio -= 1
        return dato_extraido
    
    def invertir(self):
        if self.cabeza is None or self.cabeza == self.cola:
            return
        actual = self.cabeza
        while actual:
            temp = actual.siguiente
            actual.siguiente = actual.anterior
            actual.anterior = temp
            actual = temp  # avanzar al siguiente nodo (el original siguiente)
        self.cabeza, self.cola = self.cola, self.cabeza