from analisis import calcularEstadisticas, generarInforme # Importar funciones de analisis.py
import pandas as pd # Importar pandas para manejar Excel
import os # Importar os para verificar la existencia del archivo

def gestionarEstudiantes():
    """
    Permite ingresar, editar, eliminar y recuperar estudiantes con sus notas.
    Carga datos existentes desde un archivo Excel al iniciar.
    """
    estudiantes = {} # Diccionario para almacenar estudiantes
    estudiantes_eliminados = {} # Diccionario para almacenar estudiantes eliminados
    id_actual = 1 # ID inicial para estudiantes
    archivo_excel = "notas_estudiantes.xlsx" # Nombre del archivo Excel

    # Cargar datos existentes desde el archivo Excel
    if os.path.exists(archivo_excel):
        try:
            datos = pd.read_excel(archivo_excel) # Lee los datos si existen en el archivo
            for _, fila in datos.iterrows(): # Itera sobre cada fila del DataFrame
                # Almacena en el diccionario
                estudiantes[id_actual] = {"Nombre": fila["Nombre"], "Nota": fila["Nota"]} 
                id_actual += 1 # Incrementa el ID para el siguiente estudiante
            print(f"Se cargaron {len(estudiantes)} estudiantes desde el archivo '{archivo_excel}'.")
        except Exception as e:
            print(f"Error al cargar datos desde el archivo Excel: {e}")

    while True: # Menu principal
        print("\nGestión de Estudiantes")
        print("1. Agregar estudiantes")
        print("2. Editar estudiante")
        print("3. Eliminar estudiante")
        print("4. Mostrar estudiantes")
        print("5. Ver informe")
        print("6. Recuperar estudiante eliminado")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        # Se manejan las limitantes para cada opcion
        if opcion == "1":
            if len(estudiantes) >= 10:
                """Se limita a 10 estudiantes con el objetivo de que el usuario no ingrese 
                una gran cantidad"""
                print("No se pueden agregar más de 10 estudiantes.")
                continue

            while True:
                try:
                    cantidad = int(input("¿Cuántos estudiantes desea ingresar? (Máximo 10): "))
                    if 1 <= cantidad <= 10 - len(estudiantes):# Se verifica que la cantidad no exceda el límite
                        break
                    else:
                        print(f"Debe ingresar un número entre 1 y {10 - len(estudiantes)}.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")

            for _ in range(cantidad): # Se itera por la cantidad de estudiantes a agregar
                while True:
                    nombre = input("Ingrese el nombre del estudiante: ")
                    if any(char.isdigit() for char in nombre): # Se verifica que no contenga números
                        print("El nombre no puede contener números. Intente de nuevo.") # Se manda mensaje de advertencia
                    elif nombre in [est["Nombre"] for est in estudiantes.values()]:# Se verifica que no exista el nombre
                        print("El nombre ya existe. Intente con otro nombre.")
                    elif not nombre.strip():# Se verifica que no esté vacío
                        print("El nombre no puede estar vacío. Intente de nuevo.")
                    else:
                        break

                while True:
                    try:
                        nota = float(input("Ingrese la nota del estudiante (0-100): "))
                        if 0 <= nota <= 100:# Se verifica que la nota esté en el rango permitido
                            break
                        else:
                            print("La nota debe estar entre 0 y 100.")
                    except ValueError:
                        print("Por favor, ingrese un número válido para la nota.")

                estudiantes[id_actual] = {"Nombre": nombre, "Nota": nota} # Se agrega el estudiante al diccionario
                print(f"Estudiante agregado con ID: {id_actual}") # Se muestra el ID del estudiante
                id_actual += 1 # Se incrementa el ID para el siguiente estudiante

        elif opcion == "2":
            try:
                id_editar = int(input("Ingrese el ID del estudiante a editar: ")) # Se solicita el ID del estudiante a editar
                if id_editar in estudiantes: # Se verifica que el ID exista
                    print(f"Estudiante seleccionado: {estudiantes[id_editar]}")
                    while True:
                        nuevo_nombre = input("Ingrese el nuevo nombre (deje en blanco para no cambiar): ")
                        if not nuevo_nombre.strip():# Se verifica que no esté vacío
                            break
                        elif any(char.isdigit() for char in nuevo_nombre):# Se verifica que no contenga números
                            print("El nombre no puede contener números. Intente de nuevo.")
                        elif nuevo_nombre in [est["Nombre"] for est in estudiantes.values()]:# Se verifica que no exista el nombre
                            print("El nombre ya existe. Intente con otro nombre.")
                        else:
                            estudiantes[id_editar]["Nombre"] = nuevo_nombre # Se actualiza el nombre
                            break

                    while True:
                        try:
                            nueva_nota = input("Ingrese la nueva nota (deje en blanco para no cambiar): ")
                            if not nueva_nota.strip():
                                break
                            nueva_nota = float(nueva_nota)
                            if 0 <= nueva_nota <= 100:
                                estudiantes[id_editar]["Nota"] = nueva_nota
                                break
                            else:
                                print("La nota debe estar entre 0 y 100.")
                        except ValueError:
                            print("Por favor, ingrese un número válido para la nota.")
                    print("Estudiante actualizado.")
                else:
                    print("ID no encontrado.")
            except ValueError:
                print("Por favor, ingrese un ID válido.")

        elif opcion == "3":
            try:
                id_eliminar = int(input("Ingrese el ID del estudiante a eliminar: "))
                if id_eliminar in estudiantes:# Se verifica que el ID exista
                    estudiantes_eliminados[id_eliminar] = estudiantes.pop(id_eliminar)
                    # pop elimina el estudiante del diccionario y lo almacena en la lista de eliminados
                    print("Estudiante eliminado y almacenado en la lista de eliminados.")
                else:
                    print("ID no encontrado.")
            except ValueError:
                print("Por favor, ingrese un ID válido.")

        elif opcion == "4":
            if estudiantes:
                print("\nLista de estudiantes:")
                for id_estudiante, datos in estudiantes.items():
                    # Se itera sobre los estudiantes, items() devuelve una lista 
                    print(f"ID: {id_estudiante}, Nombre: {datos['Nombre']}, Nota: {datos['Nota']}")
            else:
                print("No hay estudiantes registrados.")

        elif opcion == "5":
            if estudiantes:
                # Convertir los datos a un DataFrame y generar el informe
                datos = pd.DataFrame.from_dict(estudiantes, orient="index") # Se convierte el diccionario a DataFrame
                estadisticas = calcularEstadisticas(datos)
                generarInforme(estadisticas)
            else:
                print("No hay estudiantes registrados para generar un informe.")

        elif opcion == "6":
            try:
                id_recuperar = int(input("Ingrese el ID del estudiante a recuperar: "))
                if id_recuperar in estudiantes_eliminados:# Se verifica que el ID exista en la lista de eliminados
                    estudiantes[id_recuperar] = estudiantes_eliminados.pop(id_recuperar)# Se recupera el estudiante
                    # Se elimina de la lista de eliminados y se agrega al diccionario de estudiantes
                    print("Estudiante recuperado exitosamente.")
                else:
                    print("ID no encontrado en la lista de eliminados.")
            except ValueError:
                print("Por favor, ingrese un ID válido.")

        elif opcion == "7":
            print("Saliendo de la gestión de estudiantes.")
            # Guardar los datos actualizados en el archivo Excel
            try:
                datos = pd.DataFrame.from_dict(estudiantes, orient="index")# Se convierte el diccionario a DataFrame
                datos.to_excel(archivo_excel, index=False)# Se guarda el DataFrame en el archivo Excel
                print(f"Datos guardados exitosamente en '{archivo_excel}'.")
            except Exception as e:
                print(f"Error al guardar los datos en el archivo Excel: {e}")
            return estudiantes

        else:
            print("Opción no válida. Intente de nuevo.")