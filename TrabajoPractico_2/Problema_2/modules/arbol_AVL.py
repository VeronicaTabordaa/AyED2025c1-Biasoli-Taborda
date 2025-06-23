from modules.nodo_AVL import NodoAVL

class ArbolAVL:
    def __init__(self):
        self.raiz = None
        self._cantidad = 0

    def cantidad_nodos(self):
        """Devuelve la cantidad total de nodos en el árbol."""
        return self._cantidad
    
    def insertar(self, fecha, temperatura):
        """Inserta una nueva medición de temperatura o actualiza una existente."""
        self.raiz = self._insertar(self.raiz, fecha, temperatura)
        if self.raiz:
            self.raiz.padre = None  # Asegura que la raíz no tenga padre

    def _insertar(self, nodo, fecha, temperatura):
        if nodo is None:
            self._cantidad += 1
            return NodoAVL(fecha, temperatura)
        if fecha == nodo.fecha:
            nodo.temperatura = temperatura
        elif fecha < nodo.fecha:
            nodo.hijo_izq = self._insertar(nodo.hijo_izq, fecha, temperatura)
            nodo.hijo_izq.padre = nodo
        else:
            nodo.hijo_der = self._insertar(nodo.hijo_der, fecha, temperatura)
            nodo.hijo_der.padre = nodo

        self._actualizar_altura(nodo)
        return self._balancear(nodo)

    def eliminar(self, fecha):
        """Elimina la medición de temperatura asociada a una fecha."""
        self.raiz = self._eliminar(self.raiz, fecha)
        if self.raiz:
            self.raiz.padre = None

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

        self._actualizar_altura(nodo)
        return self._balancear(nodo)
    
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
        
    def obtener_rango(self, fecha1, fecha2):
        """Devuelve una lista ordenada de tuplas (fecha, temperatura) entre dos fechas dadas."""
        resultados = []
        self._enorden_rango(self.raiz, fecha1, fecha2, resultados)
        return resultados

    def _enorden_rango(self, nodo, fecha1, fecha2, resultados):
        if nodo is None:
            return
        if fecha1 <= nodo.fecha:
            self._enorden_rango(nodo.hijo_izq, fecha1, fecha2, resultados)
        if fecha1 <= nodo.fecha <= fecha2:
            resultados.append((nodo.fecha, nodo.temperatura))
        if nodo.fecha <= fecha2:
            self._enorden_rango(nodo.hijo_der, fecha1, fecha2, resultados)

    def max_valor_rango(self, fecha1, fecha2):
        """Devuelve la temperatura máxima en el rango de fechas."""
        valores = [temp for _, temp in self.obtener_rango(fecha1, fecha2)]
        return max(valores) if valores else None

    def min_valor_rango(self, fecha1, fecha2):
        """Devuelve la temperatura mínima en el rango de fechas."""
        valores = [temp for _, temp in self.obtener_rango(fecha1, fecha2)]
        return min(valores) if valores else None

    def _minimo_nodo(self, nodo):
        while nodo.hijo_izq:
            nodo = nodo.hijo_izq
        return nodo
    
    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    def _actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self._altura(nodo.hijo_izq), self._altura(nodo.hijo_der)) 

    def _factor_balance(self, nodo):
        return self._altura(nodo.hijo_izq) - self._altura(nodo.hijo_der) if nodo else 0

    def _balancear(self, nodo):
        balance = self._factor_balance(nodo)
        if balance > 1:
            if self._factor_balance(nodo.hijo_izq) < 0:
                nodo.hijo_izq = self._rotar_izquierda(nodo.hijo_izq)
            return self._rotar_derecha(nodo)
        if balance < -1:
            if self._factor_balance(nodo.hijo_der) > 0:
                nodo.hijo_der = self._rotar_derecha(nodo.hijo_der)
            return self._rotar_izquierda(nodo)
        return nodo
    
    def _rotar_derecha(self,y):
        x = y.hijo_izq
        T2 = x.hijo_der
        x.padre = y.padre # El padre de y se convierte en el padre de x
        if y.padre:
            if y.padre.hijo_izq == y:
                y.padre.hijo_izq = x
            else:
                y.padre.hijo_der = x
        y.padre = x # x se convierte en el padre de y
        if T2:
            T2.padre = y # y se convierte en el padre de T2
        x.hijo_der = y
        y.hijo_izq = T2
        self._actualizar_altura(y)
        self._actualizar_altura(x)
        return x

    def _rotar_izquierda(self, x):
        y = x.hijo_der
        T2 = y.hijo_izq
        y.padre = x.padre # El padre de x se convierte en el padre de y
        if x.padre:
            if x.padre.hijo_izq == x:
                x.padre.hijo_izq = y
            else:
                x.padre.hijo_der = y    
        x.padre = y # y se convierte en el padre de x
        if T2:
            T2.padre = x # x se convierte en el padre de T2
        y.hijo_izq = x
        x.hijo_der = T2
        self._actualizar_altura(x)
        self._actualizar_altura(y)
        return y