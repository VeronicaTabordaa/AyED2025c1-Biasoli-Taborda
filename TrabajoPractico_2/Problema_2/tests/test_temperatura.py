from modules.temperatura_db import Temperaturas_DB
def pruebas():
    db = Temperaturas_DB()
    db.guardar_temperatura(22.5, "01/06/2024")
    db.guardar_temperatura(25.0, "02/06/2024")
    db.guardar_temperatura(20.3, "03/06/2024")
    db.guardar_temperatura(19.8, "04/06/2024")
    db.guardar_temperatura(21.2, "05/06/2024")
    db.guardar_temperatura(23.7, "06/06/2024")
    db.guardar_temperatura(18.9, "07/06/2024")
    db.guardar_temperatura(24.4, "08/06/2024")
    db.guardar_temperatura(26.0, "09/06/2024")
    db.guardar_temperatura(22.0, "10/06/2024")

    print("Temp el 02/06:", db.devolver_temperatura("02/06/2024"))
    print("Cambio de temperatura del 02/06 a 27.3:", db.guardar_temperatura(27.3, "02/06/2024"))
    print("Temp máx entre 01 y 04:", db.temperatura_maxima_rango("01/06/2024", "10/06/2024"))
    print("Temp mín entre 01 y 04:", db.temperatura_minima_rango("01/06/2024", "10/06/2024"))
    print("Todas las muestras:", db.devolver_temperaturas_rango("01/06/2024", "10/06/2024"))
    print("Temperattura del 03/06:", db.devolver_temperatura("03/06/2024"))
    print("Elimino temperatura del 03/06:", db.eliminar_temperatura("03/06/2024"))
    print("Temperaturas después de eliminar el 03/06:", db.devolver_temperaturas_rango("01/06/2024", "10/06/2024"))
    print("Cantidad de muestras luego de eliminar:", db.cantidad_muestras())
    rango_vacio = db.devolver_temperaturas_rango("11/06/2024", "15/06/2024")
    print("Rango sin datos del 10 al 12/06:", rango_vacio)
    print("Temperatura del 05/06 antes de cambio:", db.devolver_temperatura("05/06/2024"))
    print("cambio de temperatura del 05/06 a calor:", db.guardar_temperatura("calor", "05/06/2024"))
    print("Temperatura del 05/06 después de cambio:", db.devolver_temperatura("05/06/2024"))


print("\n✔ Todas las pruebas pasaron.")
if __name__ == "__main__":
    pruebas()

