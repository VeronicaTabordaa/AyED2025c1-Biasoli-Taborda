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

    print("Temperatura el 02/06:", db.devolver_temperatura("02/06/2024"))
    print("Cambio de temperatura del 02/06 a 27.3:", db.guardar_temperatura(27.3, "02/06/2024"))
    print("Temperatura máxima entre 01 y 10:", db.temperatura_maxima_rango("01/06/2024", "10/06/2024"))
    print("Temperatura mínima entre 01 y 10:", db.temperatura_minima_rango("01/06/2024", "10/06/2024"))
    print("Todas las muestras:", db.devolver_temperaturas_rango("01/06/2024", "10/06/2024"))
    print("Temperatura del 03/06:", db.devolver_temperatura("03/06/2024"))
    print("Elimino temperatura del 03/06")
    db.eliminar_temperatura("03/06/2024")
    print("Temperaturas después de eliminar el 03/06:", db.devolver_temperaturas_rango("01/06/2024", "10/06/2024"))
    print("Cantidad de muestras luego de eliminar:", db.cantidad_muestras())
    print("Datos extremos entre 01/06 y 06/06:", db.extremos_temperatura_rango("01/06/2024", "06/06/2024"))
    print("Rango sin datos del 11 al 15/06:", db.devolver_temperaturas_rango("11/06/2024", "15/06/2024"))
    print("Temperatura del 05/06 antes de cambio:", db.devolver_temperatura("05/06/2024"))

    # Prueba con temperatura inválida
    try:
        db.guardar_temperatura("calor", "05/06/2024")
    except Exception as e:
        print("❌ Error esperado al guardar una temperatura inválida:", e)

    print("Temperatura del 05/06 después de intento fallido:", db.devolver_temperatura("05/06/2024"))

    print("\n✔ Todas las pruebas completadas correctamente.")

if __name__ == "__main__":
    pruebas()