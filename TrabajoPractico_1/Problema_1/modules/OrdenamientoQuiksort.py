import random
import time
import matplotlib.pyplot as plt


# Implementación de quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[len(arr) // 2]
        menores = [x for x in arr if x < pivote]
        iguales = [x for x in arr if x == pivote]
        mayores = [x for x in arr if x > pivote]
        return quicksort(menores) + iguales + quicksort(mayores)


# Medición de tiempos para listas de tamaño 1 a 1000
def medir_tiempos_quick():
    tamanios = list(range(1, 1001))
    tiempos_quick = []
    for n in tamanios:
        lista = [random.randint(10000, 99999) for _ in range(n)]
        inicio = time.time()
        quicksort(lista)
        tiempos_quick.append(time.time() - inicio)


