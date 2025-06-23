from modules.cola_prioridad import PrioridadQueue
from modules.grafo import Grafo
from modules.vertice import Vertice
import sys

def prim(grafo: Grafo, inicio: Vertice):
    cp = PrioridadQueue()

    # Inicialización: distancias infinitas, sin predecesor
    for v in grafo:
        v.asignarDistancia(sys.maxsize)
        v.asignarPredecesor(None)

    inicio.asignarDistancia(0)

    # Insertar todos los vértices en la cola con su prioridad inicial
    for v in grafo:
        cp.push(v, v.obtenerDistancia())

    # Algoritmo principal
    while not cp.is_empty():
        _, verticeActual = cp.pop()

        for vecino in verticeActual.obtenerConexiones():
            peso = verticeActual.obtenerPonderacion(vecino)
            if vecino in cp and peso < vecino.obtenerDistancia():
                vecino.asignarDistancia(peso)
                vecino.asignarPredecesor(verticeActual)
                verticeActual.asignarSiguiente(vecino.id)
                cp.decrementarClave(vecino, peso)
