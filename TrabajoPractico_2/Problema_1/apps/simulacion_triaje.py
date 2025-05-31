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
    PQ.push(Paciente("Maria", 2), 2)
    PQ.push(Paciente("Sofía", 1), 1)
    PQ.push(Paciente("Pedro", 1), 1) 
    PQ.push(Paciente("Mateo", 3), 3)
    PQ.push(Paciente("Valentina", 2), 2)
    PQ.push(Paciente("Diego", 1), 1)
    PQ.push(Paciente("Lucía", 3), 3)
    PQ.push(Paciente("Santiago", 2), 2)
    PQ.push(Paciente("Camila", 1), 1)
    PQ.push(Paciente("Nicolás", 3), 3)
    PQ.push(Paciente("Julieta", 2), 2)
    PQ.push(Paciente("Benjamín", 1), 1)   

    while not PQ.is_empty():
        paciente = PQ.pop()
        print("Atendiendo a:", paciente)

if __name__ == "__main__":
    Simular_paciente()
