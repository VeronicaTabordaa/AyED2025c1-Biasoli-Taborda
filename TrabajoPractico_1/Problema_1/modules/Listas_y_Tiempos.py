import random
import time
import matplotlib.pyplot as plt

# Importar funciones desde los otros módulos
from OrdenamientoBurbuja import OrdenamientoBurbuja
from OrdenamientoPorResiduos import ordenamiento_radix

# ---------- Función para generar listas ----------
def generar_lista(tamaño):
    return [random.randint(10000, 99999) for _ in range(tamaño)]

# ---------- Función para medir tiempos y graficar ----------
def medir_y_graficar_tiempos():
    tamaños = list(range(1, 1001, 50))
    tiempos_burbuja = []
    tiempos_radix = []

    for n in tamaños:
        lista = generar_lista(n)

        # Bubble Sort
        inicio = time.time()
        OrdenamientoBurbuja(lista.copy())
        tiempos_burbuja.append(time.time() - inicio)

        # Radix Sort
        inicio = time.time()
        ordenamiento_radix(lista.copy())
        tiempos_radix.append(time.time() - inicio)

    # Graficar los tiempos
    plt.figure(figsize=(10, 6))
    plt.plot(tamaños, tiempos_burbuja, label="Burbuja", marker='o')
    plt.plot(tamaños, tiempos_radix, label="Radix Sort", marker='^')
    plt.xlabel("Tamaño de lista")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Comparación de algoritmos de ordenamiento")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ---------- Punto de entrada ----------
if __name__ == "__main__":
    medir_y_graficar_tiempos()
