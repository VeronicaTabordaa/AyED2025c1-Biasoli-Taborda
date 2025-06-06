class NodoAVL:
    def __init__(self, fecha, temperatura=None, izquierda=None, derecha=None, padre=None):
        self.__fecha = fecha
        self.__temperatura = temperatura
        self.__hijo_izq = izquierda
        self.__hijo_der = derecha
        self.__padre = padre
        self.__altura = 1

    @property
    def fecha(self):
        return self.__fecha 
    
    @fecha.setter
    def fecha(self, valor):
        self.__fecha = valor
    
    @property
    def temperatura(self):
        return self.__temperatura   
    
    @temperatura.setter
    def temperatura(self, valor):
        self.__temperatura = valor
    
    @property
    def altura(self):
        return self.__altura        

    @altura.setter
    def altura(self, valor):
        self.__altura = valor
   
    @property
    def hijo_izq(self):
        return self.__hijo_izq
    
    @hijo_izq.setter
    def hijo_izq(self, valor):
        self.__hijo_izq = valor

    @property
    def hijo_der(self):
        return self.__hijo_der
    
    @hijo_der.setter
    def hijo_der(self, valor):
        self.__hijo_der = valor

    @property
    def padre(self):
        return self.__padre
    
    @padre.setter
    def padre(self, valor):
        self.__padre = valor
    
   
def altura(nodo):
    return nodo.altura if nodo else 0

def actualizar_altura(nodo):
    nodo.altura = 1 + max(altura(nodo.hijo_izq), altura(nodo.hijo_der)) 

def factor_balance(nodo):
    return altura(nodo.hijo_izq) - altura(nodo.hijo_der) if nodo else 0

def rotar_derecha(y):
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
    actualizar_altura(y)
    actualizar_altura(x)
    return x

def rotar_izquierda(x):
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
    actualizar_altura(x)
    actualizar_altura(y)
    return y
