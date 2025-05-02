# mazo.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from LDE import ListaDoblementeEnlazada  # LDE.py contiene la clase ListaDobleEnlazada
from carta import Carta  # Importa la clase Carta

#from modules.LDE import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada
import random

class DequeEmptyError(Exception):
    pass

# =========================
# Clase Mazo
# =========================

class Mazo:
    def __init__(self):
        self.cartas = ListaDoblementeEnlazada()


    def poner_carta_arriba(self, carta):
        self.cartas.insertar_inicio(carta)


    def poner_carta_abajo(self, carta):
        self.cartas.insertar_final(carta)


    def sacar_carta_arriba(self, mostrar=False):
        if len(self.cartas) == 0:
            raise DequeEmptyError("El mazo está vacío")
        carta = self.cartas.eliminar_inicio()
        if mostrar:
            print(f"saca {carta}")
        return carta
      

    def __len__(self):
        return len(self.cartas)


    def __str__(self):
        return str(self.cartas)