"""
Datos de Entrada:
•	Un archivo Excel (notas_estudiantes.xlsx) con dos columnas: 
o	"Nombre del estudiante" (texto)
o	"Nota" (número entero)

Requisitos del Programa:

1.	Importación de Datos:
o	Utilizar biblioteca para leer el archivo Excel y almacenar los datos en un DataFrame.

2.	Análisis Estadístico:
o	Calcular el número total de estudiantes.
o	Determinar el número y porcentaje de estudiantes aprobados (nota >= 70).
o	Determinar el número y porcentaje de estudiantes reprobados (nota < 70).
o	Determinar el número y porcentaje de estudiantes reprobados con notas entre 60 y 69.
o	Determinar la media de las notas.
o	Determinar la desviación estandar de las notas.

3.	Generación de Informe:
o	Mostrar los resultados de manera clara y concisa en la consola.
o	El informe debe incluir: 
	Número total de estudiantes.
	Número y porcentaje de estudiantes aprobados.
	Número y porcentaje de estudiantes reprobados.
	Número y porcentaje de estudiantes reprobados entre 60 y 69.
	La media de las notas.
	La desviación estandar de las notas.

Estructuras de Datos y Algoritmos:
•	Utilizar DataFrames para almacenar y manipular los datos.
•	Implementar funciones para realizar los cálculos estadísticos.

Requisitos Adicionales:
•	El código debe estar bien documentado con comentarios explicativos.
•	Se deben manejar posibles errores, como archivos no encontrados o datos inválidos.
•	El código debe ser lo más eficiente posible.

Ejemplo de Salida:
Informe de Análisis de Notas
Número total de estudiantes: 25
Estudiantes aprobados: 15 (60.00%)
Estudiantes reprobados: 10 (40.00%)
Estudiantes reprobados (60-69): 3 (12.00%)
Media de las notas: 75.5
Desviación estandar de las notas: 12.34

Recomendaciones:
•	Dividir el programa en funciones para mejorar la organización y la legibilidad.
•	Utilizar formatos de cadena para presentar los resultados con la precisión adecuada.
•	Agregar validaciones para que el código sea robusto.

* Se elimina un estudiante agregar opcion para recuperarlo

"""