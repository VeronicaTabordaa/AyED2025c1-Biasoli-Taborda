from collections import defaultdict
import heapq

def leer_grafo(file_path):
    graph = defaultdict(list)
    nodes = set()
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            a, b, dist = line.strip().split(", ")
            dist = int(dist)
            graph[a].append((b, dist))
            graph[b].append((a, dist))
            nodes.update([a, b])
    return graph, nodes

def prim_mst(graph, start):
    visited = set([start])
    heap = []
    parents = {start: None}
    children = defaultdict(list)
    total_distance = 0
    
    for vecino, peso in graph[start]:
        heapq.heappush(heap, (peso, start, vecino))
    
    while heap and len(visited) < len(graph):
        peso, u, v = heapq.heappop(heap)
        if v in visited:
            continue
        visited.add(v)
        parents[v] = u
        children[u].append(v)
        total_distance += peso
        
        for vecino, peso_vecino in graph[v]:
            if vecino not in visited:
                heapq.heappush(heap, (peso_vecino, v, vecino))
    
    return parents, children, total_distance

def main():
    file_path = "data/aldeas.txt"  # Aquí está la ruta relativa correcta
    graph, nodes = leer_grafo(file_path)
    
    start = "Peligros"
    padres, hijos, distancia_total = prim_mst(graph, start)
    
    aldeas_ordenadas = sorted(nodes)
    print("Aldeas en orden alfabético:")
    for aldea in aldeas_ordenadas:
        print(aldea)
    
    print("\nPara cada aldea:")
    for aldea in aldeas_ordenadas:
        padre = padres.get(aldea)
        hijos_ = hijos.get(aldea, [])
        if aldea == start:
            print(f"- {aldea}: es la aldea origen, envía noticias a {hijos_}")
        else:
            print(f"- {aldea}: recibe noticia de {padre}, envía a {hijos_}")
    
    print(f"\nDistancia total recorrida por todas las palomas: {distancia_total} leguas")

if __name__ == "__main__":
    main()
