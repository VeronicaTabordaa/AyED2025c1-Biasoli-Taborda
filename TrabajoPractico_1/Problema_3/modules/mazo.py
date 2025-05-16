# mazo.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.LDE import ListaDoblementeEnlazada  # LDE.py contiene la clase ListaDobleEnlazada
from modules.carta import Carta  # Importa la clase Carta

class DequeEmptyError(Exception):
    pass

# =========================
# Clase Mazo
# =========================

class Mazo:
    def __init__(self):
        self.cartas = ListaDoblementeEnlazada()


    def poner_carta_arriba(self, carta):
        self.cartas.agregar__al__inicio(carta)


    def poner_carta_abajo(self, carta):
        self.cartas.agregar__al__final(carta)


    def sacar_carta_arriba(self, mostrar=False):
        if len(self.cartas) == 0:
            raise DequeEmptyError("El mazo está vacío")
        carta = self.cartas.eliminar_inicio()
        if mostrar:
            #print(f"saca {carta}")
            carta.visible = True
        return carta
      

    def __len__(self):
        return len(self.cartas)


    def __str__(self):
        return str(self.cartas)