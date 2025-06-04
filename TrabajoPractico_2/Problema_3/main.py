import heapq
from collections import defaultdict

# Leer archivo y construir grafo no dirigido
def leer_grafo(filename):
    grafo = defaultdict(list)
    with open(filename, 'r') as archivo:
        for linea in archivo:
            partes = linea.strip().split(',')
            if len(partes) != 3:
                continue  # Ignora líneas vacías o mal formateadas
            origen = partes[0].strip()
            destino = partes[1].strip()
            try:
                distancia = int(partes[2].strip())
            except ValueError:
                continue  # Ignora si la distancia no es un número válido
            grafo[origen].append((destino, distancia))
            grafo[destino].append((origen, distancia))
    return grafo

# Algoritmo de Prim para generar el Árbol de Expansión Mínima (MST)
def prim(grafo, inicio):
    visitado = set()
    mst = {}
    hijos = defaultdict(list)
    heap = [(0, inicio, None)]  # (peso, nodo_actual, nodo_padre)
    total = 0

    while heap:
        peso, actual, padre = heapq.heappop(heap)
        if actual in visitado:
            continue
        visitado.add(actual)
        if padre:
            mst[actual] = padre
            hijos[padre].append(actual)
            total += peso
        for vecino, peso_vecino in grafo[actual]:
            if vecino not in visitado:
                heapq.heappush(heap, (peso_vecino, vecino, actual))
    return mst, hijos, total

# Mostrar resultados
def mostrar_resultados(mst, hijos, total_leguas):
    aldeas = sorted(set(mst.keys()) | set(hijos.keys()) | {"Peligros"})
    for aldea in aldeas:
        recibe_de = mst.get(aldea, "—")
        envia_a = sorted(hijos.get(aldea, []))
        print(f"Aldea: {aldea}")
        print(f"  Recibe de: {recibe_de}")
        print(f"  Envía a: {', '.join(envia_a) if envia_a else '—'}")
        print()
    print(f"Total de leguas recorridas por las palomas: {total_leguas}")

# Ejecutar todo
if __name__ == "__main__":
    grafo = leer_grafo('aldeas.txt')
    mst, hijos, total_leguas = prim(grafo, 'Peligros')
    mostrar_resultados(mst, hijos, total_leguas)
