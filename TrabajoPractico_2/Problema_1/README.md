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
- En la carpeta modules se encuentran los archivos: 
  - mont_binario.py: implementación propia de un montículo binario min-heap que permite mantener el orden de prioridad 
  - colaprioridadQueue.py: se define la clase PrioridadQueue que utiliza el montículo binario. Es una estructura genérica que nos permite almacenar cualquier tipo de dato con una prioridad asociada
  paciente.py: código provisto por la cátedra que representa a los pacientes con sus atributos: nombre, apelllido, riesgo, etc.  

- En la carpeta apps se encuentra el archivo simular_paciente.py, código también provisto por la cátedra pero con algunas modificaciones. Se adaptó el código para cumplir con el objetivo del problema donde se deben atender los pacientes de acuerdo a su riesgo y orden de llegada. Para esto se utiliza la cola de prioridad implementada. 

- En la carpeta test se encuentra el test_prioridad.py, en el que se encuentran pruebas unitarias que verifican que los elementos se extraen en el orden correcto de prioridad y que en caso de empate de prioridad se respeta el orden de llegada. 

No hay gráficas de los resultados, pero en caso de haberlas se encontrarían disponibles 
en la carpeta [data](./data) del proyecto.

---
## 📑Dependencias

1. **Python 3.x**
2. random, incluido en la biblioteca estándar de Python
3. datetime, incluido en la biblioteca estándar de Python
4. time, incluido en la biblioteca estándar de Python
5. No se requieren dependencias externas para el funcionamiento del proyecto, en caso de que hubiera se encontrarían listadas en  requirements.txt, disponible en la carpeta [deps](./deps).

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
