# Programa de sistemas de reserva de Vuelos

import random 
import os


# Funciones 

#--> Rama "Funcion que permite seleccionar una opcion de accion."
def menuInicial():
    ok=True
    while ok:
        print("\nMenu principal de selección")
        print("1. Registro de Usuario")
        print("2. Iniciar Sesión")
        print("3. Salir\n")
    
        opcion = int(input("Seleccionar una opción: "))
        
        if opcion >= 1 and opcion < 4:
           ok=False
           return opcion

    return -1


#--> Rama "Funcion que permite seleccionar una opcion de accion relacionada a los vuelos segun el usuario ingresado."
def menuVuelos():
    ok=True
    while ok:
        print("\nMenu principal de selección Vuelos")
        print("1. Busqueda de Vuelos")
        print("2. Reserva de vuelos")
        print("3. Historial de Vuelos")
        print("4. Cerrar Sesión")
    
        opcion = int(input("\nSeleccionar una opción: "))
        
        if opcion >= 1 and opcion < 5:
           ok=False
           return opcion

    return -1


#--> Rama "La funcion permite generar una cantidad establecida de vuelos entre paises de sudamerica y america del norte o combinacion de ambas.
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

    # print(vuelos)
    return vuelos

#--> Rama "Funcion que permite la prueba rapida de matriz y datos"
def imprimirMatrizOrdenada(matriz):
    ancho_pais = 20
    ancho_capital = 20
    
    print("\n")
    print('-'*87)
    print("\t    Ubicacion de Origen\t\t\t        Ubicacion de Llegada")
    print('-'*87)
    

    for vuelo in matriz:
        origen_pais, origen_capital, destino_pais, destino_capital = vuelo
        print(f"{origen_pais:<{ancho_pais}},{origen_capital:<{ancho_capital}}-->   {destino_pais:<{ancho_pais}},{destino_capital:<{ancho_capital}}")
        print('-' * (ancho_pais + ancho_capital + ancho_pais + ancho_capital + 7))  # Línea divisoria


#Usuario
def registrarUsuario(lista_usuarios): 
#--> juan "Funcion que permite a nuevos usuarios crear una cuenta en el sistema de reservas."
    os.system('clear')
    nuevo_usuario=int(input("Ingrese un pin de 4 digitos que lo identificará como nuevo usuario: \n"))
    bandera=True

    while bandera:
        if nuevo_usuario<999 or nuevo_usuario>10000 or nuevo_usuario in lista_usuarios:
            print("Número de usuario invalido o ya existente\n")
            nuevo_usuario=int(input("Ingrese un pin de 4 digitos que lo identificará como nuevo usuario: \n"))
        else:
            lista_usuarios.append(nuevo_usuario)
            print("Usuario registrado\n")
            bandera=False

    nueva_contraseña=str(input("Ingrese una contraseña de 8 digitos: \n"))

    caracteres= True

    while caracteres:
        if len(nueva_contraseña)<8:
            print("Contraseña inválida\n")
            nueva_contraseña=str(input("Ingrese una contraseña de 8 digitos: \n"))
        else:
            print("Nueva contraseña registrada\n")
            caracteres=False

    os.system('cls' if os.name=='nt' else 'clear')
    return lista_usuarios


def iniciarSesion(lista_usuarios): 
#--> juan "Funcion que permite a los usuarios existentes iniciar sesión en el sistema para acceder a sus reservas y realizar nuevas transacciones."
    iniciarSesion=int(input("Ingrese su número de usuario: \n"))
    bandera=True

    while bandera:
        if iniciarSesion not in lista_usuarios:
            os.system('clear')
            print("Usuario no existente\n")
            iniciarSesion=int(input("Ingrese su número de usuario: \n"))
        else:  
             print("\nLogin exitoso")

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

#--> Rama "Esta funcion gestiona el proceso de pago para completar una reserva, incluyendo la elección del método de pago y la confirmación de la transacción"
def pagarReserva():
    # Creo diccionario que contenga las opciones de pago
    metodos_pago = {
        1: "Tarjeta de crédito",
        2: "Tarjeta de débito",
        3: "QR Mercado Pago"
    }
    print("\nProceso de pago iniciado.")
    print("Opciones de método de pago:")
    for clave, valor in metodos_pago.items():
        print(f"{clave}. {valor}")
    
    metodo_pago = int(input("Selecciona un método de pago: "))

    if metodo_pago in metodos_pago:
        print(f"Método de pago seleccionado: {metodos_pago[metodo_pago]}.")
    else:
        print("Método de pago inválido. Intenta de nuevo.")
        #Vuelvo a la funcion cuando el usuario ponga cualquier otro metodo de pago no existente
        return pagarReserva()

    #Utilizacion de procesamiento de pago aleatoreo
    print("Espere un momento, su pago se esta procesando...")
    transaccion_exitosa = random.choice([True, False, True, True])
    
    if transaccion_exitosa:
        print("\nPago completado con éxito.")
        return True
    else:
        print("\nError en la transacción. Vuelve a intentarlo.")
        return False

