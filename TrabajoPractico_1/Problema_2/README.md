# Lista Doblemente Enlazada en Python


Breve descripción del proyecto:

Este módulo implementa un TAD (Tipo Abstracto de Dato) de lista doblemente enlazada desde cero, sin utilizar estructuras de datos de alto nivel de Python. Permite almacenar y manipular elementos de cualquier tipo que sean comparables, e incluye métodos como inserción, extracción, copia, inversión y concatenación. Además, se analiza la eficiencia de las operaciones mediante gráficas de tiempo de ejecución.



---
## 🏗Arquitectura General

El proyecto está organizado de la siguiente manera:

Clase Nodo: Representa cada nodo de la lista, con punteros al anterior y siguiente nodo, y un valor almacenado.

Clase ListaDobleEnlazada: Contiene los métodos necesarios para manipular la lista (agregar, insertar, extraer, copiar, invertir, concatenar, etc.). Todos los métodos están diseñados para ser eficientes en complejidad temporal y no utilizan listas de Python para almacenar datos.

Manejo de excepciones: Se implementan validaciones para manejar intentos de acceso a posiciones inválidas dentro de la lista.

Tests unitarios: Se proveen casos de prueba para validar el correcto funcionamiento de los métodos.

Medición de rendimiento: Se analizan y grafican los tiempos de ejecución de los métodos __len__, copiar() e invertir() para evaluar su complejidad.



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

- Biasoli, Ana Inés
- Taborda, Veronica
---
