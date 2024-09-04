# Programa de sistemas de reserva de Vuelos

import random 

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

# Generar pares de vuelos entre países y capitales
def generarVuelos(matriz):
    vuelos = []
    
    for i in range(len(matriz)):
        random.shuffle(matriz)
        for j in range(i + 1, len(matriz)):
            # Se limita a 10 para realizar prueba
            if len(vuelos)<10:
                random.shuffle(matriz)
                origen_pais, origen_capital = matriz[i]
                destino_pais, destino_capital = matriz[j]
                vuelos.append((origen_pais, origen_capital, destino_pais, destino_capital))
    return vuelos

def imprimirMatrizOrdenada(matriz):
    for fila in matriz:
        print(fila)

#Usuario
def registrarUsuario(): 
#--> juan "Funcion que permite a nuevos usuarios crear una cuenta en el sistema de reservas."
    lista_usuarios=[]
    
    nuevo_usuario=int(input("Ingrese un pin de 4 digitos que lo identificará como nuevo usuario: \n"))
    bandera=True

    while bandera:
        if nuevo_usuario<999 or nuevo_usuario>10000 or nuevo_usuario in lista_usuarios:
            print("Número de usuario invalido o ya existente\n")
            nuevo_usuario=int(input("Ingrese un pin de 4 digitos que lo identificará como nuevo usuario: \n"))
        else:
            lista_usuarios.append(nuevo_usuario)
            bandera=False
            
    return lista_usuarios


def iniciarSesion(lista_usuarios): 
#--> juan "Funcion que permite a los usuarios existentes iniciar sesión en el sistema para acceder a sus reservas y realizar nuevas transacciones."
    iniciarSesion=int(input("Ingrese su número de usuario: \n"))
    bandera=True

    while bandera:
        if iniciarSesion not in lista_usuarios:
            print("Usuario no existente\n")
            iniciarSesion=int(input("Ingrese su número de usuario: \n"))
        else:  
             print("Login exitoso")
             bandera=False  

def cerrarSesion(lista_usuarios): 
#--> juan "Funcion que cierra la sesión del usuario actual, asegurando que la información personal y las reservas estén protegidas."
    cerrarUsuario=int(input("Ingrese su pin para cerrar la sesión. Los cambios serán guardados automaticamente. \n"))
    bandera=True

    while bandera:
        if cerrarUsuario not in lista_usuarios:
            print("Usuario no existente\n")
            cerrarUsuario=int(input("Ingrese su número de usuario para cerrar la sesión: \n"))
        else:  
             print("Sesión cerrada.")
             bandera=False 

# Hacer reserva de vuelos
def hacerReservaDeVuelos(vuelos, lista_usuarios, reservas):
    usuario = int(input("Ingrese su número de usuario: \n"))
    bandera = True
    
    while bandera:
        if usuario not in lista_usuarios:
            print("Usuario no existente\n")
            usuario = int(input("Ingrese su número de usuario: \n"))
        else:
            print("Usuario válido\n")
            bandera = False

    print("\nLista de vuelos disponibles:")
    for i, vuelo in enumerate(vuelos):
        print(f"{i+1}. Origen: {vuelo[1]}, {vuelo[0]} -> Destino: {vuelo[3]}, {vuelo[2]}")

    seleccion = int(input("\nSeleccione el número del vuelo que desea reservar: \n"))
    bandera = True

    while bandera:
        if seleccion < 1 or seleccion > len(vuelos):
            print("Selección de vuelo inválida\n")
            seleccion = int(input("Seleccione el número del vuelo que desea reservar: \n"))
        else:
            vuelo_seleccionado = vuelos[seleccion-1]
            bandera = False

    reservas.append((usuario, vuelo_seleccionado))
    print(f"\nReserva realizada con éxito. Vuelo reservado: Origen: {vuelo_seleccionado[1]}, {vuelo_seleccionado[0]} -> Destino: {vuelo_seleccionado[3]}, {vuelo_seleccionado[2]}\n")

    consultarStatusDeVuelo(vuelo_seleccionado)


# Cancelar reserva
def cancelarReserva(lista_usuarios, reservas):
    usuario = int(input("Ingrese su número de usuario: \n"))
    bandera = True

    while bandera:
        if usuario not in lista_usuarios:
            print("Usuario no existente\n")
            usuario = int(input("Ingrese su número de usuario: \n"))
        else:
            bandera = False

    print("\nReservas del usuario:")
    reservas_usuario = [reserva for reserva in reservas if reserva[0] == usuario]

    if not reservas_usuario:
        print("No tiene reservas para cancelar.\n")
        return

    for i, reserva in enumerate(reservas_usuario):
        vuelo = reserva[1]
        print(f"{i+1}. Origen: {vuelo[1]}, {vuelo[0]} -> Destino: {vuelo[3]}, {vuelo[2]}")

    seleccion = int(input("\nSeleccione el número de la reserva que desea cancelar: \n"))
    bandera = True

    while bandera:
        if seleccion < 1 or seleccion > len(reservas_usuario):
            print("Selección de reserva inválida\n")
            seleccion = int(input("Seleccione el número de la reserva que desea cancelar: \n"))
        else:
            reserva_seleccionada = reservas_usuario[seleccion-1]
            reservas.remove(reserva_seleccionada)
            bandera = False

    print(f"\nReserva cancelada con éxito. Vuelo cancelado: Origen: {reserva_seleccionada[1][1]}, {reserva_seleccionada[1][0]} -> Destino: {reserva_seleccionada[1][3]}, {reserva_seleccionada[1][2]}\n")


# Consultar status de vuelo
def consultarStatusDeVuelo(vuelo_seleccionado):
    estados = ["A tiempo", "Retrasado", "Cancelado", "Reprogramado"]
    estado_vuelo = random.choice(estados)
    
    print(f"Estado del vuelo seleccionado: Origen: {vuelo_seleccionado[1]}, {vuelo_seleccionado[0]} -> Destino: {vuelo_seleccionado[3]}, {vuelo_seleccionado[2]}")
    print(f"Estado actual del vuelo: {estado_vuelo}\n")

# Programa Principal


# Paises unicamente de america del norte y sur
matrizPaisesCapitales = [
    ["Canadá", "Ottawa"],
    ["Estados Unidos", "Washington, D.C."],
    ["México", "Ciudad de México"],
    ["Guatemala", "Ciudad de Guatemala"],
    ["Belice", "Belmopán"],
    ["Honduras", "Tegucigalpa"],
    ["El Salvador", "San Salvador"],
    ["Nicaragua", "Managua"],
    ["Costa Rica", "San José"],
    ["Panamá", "Ciudad de Panamá"],
    ["Argentina", "Buenos Aires"],
    ["Bolivia", "La Paz"],
    ["Brasil", "Brasília"],
    ["Chile", "Santiago"],
    ["Colombia", "Bogotá"],
    ["Ecuador", "Quito"],
    ["Paraguay", "Asunción"],
    ["Perú", "Lima"],
    ["Uruguay", "Montevideo"],
    ["Venezuela", "Caracas"]
]

# Menu de interaccion
salir = True
while salir:
    seleccion = menuInicial()

    if seleccion == 1:
        pass
        # menu_1()
    elif seleccion == 2:
        # Obtener la lista de vuelos
        vuelos = generarVuelos(matrizPaisesCapitales)

        imprimirMatrizOrdenada(vuelos)
       
        # menu_2()
    elif seleccion == 3:
        pass
        # menu_3()
    else:
        print("\n   ¡¡¡¡Gracias por utilizar nuestro Sistema de Vuelos!!!!")
        print("\n\t\t***** ADIOS *****\n")
        salir=False



