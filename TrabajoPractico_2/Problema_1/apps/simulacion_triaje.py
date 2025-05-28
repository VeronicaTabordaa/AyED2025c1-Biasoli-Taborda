from modules import Prioridad_Queue

class Paciente:
    def __init__(self, nombre, riesgo):
        self.nombre = nombre
        self.riesgo = riesgo

    def __repr__(self):
        return f"Paciente(nombre={self.nombre}, riesgo={self.riesgo})"
    
def Simular_paciente():
    PQ = Prioridad_Queue.PrioridadQueue()
    PQ.push(Paciente("Juan", 2), 2)
    PQ.push(Paciente("Ana", 1), 1)
    PQ.push(Paciente("Luis", 3), 3)

    while not PQ.is_empty():
        paciente = PQ.pop()
        print("Atendiendo a:", paciente)