def crearAvion(filas, columnas):
    asientos = [['O' for _ in range(columnas)] for _ in range(filas)]
    return asientos

def mostrarAvion(asientos):
    print("       ________")
    print("      /        \\")
    print("     /          \\")
    print("    /            \\")
    print("   | A B C  D E F |")
    print("   |              |")

    for i, fila in enumerate(asientos):
        # el zfill para mantener la estructura de dos digitos de butacas un 0 si es necesario
        id_formateado = str(i + 1).zfill(2)  
        fila1 = fila[0]+fila[1]+fila[2]
        fila2 = fila[3]+fila[4]+fila[5]
        # con el join uno todos los elementos de la lista en una sola cadena, utilizando el separador " "
        print(f"{id_formateado} | {' '.join(fila1)}  {' '.join(fila2)} |")

    print("    \\            /")
    print("     \\__________/")
    print("\n")

def seleccionarAsiento(asientos):
    bandera = True
    # Mapeo de letras a índices
    columnas_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5} 

    while bandera:
        seleccion = input("Selecciona un asiento (ej. 1A) o '-1' para salir: ").strip().upper()
        print(seleccion)
        if seleccion == "-1":
            bandera = False
            
        else:
            try:
                # se onvierte la parte numérica de la selección a un índice de fila.
                fila = int(seleccion[:-1]) - 1
                # se obtiene la letra de la columna.
                letra_columna = seleccion[-1]
                # El get traduce la letra de columna a un índice.
                columna = columnas_map.get(letra_columna)

                if fila < 0 or fila >= len(asientos) or columna is None or columna < 0 or columna >= len(asientos[0]):
                    print("Asiento no válido, intenta de nuevo.")
                    continue
                
                if asientos[fila][columna] == 'X':
                    mostrarAvion(asientos)
                    print("Asiento ya ocupado, elige otro.")
                else:
                    asientos[fila][columna] = 'X'
                    mostrarAvion(asientos)
                    print(f"Asiento {seleccion} reservado con éxito.")

            except ValueError:
                print("Entrada no válida, intenta de nuevo.")
                

# Configuración del avión
filas = 20  
columnas = 6  

asientos = crearAvion(filas, columnas)
bandera = True

# prog principal
while bandera:
    print("\n" + "-" * 40)
    print("   Airbus 737 - Selección de Asientos")
    print("-" * 40)
    mostrarAvion(asientos)
    seleccionarAsiento(asientos)
    print("-" * 40 + "\n")

    bandera = False