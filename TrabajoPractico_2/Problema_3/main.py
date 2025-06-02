# Leer el archivo aldeas.txt directamente desde el sistema de archivos
file_path = "/mnt/data/aldeas.txt"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Procesar las líneas del archivo para obtener las aristas
edges_from_file = [line.strip().split(', ') for line in lines]
edges_from_file = [(a, b, int(d)) for a, b, d in edges_from_file]

# Crear el grafo
G_file = nx.Graph()
G_file.add_weighted_edges_from(edges_from_file)

# Crear el árbol de expansión mínima desde Peligros
mst_file = nx.minimum_spanning_tree(G_file)
tree_file = nx.bfs_tree(mst_file, source="Peligros")

# Calcular padres e hijos en el árbol
parents_file = {node: None for node in tree_file.nodes}
children_file = {node: [] for node in tree_file.nodes}
for parent, child in tree_file.edges:
    parents_file[child] = parent
    children_file[parent].append(child)

# Aldeas en orden alfabético
aldeas_ordenadas_file = sorted(tree_file.nodes)

# Distancia total recorrida
total_distance_file = sum(mst_file[u][v]['weight'] for u, v in tree_file.edges)

aldeas_ordenadas_file, parents_file, children_file, total_distance_file
