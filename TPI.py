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
    print("\n--- FILTRAR POR ---")
    print("1 - Continente")
    print("2 - Población")
    print("3 - Superficie")
    
    opcion = input("Opción: ")

    if opcion == "1":
        continente = input("Continente: ").lower().strip()
        for pais in paises:
            if pais["continente"].lower() == continente:
                print(f"{pais['nombre']} - Pob: {pais['poblacion']} - Sup: {pais['superficie']}")

    elif opcion == "2":
        try:
            minimo = int(input("Población mínima: "))
            maximo = int(input("Población máxima: "))
            for pais in paises:
                if pais["poblacion"] >= minimo and pais["poblacion"] <= maximo:
                    print(f"{pais['nombre']} - Pob: {pais['poblacion']}")
        except ValueError:
            print("Error: Ingrese valores numéricos.")

    elif opcion == "3":
        try:
            minimo = int(input("Superficie mínima: "))
            maximo = int(input("Superficie máxima: "))
            for pais in paises:
                if pais["superficie"] >= minimo and pais["superficie"] <= maximo:
                    print(f"{pais['nombre']} - Sup: {pais['superficie']}")
        except ValueError:
            print("Error: Ingrese valores numéricos.")
    else:
        print("Opción inválida")


# ORDENAR
# -------------------------
def ordenar_paises(paises):
    print("\n--- CRITERIO DE ORDENAMIENTO ---")
    print("1 - Nombre")
    print("2 - Población")
    print("3 - Superficie")
    opcion = input("Opción: ")
    
    if opcion not in ["1", "2", "3"]:
        print("Opción inválida")
        return

    print("\n--- DIRECCIÓN ---")
    print("1 - Ascendente (Menor a Mayor / A-Z)")
    print("2 - Descendente (Mayor a Menor / Z-A)")
    direccion = input("Opción: ")

    if direccion not in ["1", "2"]:
        print("Opción inválida")
        return


    for i in range(len(paises)):
        for j in range(i + 1, len(paises)):
            intercambiar = False

            if opcion == "1":
                if direccion == "1" and paises[i]["nombre"] > paises[j]["nombre"]:
                    intercambiar = True
                elif direccion == "2" and paises[i]["nombre"] < paises[j]["nombre"]:
                    intercambiar = True
            
            elif opcion == "2":
                if direccion == "1" and paises[i]["poblacion"] > paises[j]["poblacion"]:
                    intercambiar = True
                elif direccion == "2" and paises[i]["poblacion"] < paises[j]["poblacion"]:
                    intercambiar = True
            
            elif opcion == "3":
                if direccion == "1" and paises[i]["superficie"] > paises[j]["superficie"]:
                    intercambiar = True
                elif direccion == "2" and paises[i]["superficie"] < paises[j]["superficie"]:
                    intercambiar = True

            # Si se cumple la condición, intercambiamos las posiciones
            if intercambiar:
                aux = paises[i]
                paises[i] = paises[j]
                paises[j] = aux

    print("\nLista ordenada:")
    for pais in paises:
        print(f"Nombre: {pais['nombre']}, Pob: {pais['poblacion']}, Sup: {pais['superficie']}")


# ESTADÍSTICAS
# -------------------------
def estadisticas(paises):
    if len(paises) == 0:
        print("No hay datos para calcular estadísticas")
        return

    mayor = paises[0]
    menor = paises[0]
    suma_poblacion = 0
    suma_superficie = 0
    continentes = {}

    for pais in paises:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        cont = pais["continente"]
        if cont in continentes:
            continentes[cont] += 1
        else:
            continentes[cont] = 1

    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    print("\n--- ESTADÍSTICAS ---")
    print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"País con menor población: {menor['nombre']} ({menor['poblacion']})")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f}")
    
    print("\nCantidad de países por continente:")
    for cont in continentes:
        print(f"{cont}: {continentes[cont]}")


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