class Vertice:
    def __init__(self, nombre):
        self.id = nombre
        self.conectadoA = {}  
        self.distancia = 0
        self.siguiente = []
        self.predecesor = None

    def agregarVecino(self, vecino, peso=0):
        self.conectadoA[vecino] = peso

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self, vecino):
        return self.conectadoA[vecino]

    def asignarDistancia(self, nueva_distancia):
        self.distancia = nueva_distancia

    def obtenerDistancia(self):
        return self.distancia

    def asignarPredecesor(self, predecesor):
        self.predecesor = predecesor

    def obtenerPredecesor(self):
        return self.predecesor

    def asignarSiguiente(self, siguiente):
        self.siguiente.append(siguiente)

    def obtenerSiguiente(self):
        return self.siguiente

    def __str__(self):
        return f'{self.id} conectado a {[v.id for v in self.conectadoA]}'

    def __lt__(self, otro):
        return self.distancia < otro.distancia  # útil para comparación en heaps

