# Programa de sistemas de reserva de Vuelos

# Funciones 
def menuInicial():
    ok=True
    while ok:
        print("\nMenu principal de selección")
        print("1. Busqueda de Vuelos")
        print("2. Reservar vuelos")
        print("3. Historial de reservas")
        print("4. Salir\n")
    
        opcion = int(input("Seleccionar una opción: "))
        
        if opcion >= 1 and opcion < 5:
           ok=False
           return opcion

    return -1


# Programa Principal
#Menu de interaccion
salir = True
while salir:
    seleccion = menuInicial()

    if seleccion == 1:
        pass
        # menu_1()
    elif seleccion == 2:
        pass
        # menu_2()
    elif seleccion == 3:
        pass
        # menu_3()
    else:
        print("\n   ¡¡¡¡Gracias por utilizar nuestro Sistema de Vuelos!!!!")
        print("\n\t\t***** ADIOS *****\n")
        salir=False