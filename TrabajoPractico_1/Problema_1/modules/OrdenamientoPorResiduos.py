#exp es un dígito específico en el cual se basa el ordenamiento
def ordenamiento_porconteo(lista, exp):      
    n = len(lista)
    lista_datos_ordenados = [0] * n    #esta lista va a contener los datos ordenados
    conteo = [0] * 10    #esta lista es la que va a contar la cantidad de veces que aparece cada dígito en la lista original

    # Contar cuántos números tienen cada dígito en la posición 'exp'
    for i in range(n):
        indice = (lista[i] // exp) % 10
        conteo[indice] += 1

    # Acumular los conteos para saber las posiciones correctas
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # Construir la lista ordenada según el dígito actual
    for i in reversed(range(n)):
        indice = (lista[i] // exp) % 10
        lista_datos_ordenados[conteo[indice] - 1] = lista[i]
        conteo[indice] -= 1

    return lista_datos_ordenados

# Función principal: Ordenamiento Radix
def ordenamiento_radix(lista):
    maximo = max(lista)       # Encontrar el número más grande
    exp = 1                   # Comenzar por las unidades

    # Repetir para cada dígito (unidades, decenas, centenas, etc.)
    while maximo // exp > 0:
        lista = ordenamiento_porconteo(lista, exp)
        exp *= 10

    return lista