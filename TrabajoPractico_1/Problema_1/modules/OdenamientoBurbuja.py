# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
import random


def OrdenamientoBurbuja(lista1):
    for extremo in range(len(lista1)-1,0,-1):
        for i in range(extremo):
            if lista1[i]>lista1[i+1]:
                temp = lista1[i]
                lista1[i] = lista1[i+1]
                lista1[i+1] = temp
    return lista1

if __name__=="__main__":
    lista1 = [random.randint(10000,99999) for _ in range(500)]
    #print("Lista 1:", lista1)
    listaordenadaburb = OrdenamientoBurbuja(lista1)
    #print ("lista ordenada:",listaordenadaburb)

contador=0
ordenada = True
while contador < len(listaordenadaburb) - 1:
    if listaordenadaburb[contador] > listaordenadaburb[contador + 1]:  
        ordenada = False
        break  
    contador += 1
if ordenada:
    print("La lista está correctamente ordenada.")
else:
    print("La lista NO está ordenada.")

import time 
import matplotlib.pyplot as plt
#creo funciones para medir tiempo y para graficar

def medir_tiempo(funcion, lista):
    inicio=time.time()
    funcion(lista)
    fin=time.time()
    return fin-inicio

def graficar_tiempos(tiempos, tamanos):
    plt.plot(tamanos, tiempos, marker='o')
    plt.title('Tiempo de ejecución del algoritmo de ordenamiento por burbuja')
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.grid(True)
    plt.show()
    



























'''    def ordenada_si_o_no(lista):
        for i in range(len(listaordenadaburb)-1):
            if listaordenadaburb[i]>listaordenadaburb[i+1]:
                return False
        return True
    
    if ordenada_si_o_no(listaordenadaburb)==True:
        print("está ordenada")
    else:
        print("no está ordenada") '''