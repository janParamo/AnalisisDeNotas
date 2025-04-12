from analisis import calcularEstadisticas, generarInforme
import pandas as pd
import os

def gestionarEstudiantes():
    """
    Permite ingresar, editar, eliminar y recuperar estudiantes con sus notas.
    Carga datos existentes desde un archivo Excel al iniciar.
    """
    estudiantes = {}
    estudiantes_eliminados = {}
    id_actual = 1
    archivo_excel = "notas_estudiantes.xlsx"

    # Cargar datos existentes desde el archivo Excel
    if os.path.exists(archivo_excel):
        try:
            datos = pd.read_excel(archivo_excel)
            for _, fila in datos.iterrows():
                estudiantes[id_actual] = {"Nombre": fila["Nombre"], "Nota": fila["Nota"]}
                id_actual += 1
            print(f"Se cargaron {len(estudiantes)} estudiantes desde el archivo '{archivo_excel}'.")
        except Exception as e:
            print(f"Error al cargar datos desde el archivo Excel: {e}")

    while True:
        print("\nGestión de Estudiantes")
        print("1. Agregar estudiantes")
        print("2. Editar estudiante")
        print("3. Eliminar estudiante")
        print("4. Mostrar estudiantes")
        print("5. Ver informe")
        print("6. Recuperar estudiante eliminado")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if len(estudiantes) >= 10:
                print("No se pueden agregar más de 10 estudiantes.")
                continue

            while True:
                try:
                    cantidad = int(input("¿Cuántos estudiantes desea ingresar? (Máximo 10): "))
                    if 1 <= cantidad <= 10 - len(estudiantes):
                        break
                    else:
                        print(f"Debe ingresar un número entre 1 y {10 - len(estudiantes)}.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")

            for _ in range(cantidad):
                while True:
                    nombre = input("Ingrese el nombre del estudiante: ")
                    if any(char.isdigit() for char in nombre):
                        print("El nombre no puede contener números. Intente de nuevo.")
                    elif nombre in [est["Nombre"] for est in estudiantes.values()]:
                        print("El nombre ya existe. Intente con otro nombre.")
                    elif not nombre.strip():
                        print("El nombre no puede estar vacío. Intente de nuevo.")
                    else:
                        break

                while True:
                    try:
                        nota = float(input("Ingrese la nota del estudiante (0-100): "))
                        if 0 <= nota <= 100:
                            break
                        else:
                            print("La nota debe estar entre 0 y 100.")
                    except ValueError:
                        print("Por favor, ingrese un número válido para la nota.")

                estudiantes[id_actual] = {"Nombre": nombre, "Nota": nota}
                print(f"Estudiante agregado con ID: {id_actual}")
                id_actual += 1

        elif opcion == "2":
            try:
                id_editar = int(input("Ingrese el ID del estudiante a editar: "))
                if id_editar in estudiantes:
                    print(f"Estudiante seleccionado: {estudiantes[id_editar]}")
                    while True:
                        nuevo_nombre = input("Ingrese el nuevo nombre (deje en blanco para no cambiar): ")
                        if not nuevo_nombre.strip():
                            break
                        elif any(char.isdigit() for char in nuevo_nombre):
                            print("El nombre no puede contener números. Intente de nuevo.")
                        elif nuevo_nombre in [est["Nombre"] for est in estudiantes.values()]:
                            print("El nombre ya existe. Intente con otro nombre.")
                        else:
                            estudiantes[id_editar]["Nombre"] = nuevo_nombre
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
                if id_eliminar in estudiantes:
                    estudiantes_eliminados[id_eliminar] = estudiantes.pop(id_eliminar)
                    print("Estudiante eliminado y almacenado en la lista de eliminados.")
                else:
                    print("ID no encontrado.")
            except ValueError:
                print("Por favor, ingrese un ID válido.")

        elif opcion == "4":
            if estudiantes:
                print("\nLista de estudiantes:")
                for id_estudiante, datos in estudiantes.items():
                    print(f"ID: {id_estudiante}, Nombre: {datos['Nombre']}, Nota: {datos['Nota']}")
            else:
                print("No hay estudiantes registrados.")

        elif opcion == "5":
            if estudiantes:
                # Convertir los datos a un DataFrame y generar el informe
                datos = pd.DataFrame.from_dict(estudiantes, orient="index")
                estadisticas = calcularEstadisticas(datos)
                generarInforme(estadisticas)
            else:
                print("No hay estudiantes registrados para generar un informe.")

        elif opcion == "6":
            try:
                id_recuperar = int(input("Ingrese el ID del estudiante a recuperar: "))
                if id_recuperar in estudiantes_eliminados:
                    estudiantes[id_recuperar] = estudiantes_eliminados.pop(id_recuperar)
                    print("Estudiante recuperado exitosamente.")
                else:
                    print("ID no encontrado en la lista de eliminados.")
            except ValueError:
                print("Por favor, ingrese un ID válido.")

        elif opcion == "7":
            print("Saliendo de la gestión de estudiantes.")
            # Guardar los datos actualizados en el archivo Excel
            try:
                datos = pd.DataFrame.from_dict(estudiantes, orient="index")
                datos.to_excel(archivo_excel, index=False)
                print(f"Datos guardados exitosamente en '{archivo_excel}'.")
            except Exception as e:
                print(f"Error al guardar los datos en el archivo Excel: {e}")
            return estudiantes

        else:
            print("Opción no válida. Intente de nuevo.")