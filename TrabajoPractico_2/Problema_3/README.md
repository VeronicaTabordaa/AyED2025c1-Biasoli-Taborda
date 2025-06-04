# 🐍"Red de Comunicaciones Aldeanas"



Breve descripción del proyecto:

Este script modela una red de aldeas conectadas entre sí mediante caminos con pesos (distancias). Utiliza el algoritmo de Dijkstra para determinar el camino más corto desde la aldea "Peligros" hacia todas las demás, con el objetivo de simular cómo se enviarían cartas de manera eficiente entre las aldeas.

Permite identificar:

Desde qué aldea se reciben cartas.

A qué aldea se envían cartas desde cada punto intermedio del camino más corto.
---
## 🏗Arquitectura General

El proyecto está estructurado de forma modular mediante funciones:

leer_grafo(filename): Lee un archivo de texto y construye el grafo como un diccionario de adyacencia.

dijkstra(grafo, inicio): Implementa el algoritmo de Dijkstra para calcular los caminos mínimos desde una aldea origen.

reconstruir_camino(predecesores, destino): Reconstruye el camino más corto desde la aldea origen hasta una aldea destino usando el diccionario de predecesores.

imprimir_resultados(grafo, distancias, predecesores): Muestra los resultados de manera clara, indicando para cada aldea a quién le envía y de quién recibe.

Nota: Las conexiones están definidas en el archivo aldeas.txt, ubicado en la carpeta data.
---
## 📑Dependencias

1. **Python 3.x**
2. **matplotlib** (`pip install matplotlib`)
3. listar dependencias principales
4. Dependencias listadas en requierements.txt

---
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio.

2. **Crear y activar** un entorno virtual.

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   El archivo `requirements.txt` se encuentran en la carpeta [deps](./deps) del proyecto.

---
## 🙎‍♀️🙎‍♂️Autores

- Biasoli Ana, Inés
- Taborda, Verónica

---
