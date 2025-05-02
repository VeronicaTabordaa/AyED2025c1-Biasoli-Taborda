import time
import matplotlib.pyplot as plt
from ListaDobleEnlazada import ListaDoblementeEnlazada

def medir_tiempos(max_n, paso):
    ns = list(range(paso, max_n + 1, paso))
    tiempos_len = []
    tiempos_copiar = []
    tiempos_invertir = []

    for n in ns:
        print(f"Probando con tamaño N = {n}")  # Verifica la progresión del bucle

        lista = ListaDoblementeEnlazada()
        for i in range(n):
            lista.agregar__al__final(i)

        # Medir len()
        inicio = time.time()
        _ = len(lista)
        tiempos_len.append(time.time() - inicio)
        print(f"Tiempo len({n}): {tiempos_len[-1]:.6f} segundos")

        # Medir copiar()
        inicio = time.time()
        _ = lista.copiar()
        tiempos_copiar.append(time.time() - inicio)
        print(f"Tiempo copiar({n}): {tiempos_copiar[-1]:.6f} segundos")

        # Medir invertir()
        inicio = time.time()
        lista.invertir()
        tiempos_invertir.append(time.time() - inicio)
        print(f"Tiempo invertir({n}): {tiempos_invertir[-1]:.6f} segundos")

    print("Finalización de la medición de tiempos.")
    return ns, tiempos_len, tiempos_copiar, tiempos_invertir


def graficar(ns, tiempos_len, tiempos_copiar, tiempos_invertir): 
    plt.figure(figsize=(10, 6)) 
    plt.plot(ns, tiempos_len, label="len() - O(1)", marker='o') 
    plt.plot(ns, tiempos_copiar, label="copiar() - O(n)", marker='s') 
    plt.plot(ns, tiempos_invertir, label="invertir() - O(n)", marker='^') 
    plt.xlabel("Cantidad de elementos (N)") 
    plt.ylabel("Tiempo de ejecución (segundos)") 
    plt.title("Rendimiento de métodos sobre ListaDobleEnlazada") 
    plt.legend() 
    plt.grid(True) 
    plt.tight_layout() 
    plt.show()

print("Ejecutando la prueba de rendimiento...")
ns, tiempos_len, tiempos_copiar, tiempos_invertir = medir_tiempos(max_n=5000, paso=500)
print("Datos recopilados, generando gráfica...")
graficar(ns, tiempos_len, tiempos_copiar, tiempos_invertir)
print("Gráfica generada correctamente.")
