# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# # Crear tantos módulos como sea necesario para organizar el código
import random 
import matplotlib.pyplot as plt
import time


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



























