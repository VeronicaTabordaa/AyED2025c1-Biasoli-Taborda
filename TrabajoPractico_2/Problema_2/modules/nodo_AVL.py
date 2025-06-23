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