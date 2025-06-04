
from datetime import datetime
from modules.nodo_AVL import altura, actualizar_altura, factor_balance, rotar_derecha, rotar_izquierda
from modules.arbol_AVL import ArbolAVL  # Asegúrate de tener una clase AVL con estas operaciones

class Temperaturas_DB:
    def __init__(self):
        self.__arbol_avl = ArbolAVL()

    def __str_a_fecha(self, fecha_str):
        
        #Convierte una cadena con formato 'dd/mm/aaaa' a un objeto datetime.date.
        #Lanza un error si el formato es incorrecto.
        
        try:
            return datetime.strptime(fecha_str, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError(f"Formato de fecha inválido: '{fecha_str}'. Use 'dd/mm/aaaa'.")

    def guardar_temperatura(self, temperatura, fecha_str):
        #Inserta o actualiza una medición de temperatura para una fecha dada.
        if not isinstance(temperatura, (int, float)):
            return False

    
        fecha = self.__str_a_fecha(fecha_str)
        self.__arbol_avl.insertar(fecha, temperatura)

    def devolver_temperatura(self, fecha_str):
        
        #Devuelve la temperatura correspondiente a una fecha específica.
        #Si no existe, devuelve None.
        
        fecha = self.__str_a_fecha(fecha_str)
        return self.__arbol_avl.buscar(fecha)

    def temperatura_maxima_rango(self, fecha1_str, fecha2_str):
        #Retorna la temperatura máxima registrada entre dos fechas (inclusive).
        fecha1 = self.__str_a_fecha(fecha1_str)
        fecha2 = self.__str_a_fecha(fecha2_str)
        return self.__arbol_avl.max_valor_rango(fecha1, fecha2)

    def temperatura_minima_rango(self, fecha1_str, fecha2_str):
        #Retorna la temperatura mínima registrada entre dos fechas (inclusive).
        
        fecha1 = self.__str_a_fecha(fecha1_str)
        fecha2 = self.__str_a_fecha(fecha2_str)
        return self.__arbol_avl.min_valor_rango(fecha1, fecha2)

    def extremos_temperatura_rango(self, fecha1_str, fecha2_str):
        #Retorna una tupla con la temperatura mínima y máxima entre dos fechas (inclusive).
        minimo = self.temperatura_minima_rango(fecha1_str, fecha2_str)
        maximo = self.temperatura_maxima_rango(fecha1_str, fecha2_str)
        return (minimo, maximo)

    def eliminar_temperatura(self, fecha_str):
        #Elimina la medición de temperatura asociada a la fecha indicada.
        
        fecha = self.__str_a_fecha(fecha_str)
        self.__arbol_avl.eliminar(fecha)

    def devolver_temperaturas_rango(self, fecha1_str, fecha2_str):
        #Devuelve una lista de temperaturas en el rango dado con formato:
        #"dd/mm/aaaa: temperatura ºC"<
        fecha1 = self.__str_a_fecha(fecha1_str)
        fecha2 = self.__str_a_fecha(fecha2_str)

        mediciones = self.__arbol_avl.obtener_rango(fecha1, fecha2)
        resultado = []
        for fecha, temp in mediciones:
            resultado.append(f"{fecha.strftime('%d/%m/%Y')}: {temp} ºC")

        return resultado

    def cantidad_muestras(self):
        
        #Retorna la cantidad total de mediciones guardadas.
        return self.__arbol_avl.cantidad_nodos()
