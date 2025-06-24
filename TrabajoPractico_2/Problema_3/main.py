from modules.grafo import Grafo
from modules.Prim import prim

# Ruta del archivo con las conexiones entre aldeas (formato: aldea1, aldea2, peso)
ruta = 'data/aldeas.txt'  
# Crear grafo de aldeas
grafo_aldeas = Grafo()

# Leer el archivo e insertar aristas en el grafo
with open(ruta, 'r') as archivo_datos:
    for linea in archivo_datos:
        datos = linea.strip().split(',')
        if len(datos) != 3:
            continue  # línea mal formateada    

        aldea1 = datos[0].strip()
        aldea2 = datos[1].strip()
        peso = int(datos[2].strip())

        grafo_aldeas.agregarArista(aldea1, aldea2, peso)

# Ejecutar Prim desde la aldea "Peligros"
inicio = grafo_aldeas["Peligros"]
prim(grafo_aldeas, inicio)

nombres_aldeas = grafo_aldeas.obtenerVertices()
ordenadas = sorted(nombres_aldeas)
print("📜 Lista de aldeas en orden alfabético:")
for nombre in ordenadas:
    print(f"- {nombre}")
print()

# Mostrar origen de la noticia y las aldeas a las que se reenvía
print("🔄 Propagación de la noticia:\n")
for nombre in ordenadas:
    aldea = grafo_aldeas[nombre]
    if aldea.id == "Peligros":
        print(f"Aldea: {aldea.id}, Predecesor: -----, Siguientes: {aldea.siguiente}")
    else:
        print(f"Aldea: {aldea.id}, Predecesor: {aldea.predecesor.id}, Siguientes: {aldea.siguiente}")

# Cálculo del costo total de propagación
costo_total = 0
for clave in grafo_aldeas.obtenerVertices():
    nodo = grafo_aldeas[clave]
    costo_total += nodo.distancia

print(f"\n📏 Distancia total recorrida por las palomas: {costo_total} leguas")
