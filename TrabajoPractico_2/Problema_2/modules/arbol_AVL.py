from modules.nodo_AVL import NodoAVL, altura, actualizar_altura, factor_balance, rotar_izquierda, rotar_derecha

class ArbolAVL:
    def __init__(self):
        self.raiz = None
        self._cantidad = 0

    def cantidad_nodos(self):
        """Devuelve la cantidad total de nodos en el árbol."""
        return self._cantidad

    def buscar(self, fecha):
        """Busca la temperatura correspondiente a una fecha exacta."""
        return self._buscar_recursivo(self.raiz, fecha)

    def _buscar_recursivo(self, nodo, fecha):
        if nodo is None:
            return None
        if fecha == nodo.fecha:
            return nodo.temperatura
        elif fecha < nodo.fecha:
            return self._buscar_recursivo(nodo.hijo_izq, fecha)
        else:
            return self._buscar_recursivo(nodo.hijo_der, fecha)

    def insertar(self, fecha, temperatura):
        """Inserta una nueva medición de temperatura o actualiza una existente."""
        self.raiz = self._insertar(self.raiz, fecha, temperatura)
        self.raiz.padre = None  # Asegura que la raíz no tenga padre

    def _insertar(self, nodo, fecha, temperatura):
        if nodo is None:
            self._cantidad += 1
            return NodoAVL(fecha, temperatura)
        if fecha == nodo.fecha:
            nodo.temperatura = temperatura
        elif fecha < nodo.fecha:
            hijo_izq = self._insertar(nodo.hijo_izq, fecha, temperatura)
            nodo.hijo_izq = hijo_izq
            hijo_izq.padre = nodo
        else:
            hijo_der = self._insertar(nodo.hijo_der, fecha, temperatura)
            nodo.hijo_der = hijo_der
            hijo_der.padre = nodo

        actualizar_altura(nodo)
        return self._balancear(nodo)

    def eliminar(self, fecha):
        """Elimina la medición de temperatura asociada a una fecha."""
        self.raiz = self._eliminar(self.raiz, fecha)

    def _eliminar(self, nodo, fecha):
        if nodo is None:
            return None

        if fecha < nodo.fecha:
            nodo.hijo_izq = self._eliminar(nodo.hijo_izq, fecha)
        elif fecha > nodo.fecha:
            nodo.hijo_der = self._eliminar(nodo.hijo_der, fecha)
        else:
            self._cantidad -= 1
            if nodo.hijo_izq is None:
                return nodo.hijo_der
            elif nodo.hijo_der is None:
                return nodo.hijo_izq
            sucesor = self._minimo_nodo(nodo.hijo_der)
            nodo.fecha = sucesor.fecha
            nodo.temperatura = sucesor.temperatura
            nodo.hijo_der = self._eliminar(nodo.hijo_der, sucesor.fecha)

        actualizar_altura(nodo)
        return self._balancear(nodo)

    def _minimo_nodo(self, nodo):
        while nodo.hijo_izq:
            nodo = nodo.hijo_izq
        return nodo

    def _balancear(self, nodo):
        balance = factor_balance(nodo)
        if balance > 1:
            if factor_balance(nodo.hijo_izq) < 0:
                nodo.hijo_izq = rotar_izquierda(nodo.hijo_izq)
            return rotar_derecha(nodo)
        if balance < -1:
            if factor_balance(nodo.hijo_der) > 0:
                nodo.hijo_der = rotar_derecha(nodo.hijo_der)
            return rotar_izquierda(nodo)
        return nodo

    def obtener_rango(self, fecha1, fecha2):
        """Devuelve una lista ordenada de tuplas (fecha, temperatura) entre dos fechas dadas."""
        resultados = []
        self._inorden_rango(self.raiz, fecha1, fecha2, resultados)
        return resultados

    def _inorden_rango(self, nodo, fecha1, fecha2, resultados):
        if nodo is None:
            return
        if fecha1 <= nodo.fecha:
            self._inorden_rango(nodo.hijo_izq, fecha1, fecha2, resultados)
        if fecha1 <= nodo.fecha <= fecha2:
            resultados.append((nodo.fecha, nodo.temperatura))
        if nodo.fecha <= fecha2:
            self._inorden_rango(nodo.hijo_der, fecha1, fecha2, resultados)

    def max_valor_rango(self, fecha1, fecha2):
        """Devuelve la temperatura máxima en el rango de fechas."""
        valores = [temp for _, temp in self.obtener_rango(fecha1, fecha2)]
        return max(valores) if valores else None

    def min_valor_rango(self, fecha1, fecha2):
        """Devuelve la temperatura mínima en el rango de fechas."""
        valores = [temp for _, temp in self.obtener_rango(fecha1, fecha2)]
        return min(valores) if valores else None
 