import pandas as pd

def calcularEstadisticas(datos):
    """
    Calcula las estadísticas requeridas a partir del DataFrame.
    """
    total_estudiantes = len(datos)
    aprobados = datos[datos["Nota"] >= 70]
    reprobados = datos[datos["Nota"] < 70]
    reprobados_60_69 = datos[(datos["Nota"] >= 60) & (datos["Nota"] < 70)]
    
    porcentaje_aprobados = (len(aprobados) / total_estudiantes) * 100
    porcentaje_reprobados = (len(reprobados) / total_estudiantes) * 100
    porcentaje_reprobados_60_69 = (len(reprobados_60_69) / total_estudiantes) * 100
    
    media_notas = datos["Nota"].mean()
    desviacion_estandar = datos["Nota"].std()
    
    return {
        "total_estudiantes": total_estudiantes,
        "aprobados": len(aprobados),
        "porcentaje_aprobados": porcentaje_aprobados,
        "reprobados": len(reprobados),
        "porcentaje_reprobados": porcentaje_reprobados,
        "reprobados_60_69": len(reprobados_60_69),
        "porcentaje_reprobados_60_69": porcentaje_reprobados_60_69,
        "media_notas": media_notas,
        "desviacion_estandar": desviacion_estandar
    }

def generarInforme(estadisticas):
    """
    Genera un informe con las estadísticas calculadas y lo muestra en la consola.
    """
    print("Informe de Análisis de Notas")
    print(f"Número total de estudiantes: {estadisticas['total_estudiantes']}")
    print(f"Estudiantes aprobados: {estadisticas['aprobados']} ({estadisticas['porcentaje_aprobados']:.2f}%)")
    print(f"Estudiantes reprobados: {estadisticas['reprobados']} ({estadisticas['porcentaje_reprobados']:.2f}%)")
    print(f"Estudiantes reprobados (60-69): {estadisticas['reprobados_60_69']} ({estadisticas['porcentaje_reprobados_60_69']:.2f}%)")
    print(f"Media de las notas: {estadisticas['media_notas']:.2f}")
    print(f"Desviación estándar de las notas: {estadisticas['desviacion_estandar']:.2f}")

def exportarExcel(datos, nombre_archivo="notas_estudiantes.xlsx"):
    """
    Exporta un DataFrame a un archivo Excel.
    """
    try:
        datos.to_excel(nombre_archivo, index=False)
        print(f"Datos exportados exitosamente a '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error al exportar los datos a Excel: {e}")