#--> Rama "Esta funcion muestra un historial de reservas realizadas por el usuario, incluyendo reservas anteriores y pagos.(antiguas y actuales)"
def historialReservas(reservas, lista_usuarios):
    os.system('cls' if os.name=='nt' else 'clear')
    usuario = int(input("Ingrese su número de usuario: \n"))
    bandera = True

    # Opcional pedir usuario "consultarlo"
    # while bandera:
    #     if usuario not in lista_usuarios:
    #         print("Usuario no existente\n")
    #         usuario = int(input("Ingrese su número de usuario: \n"))
    #     else:
    #         bandera = False

    print("\nHistorial de reservas del usuario:")
    reservas_usuario = [reserva for reserva in reservas if reserva[0] == usuario]

    if not reservas_usuario:
        print("No tiene reservas registradas.\n")
        return

    for i, reserva in enumerate(reservas_usuario):
        vuelo = reserva[1]
        print('-' * 80)
        print(f"{i+1}. | Origen: {vuelo[0]}, {vuelo[1]} -> Destino: {vuelo[2]}, {vuelo[3]}")
    print('-' * 80) 

#--> Rama modificacion y acople a codigo
def hacerReservaDeVuelos(vuelos, lista_usuarios, reservas):
    os.system('cls' if os.name=='nt' else 'clear')
    # Opcional pedir usuario "consultarlo"
    usuario = int(input("Ingrese su número de usuario: \n"))
    bandera = True
    ancho_pais = 20
    ancho_capital = 20
    
    # Opcional pedir usuario "consultarlo"
    while bandera:
        if usuario not in lista_usuarios:
            print("Usuario no existente\n")
            usuario = int(input("Ingrese su número de usuario: \n"))
        else:
            print("Usuario válido\n")
            bandera = False

    # print("\nLista de vuelos disponibles:\n")
    # for i, vuelo in enumerate(vuelos):
    #     print(f"{i+1}. Origen: {vuelo[1]}, {vuelo[0]} -> Destino: {vuelo[3]}, {vuelo[2]}")
    
    print("\nLista de vuelos disponibles:\n")
    print('-'*90)
    for i,vuelo in enumerate(vuelos):
        origen_pais, origen_capital, destino_pais, destino_capital = vuelo
        print(f"{i+1}. | {origen_pais:<{ancho_pais}},{origen_capital:<{ancho_capital}}-->   {destino_pais:<{ancho_pais}},{destino_capital:<{ancho_capital}}")
        print('-' * (ancho_pais + ancho_capital + ancho_pais + ancho_capital + 10))

    seleccion = int(input("\nSeleccione el número del vuelo que desea reservar: \n"))
    bandera = True

    while bandera:
        if seleccion < 1 or seleccion > len(vuelos):
            print("Selección de vuelo inválida\n")
            seleccion = int(input("Seleccione el número del vuelo que desea reservar: \n"))
        else:
            vuelo_seleccionado = vuelos[seleccion-1]
            bandera = False

    if pagarReserva():
        os.system('cls' if os.name=='nt' else 'clear')
        reservas.append((usuario, vuelo_seleccionado))
        print("\nReserva realizada con ÉXITO\n")
        print(f"Vuelo reservado: Origen: {vuelo_seleccionado[0]}, {vuelo_seleccionado[1]} -> Destino: {vuelo_seleccionado[2]}, {vuelo_seleccionado[3]}\n")
        consultarStatusDeVuelo(vuelo_seleccionado)
    else:
        print("ERROR. La reserva no se pudo completar debido a un problema con el pago.")
        

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
lista_usuarios = []
reservas = []

salir = True
salir2 = True

vuelos = generarVuelos(matrizPaisesCapitales)
while salir:
    seleccion = menuInicial()

    if seleccion == 1:
        lista_usuarios = registrarUsuario(lista_usuarios)

    elif seleccion == 2:
        os.system('clear')
        iniciarSesion(lista_usuarios)
        # Prueba - Chequeo de usuarios activos 
        print(lista_usuarios)

        salir2 = True

        while salir2:
            seleccion = menuVuelos()

            if seleccion == 1:
                # Buscar vuelos               
                imprimirMatrizOrdenada(vuelos)
            elif seleccion == 2:
                # Hacer reserva y pagar
                hacerReservaDeVuelos(vuelos, lista_usuarios, reservas)
            elif seleccion == 3:
                # Historial de reservas
                historialReservas(reservas, lista_usuarios)  # Aquí se llama a historialReservas
            else:
                os.system('clear')
                print("\n   ¡¡¡¡Gracias por utilizar nuestro Sistema de Vuelos!!!!")
                print("\n\t\t***** ADIOS *****\n")
                salir2 = False
    else:
        print("\n   ¡¡¡¡Gracias por utilizar nuestro Sistema de Vuelos!!!!")
        print("\n\t\t***** ADIOS *****\n")
        salir = False


# APUNTE: Logica para funcion de busqueda de vuelo, se podria crear una matriz con minimo y un maximo de registros (salida llegada),
# para luego filtrarla segun el pais de salida y el de llegada que desee el usuario, tamb pienso agregar horarios (con o sin biblio time)
# con esta tengo ligada las funciones hacer reserva, cancelar reserva e historial reserva