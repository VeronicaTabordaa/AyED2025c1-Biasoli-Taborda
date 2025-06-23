# 🐍"Red de Comunicaciones Aldeanas"

Breve descripción del proyecto: Este proyecto simula una red de comunicación entre aldeas, modelada como un grafo no dirigido. Se utiliza el algoritmo de Prim para encontrar la forma más eficiente de propagar una noticia desde la aldea "Peligros" al resto, minimizando el costo total del recorrido.

---
## 🏗Arquitectura General

El proyecto está estructurado de la siguiente manera: 
- `modules/grafo.py`: implementación del TAD `Grafo`.
- `modules/vertice.py`: definición del objeto `Vertice` con atributos y métodos asociados.
- `modules/cola_prioridad.py`: cola de prioridad basada en un montículo binario personalizado.
- `modules/monticulo_binario.py`: implementación del heap mínimo (`MinHeap`) base 0.
- `modules/prim.py`: implementación del algoritmo de Prim.
- `main.py`: carga del archivo, ejecución del algoritmo y presentación de resultados.
- `data/aldeas.txt`: archivo de entrada con las conexiones entre aldeas.

---
## 📑Dependencias

1. **Python 3.x**
2. Dependencias listadas en requierements.txt

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