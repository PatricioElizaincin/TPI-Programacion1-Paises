import csv


# CARGAR CSV

def cargar_paises():
    paises = []
    try:
        
        with open("paises.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }
                    paises.append(pais)
                except ValueError:
                    print(f"Error de formato numérico en el país: {fila['nombre']}")
    except FileNotFoundError:
        print("No se encontró el archivo 'paises.csv'. Se iniciará con una lista vacía.")
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
        
    return paises

# -------------------------
# GUARDAR CSV (Para mantener los cambios al salir)

def guardar_paises(paises):
    if len(paises) == 0:
        return
    
    try:
        with open("paises.csv", "w", encoding="utf-8", newline='') as archivo:
            nombres_columnas = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=nombres_columnas)
            
            escritor.writeheader()
            for pais in paises:
                escritor.writerow(pais)
        print("Datos guardados exitosamente en paises.csv")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")


# AGREGAR
# -------------------------
def agregar_pais(paises):
    nombre = input("Nombre: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío")
        return

    try:
        poblacion = int(input("Población: "))
        superficie = int(input("Superficie: "))
    except ValueError:
        print("Error: Debe ingresar números enteros para población y superficie.")
        return

    continente = input("Continente: ").strip()
    if continente == "":
        print("El continente no puede estar vacío")
        return

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(pais)
    print("País agregado correctamente")


# ACTUALIZAR
# -------------------------
def actualizar_pais(paises):
    nombre = input("Ingrese el país a actualizar: ").lower().strip()

    for pais in paises:
        if pais["nombre"].lower() == nombre:
            try:
                pais["poblacion"] = int(input("Nueva población: "))
                pais["superficie"] = int(input("Nueva superficie: "))
            except ValueError:
                print("Error: Los datos ingresados deben ser números enteros.")
                return

            print("País actualizado correctamente")
            return

    print("País no encontrado")


# BUSCAR
# -------------------------
def buscar_pais(paises):
    texto = input("Nombre a buscar: ").lower().strip()
    encontrado = False

    for pais in paises:
        if texto in pais["nombre"].lower():
            print("--------------------")
            print("Nombre:", pais["nombre"])
            print("Población:", pais["poblacion"])
            print("Superficie:", pais["superficie"])
            print("Continente:", pais["continente"])
            encontrado = True

    if not encontrado:
        print("No se encontraron resultados")

# FILTRAR
# -------------------------
def filtrar_paises(paises):
    print("Función en desarrollo por mi compañero...")

# ORDENAR
# -------------------------
def ordenar_paises(paises):
    print("Función en desarrollo por mi compañero...")

# ESTADÍSTICAS
# -------------------------
def estadisticas(paises):
    print("Función en desarrollo por mi compañero...")


# -------------------------
# PROGRAMA PRINCIPAL
# -------------------------
paises = cargar_paises()

while True:
    print("\n----- MENÚ PRINCIPAL ------")
    print("1 - Agregar país")
    print("2 - Actualizar país")
    print("3 - Buscar país")
    print("4 - Filtrar países")
    print("5 - Ordenar países")
    print("6 - Estadísticas")
    print("7 - Salir y Guardar")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_pais(paises)
    elif opcion == "2":
        actualizar_pais(paises)
    elif opcion == "3":
        buscar_pais(paises)
    elif opcion == "4":
        filtrar_paises(paises)
    elif opcion == "5":
        ordenar_paises(paises)
    elif opcion == "6":
        estadisticas(paises)
    elif opcion == "7":
        guardar_paises(paises) 
        print("Programa finalizado.7")
        break
    else:
        print("Opción inválida. Intente nuevamente.")