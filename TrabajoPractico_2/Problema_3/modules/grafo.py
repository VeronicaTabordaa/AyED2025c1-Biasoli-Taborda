from modules.vertice import Vertice

class Grafo:
    def __init__(self):
        self.Vertices = {}
        self.totalVertices = 0

    def agregarVertice(self, nombre):
        self.totalVertices += 1
        vertice = Vertice(nombre)
        self.Vertices[nombre] = vertice
        return vertice
    
    def obtenerVertice(self, nombre):
        return self.Vertices.get(nombre)

    def __contains__(self, nombre):
        return nombre in self.Vertices

    def agregarArista(self, origen, destino, costo=0):
        if origen not in self.Vertices:
            self.agregarVertice(origen)
        if destino not in self.Vertices:
            self.agregarVertice(destino)

        self.Vertices[origen].agregarVecino(self.Vertices[destino], costo)
        self.Vertices[destino].agregarVecino(self.Vertices[origen], costo)  # grafo no dirigido


    def obtenerVertices(self):
        return self.Vertices.keys()

    def __iter__(self):
        return iter(self.Vertices.values())

    def __getitem__(self, nombre):
        return self.Vertices.get(nombre)
