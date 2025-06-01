# Proclema 1: Sala de Emergencias - Triaje de prioridades 

Breve descripción del proyecto:

En el siguiente proyecto se simula una **sala de emergencias**, en la cual se atiende a 
los pacientes de acuerdo al *nivel de riesgo clínico* y orden de llegada. Los de mayor 
riesgo, indicado con **riesgo 1**, deben ser atendidos primero, luego **riesgo 2** y por 
último **riesgo 3**. en caso de que haya 2 pacientes con el mismo riesgo, se atiende a 
quien haya llegado primero. Para lograr esto, se usa una estructura de datos genérica 
(Prioridad Queue), para garantizar que siempre se atienda de acuerdo al riesgo, y en 
caso de empate, en orden de llegada 

---
## 🏗Arquitectura General

El proyecto se encuentra organizado en 3 partes:
      En la carpeta modules se encuentra el archivo Prioridad_Queue.py, donde se define 
      la clase PrioridadQueue que se utiliza para definir el orden y prioridad de atención 
      En la carpeta apps se encuentra el archivo simulacion_triaje.py, donde se implementa 
      el triaje de los pacientes utilizando la clase definida en Prioridad_Queue.py
      En la carpeta test se encuentra el test_prioridad, en el que se encuentran pruebas 
      unitarias que verifican la estructura de datos funcione correctamente. 

No hay gráficas de los resultados, pero en caso de haberlas se encontrarían disponibles 
en la carpeta [data](./data) del proyecto.

---
## 📑Dependencias

1. **Python 3.x**
2. **itertools** (incluida en la biblioteca estándar de python)
3. **heapq** (incluida en la biblioteca estándar de Python)
4. Las dependencias están listadas en `requirements.txt`, disponible en la carpeta [deps](./deps).

---
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio.

2. **Crear y activar** un entorno virtual.

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
---
## 🙎‍♀️🙎‍♂️Autores

- Biasoli, Ana Inés
- Apellido y Nombre del primer integrante

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
