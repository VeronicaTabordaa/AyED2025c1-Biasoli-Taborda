import heapq
from collections import defaultdict

def leer_grafo(filename):
    grafo = defaultdict(list)
    with open(filename, 'r') as archivo:
        for linea in archivo:
            partes = linea.strip().split(',')
            if len(partes) != 3:
                continue  # Ignora líneas vacías o mal formateadas
            origen, destino, distancia = partes
            distancia = int(distancia)
            grafo[origen].append((destino, distancia))
            grafo[destino].append((origen, distancia))  # Grafo no dirigido
    return grafo

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    predecesores = {nodo: None for nodo in grafo}
    cola = [(0, inicio)]

    while cola:
        distancia_actual, actual = heapq.heappop(cola)

        if distancia_actual > distancias[actual]:
            continue

        for vecino, peso in grafo[actual]:
            nueva_dist = distancia_actual + peso
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                predecesores[vecino] = actual
                heapq.heappush(cola, (nueva_dist, vecino))

    return distancias, predecesores

def reconstruir_camino(predecesores, destino):
    camino = []
    while destino is not None:
        camino.append(destino)
        destino = predecesores[destino]
    return camino[::-1]

def imprimir_resultados(grafo, distancias, predecesores):
    for aldea in sorted(grafo):
        if aldea == "Peligros":
            continue

        camino = reconstruir_camino(predecesores, aldea)
        if len(camino) < 2:
            print(f"Aldea: {aldea}\n  Recibe de: -\n  Envía a: -\n")
            continue

        recibe_de = camino[-2]
        envia_a = camino[1]

        print(f"Aldea: {aldea}")
        print(f"  Recibe de: {recibe_de}")
        print(f"  Envía a: {envia_a}\n")

# --- EJECUCIÓN PRINCIPAL ---

grafo = leer_grafo('data/aldeas.txt')
distancias, predecesores = dijkstra(grafo, "Peligros")
imprimir_resultados(grafo, distancias, predecesores)
