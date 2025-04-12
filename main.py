import pandas as pd  # Para manejar datos en forma de DataFrame
import os  # Para manejar rutas y verificar la existencia del archivo
from gestionarEstudiantes import gestionarEstudiantes
from analisis import calcularEstadisticas, generarInforme, exportarExcel

def importar_datos(ruta_archivo = "notas_estudiantes.xlsx"):
    """
    Importa los datos desde un archivo Excel y los almacena en un DataFrame.
    """
    if not os.path.exists(ruta_archivo = "notas_estudiantes.xlsx"):
        print(f"Error: El archivo '{ruta_archivo}' no se encontró en el directorio actual.")
        return None

    try:
        datos = pd.read_excel(ruta_archivo = "notas_estudiantes.xlsx")
        return datos
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def main():
    """
    Función principal que ejecuta el programa.
    """
    print("Bienvenido al programa de análisis de notas.")
    estudiantes = gestionarEstudiantes()

    if estudiantes:
        # Convertir los datos a un DataFrame para el análisis
        datos = pd.DataFrame.from_dict(estudiantes, orient="index")
        estadisticas = calcularEstadisticas(datos)
        generarInforme(estadisticas)

        # Exportar los datos a un archivo Excel
        exportarExcel(datos)
    else:
        print("No se ingresaron estudiantes. Finalizando el programa.")

if __name__ == "__main__":
    main()
    