# 🐍Nombre del proyecto: Temperaturas_DB 

Breve descripción del proyecto:

En este proyecto se puede registrar, consultar, eliminar y analizar distintas tempperaturas diarias, que se encuentran almacenadas en una estructura de árbol AVL.

---
## 🏗Arquitectura General

El proyecto está dividido en 3 módulos principales que continen la estructura del funcionamiento del proyecto. Estos módulos se encuentran en la carpeta modules y son:
   * nodo_AVL.py: se define la clase NodoAVL que va a representar los nodos del árbol. Cada uno almacena una fecha y una temperatura, y referencias para mantener el orden y equilibrio del árbol.  
   * arbol_AVL.py: se define la clase ArbolAVL, que utilizando las funciones definidas en nodo_AVL.py deffine la busqueda, insersión y eliinación de estos para garantixar el balanceo del árbol
   * temperatura_db.py: se define la clase TemperaturasDB que usa el árbol AVL para el almacenamiento, consulta, comparación, eliminación, actualización o reemplazo de temperaturas dentro de un rango de tiempo. 
En la carpeta [tests](./tests) se encuentra el archivo test_temperatura.py en el cual se corrobora el correcto funcionamiento de las funciones definidas. 

En este proyecto no se generan gráficas, pero en caso de que hubiera se encontrarían en la carpeta [data](./data). 

---
## 📑Dependencias

1. **Python 3.x**
2. datetime (incluido en la biblioteca estándar)
3. No se requieren dependencias externas para el funcionamiento del proyecto, en caso de que hubiera se encontrarían listadas en  requirements.txt, disponible en la carpeta [deps](./deps).

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

- Biasoli, Ana Inés
- Taborda, Verónica

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
