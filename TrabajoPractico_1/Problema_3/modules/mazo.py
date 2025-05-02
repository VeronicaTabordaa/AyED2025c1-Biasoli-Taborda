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


# =========================
# Clase JuegoGuerra
# =========================


N_TURNOS = 10000


class JuegoGuerra:
   
    valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    palos = ['♠', '♥', '♦', '♣']
   
    def __init__(self, random_seed = 0):
        self._mazo_inicial = Mazo()
        self.mazo_1 = Mazo()
        self.mazo_2 = Mazo()
        self._guerra = False
        self._ganador = ''
        self.empate = False
        self._turno = 0
        self._cartas_en_la_mesa = []
        self._seed = random_seed
   
    @property
    def turnos_jugados(self):
        if self.empate:
            return N_TURNOS
        return self._turno + 1
           
    @property
    def ganador(self):
        return self._ganador
       
    def armar_mazo_inicial(self):
        random.seed(self._seed)
        cartas = [Carta(valor, palo) for valor in JuegoGuerra.valores
                  for palo in JuegoGuerra.palos]
        random.shuffle(cartas)
        for carta in cartas:
            self._mazo_inicial.poner_carta_arriba(carta)
        return self._mazo_inicial
   
    def repartir_cartas(self):
        while len(self._mazo_inicial):
            carta_1 = self._mazo_inicial.sacar_carta_arriba()
            self.mazo_1.poner_carta_arriba(carta_1)
            carta_2 = self._mazo_inicial.sacar_carta_arriba()
            self.mazo_2.poner_carta_arriba(carta_2)
        return self.mazo_1, self.mazo_2
   
    def iniciar_juego(self, ver_partida=True):
        self.armar_mazo_inicial()
        self.repartir_cartas()
        self._cartas_en_la_mesa = []
        self._turno = 0
       
        while len(self.mazo_1) and len(self.mazo_2) and self._turno != N_TURNOS:            
            try:
                if self._guerra:
                    for _ in range(3):
                        self._cartas_en_la_mesa.append(self.mazo_1.sacar_carta_arriba())
                        self._cartas_en_la_mesa.append(self.mazo_2.sacar_carta_arriba())
               
                self._cartas_en_la_mesa.append(self.mazo_1.sacar_carta_arriba(mostrar=True))
                self._cartas_en_la_mesa.append(self.mazo_2.sacar_carta_arriba(mostrar=True))
           
            except DequeEmptyError:
                if len(self.mazo_1):
                    self._ganador = 'jugador 1'
                else:
                    self._ganador = 'jugador 2'
                self._guerra = False
                if ver_partida:
                    print(f'***** {self._ganador} gana la partida *****')  
               
            else:
                if ver_partida:
                    self.mostrar_juego()
               
                if self._cartas_en_la_mesa[-2] > self._cartas_en_la_mesa[-1]:
                    for carta in self._cartas_en_la_mesa:
                        self.mazo_1.poner_carta_abajo(carta)
                    self._cartas_en_la_mesa = []
                    self._guerra = False
                    if len(self.mazo_2):
                        self._turno += 1
                elif self._cartas_en_la_mesa[-1] > self._cartas_en_la_mesa[-2]:
                    for carta in self._cartas_en_la_mesa:
                        self.mazo_2.poner_carta_abajo(carta)
                    self._cartas_en_la_mesa = []
                    self._guerra = False
                    if len(self.mazo_1):                        
                        self._turno += 1
                else:
                    self._guerra = True
                    if ver_partida:
                        print('**** Guerra!! ****')
           
            finally:                      
                if self._turno == N_TURNOS:
                    self.empate = True
                    if ver_partida:
                        print('***** Empate *****')  
                   
        if self._turno != N_TURNOS and not self._ganador:
            if len(self.mazo_1):
                self._ganador = 'jugador 1'
            else:
                self._ganador = 'jugador 2'              
            if ver_partida:
                print(f'***** {self._ganador} gana la partida *****')  
       
    def mostrar_juego(self):
        print(f"Turno: {self._turno+1}")
        print('jugador 1:')        
        print(self.mazo_1)
        print()
        print('              ', end='')
        for carta in self._cartas_en_la_mesa:
            print(carta, end=' ')
        print('\n')
        print('jugador 2:')
        print(self.mazo_2)            
        print()
        print('------------------------------------')
        if self._ganador:
             print(f'***** {self._ganador} gana la partida *****')  


