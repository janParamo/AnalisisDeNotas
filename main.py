import pandas as pd  # Para manejar datos en forma de DataFrame
import os  # Para manejar rutas y verificar la existencia del archivo
from gestionarEstudiantes import gestionarEstudiantes # Importar la función gestionarEstudiantes
from analisis import calcularEstadisticas, generarInforme, exportarExcel # Importar funciones de análisis

def importar_datos(ruta_archivo = "notas_estudiantes.xlsx"): 
    """
    Importa los datos desde un archivo Excel y los almacena en un DataFrame.
    """
    if not os.path.exists(ruta_archivo = "notas_estudiantes.xlsx"):# Verifica si el archivo existe
        # Si el archivo no existe, se crea un DataFrame vacío
        print(f"Error: El archivo '{ruta_archivo}' no se encontró en el directorio actual.") #Mensaje de error
        return None # Retorna None si el archivo no existe
    try: # Intenta leer el archivo Excel
        datos = pd.read_excel(ruta_archivo = "notas_estudiantes.xlsx")
        #Lee el archivo Excel y lo almacena en un DataFrame
        return datos # Retorna el DataFrame con los datos
    except Exception as e: # Captura cualquier excepción que ocurra al leer el archivo
        print(f"Error al leer el archivo: {e}")
        return None

def main():
    """
    Función principal que ejecuta el programa.
    """
    print("Bienvenido al programa de análisis de notas.")
    estudiantes = gestionarEstudiantes() 
    # Llama a la función gestionarEstudiantes para manejar la entrada de datos

    if estudiantes:
        # Convertir los datos a un DataFrame para el análisis
        datos = pd.DataFrame.from_dict(estudiantes, orient="index")
        estadisticas = calcularEstadisticas(datos) 
        # Estadisticas recibe el valor de la función calcularEstadisticas
        generarInforme(estadisticas)# Genera un informe con las estadísticas calculadas

        # Exportar los datos a un archivo Excel
        exportarExcel(datos)
    else:
        print("No se ingresaron estudiantes. Finalizando el programa.")

if __name__ == "__main__": #Si el script se ejecuta directamente, llama a la función main
    main()
    