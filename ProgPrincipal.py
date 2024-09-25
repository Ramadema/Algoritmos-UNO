# Programa de sistemas de reserva de Vuelos

import random 
import os
import re


# Funciones 
def menuInicial():
    """Funcion que permite seleccionar una opcion de accion de sesion de usuario."""
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


def menuVuelos():
    """Funcion que permite seleccionar una opcion de accion relacionada a los vuelos segun el usuario ingresado."""
    ok=True
    while ok:
        print("\nMenu principal de selección Vuelos")
        print("1. Busqueda de Vuelos")
        print("2. Reserva de vuelos")
        print("3. Historial de Vuelos")
        print("4. Cancelar reservas")
        print("5. Cerrar Sesión")
    
        opcion = int(input("\nSeleccionar una opción: "))
        
        if opcion >= 1 and opcion < 6:
           ok=False
           return opcion

    return -1


def generarVuelos(matriz):
    """La funcion permite generar una cantidad establecida de vuelos entre paises de sudamerica y america del norte o combinacion de ambas. Recibe la matriz de vuelos"""
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
    """Funcion que permite la prueba rapida de matriz y datos"""
    ancho_pais = 20
    ancho_capital = 20
    
    print("\n")
    print('-'*87)
    print("\t    Ubicacion de Origen\t\t\t        Ubicacion de Llegada")
    print('-'*87)
    
    imprimir_vuelo = lambda vuelo: print(f"{vuelo[0]:<{ancho_pais}},{vuelo[1]:<{ancho_capital}}-->   {vuelo[2]:<{ancho_pais}},{vuelo[3]:<{ancho_capital}}")

    for vuelo in matriz:
        # Llamada a la función lambda
        imprimir_vuelo(vuelo)  
        print('-' * (ancho_pais + ancho_capital + ancho_pais + ancho_capital + 7))


#Usuario
def registrarUsuario(lista_usuarios, diccionario_usuarios): 
    """Funcion que permite a nuevos usuarios crear una cuenta en el sistema de reservas. Recibe la lista de usuarios existente"""
    os.system('cls' if os.name == 'nt' else 'clear')
    nuevo_usuario = int(input("Ingrese un pin de 4 dígitos que lo identificará como nuevo usuario: \n"))
    bandera = True

    while bandera:
        if nuevo_usuario < 1000 or nuevo_usuario > 9999 or nuevo_usuario in lista_usuarios:
            print("Número de usuario inválido o ya existente\n")
            nuevo_usuario = int(input("Ingrese un pin de 4 dígitos que lo identificará como nuevo usuario: \n"))
        else:
            lista_usuarios.append(nuevo_usuario)
            print("Usuario registrado\n")
            bandera = False

    while True:
        nueva_contraseña = input("Ingrese una contraseña de al menos 8 caracteres con al menos un número, una letra minúscula y una letra mayúscula: \n")
        
        # Expresión regular para validar la contraseña
        patron = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$')
        
        if patron.match(nueva_contraseña):
            print("Nueva contraseña registrada\n")
            break
        else:
            print("Contraseña inválida. Debe tener al menos 8 caracteres, un número, una letra minúscula y una letra mayúscula.\n")

    diccionario_usuarios[nuevo_usuario] = nueva_contraseña

    print(diccionario_usuarios)
    # os.system('cls' if os.name == 'nt' else 'clear')
    return lista_usuarios

def iniciarSesion(lista_usuarios, diccionario_usuarios, Vexit): 
    """Funcion que permite a los usuarios existentes iniciar sesión en el sistema para acceder a sus reservas y realizar nuevas transacciones."""
    usuario_actual = 0
    iniciarSesion = int(input("Ingrese su número de usuario: \n"))
    bandera = True

    while bandera:
        if iniciarSesion not in diccionario_usuarios:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Usuario no existente\n")
            Vexit += 1
            
            iniciarSesion = int(input("Ingrese su número de usuario: \n"))
            if Vexit == 3:
                Vexit = 1
                print("Demasiados intentos fallidos.")
                bandera = False
        else:
            # Solicitar la contraseña
            contrasena = input("Ingrese su contraseña: \n")
            if diccionario_usuarios[iniciarSesion] == contrasena:
                print("\nLogin exitoso")
                Vexit = 0
                usuario_actual = iniciarSesion
                bandera = False``
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Contraseña incorrecta\n")
                Vexit += 1

                if Vexit == 3:
                    Vexit = 1
                    print("Demasiados intentos fallidos.")
                    bandera = False

    return Vexit, usuario_actual


def cerrarSesion(lista_usuarios): 
    """Funcion que cierra la sesión del usuario actual, asegurando que la información personal y las reservas estén protegidas. Recibe lista de usuarios existente"""
    cerrarUsuario=int(input("Ingrese su pin para cerrar la sesión. Los cambios serán guardados automaticamente. \n"))
    bandera=True

    while bandera:
        if cerrarUsuario not in lista_usuarios:
            print("Usuario no existente\n")
            cerrarUsuario=int(input("Ingrese su número de usuario para cerrar la sesión: \n"))
        else:  
             print("Sesión cerrada.")
             bandera=False 


def cancelarReserva(lista_usuarios, reservas, usuario_actual):
    """Función que permite al usuario cancelar una reserva existente, gestionando el reembolso o cambios según las políticas del sistema. Recibe lista de usuarios y lista de reservas existentes."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Validacion de existencia de usuario
    # Función lambda para validar la existencia del usuario
    # validar_usuario = lambda usuario: usuario in lista_usuarios

    # usuario = int(input("Ingrese su número de usuario: \n"))
    # while not validar_usuario(usuario):
    #     print("Usuario no existente\n")
    #     usuario = int(input("Ingrese su número de usuario: \n"))

    print("\nReservas del usuario:")
    reservas_usuario = [reserva for reserva in reservas if reserva[0] == usuario_actual]

    if not reservas_usuario:
        print("No tiene reservas para cancelar.\n")
        return

    for i, reserva in enumerate(reservas_usuario):
        vuelo = reserva[1]
        print(f"{i + 1}. Origen: {vuelo[0]}, {vuelo[1]} -> Destino: {vuelo[2]}, {vuelo[3]}")

    # Función lambda para validar la selección de reserva
    validar_seleccion = lambda seleccion: 1 <= seleccion <= len(reservas_usuario)

    seleccion = int(input("\nSeleccione el número de la reserva que desea cancelar: \n"))
    while not validar_seleccion(seleccion):
        print("Selección de reserva inválida\n")
        seleccion = int(input("Seleccione el número de la reserva que desea cancelar: \n"))

    reserva_seleccionada = reservas_usuario[seleccion - 1]
    reservas.remove(reserva_seleccionada)

    print(f"\nReserva cancelada con éxito. Vuelo cancelado: Origen: {reserva_seleccionada[1][1]}, {reserva_seleccionada[1][0]} -> Destino: {reserva_seleccionada[1][3]}, {reserva_seleccionada[1][2]}\n")


# Consultas Vuelos
def consultarStatusDeVuelo(vuelo_seleccionado):
    """Funcion que proporciona información actualizada sobre el estado de un vuelo, como retrasos o cambios en la programación. Recibe el vuelo que quedo seleccionado en el sector de pagos"""
    estados = ["A tiempo", "Retrasado", "Cancelado", "Reprogramado"]
    estado_vuelo = random.choice(estados)
    
    print(f"Estado del vuelo seleccionado: Origen: {vuelo_seleccionado[0]}, {vuelo_seleccionado[1]} -> Destino: {vuelo_seleccionado[2]}, {vuelo_seleccionado[3]}")
    print(f"Estado actual del vuelo: {estado_vuelo}\n")


def pagarReserva():
    """Esta funcion gestiona el proceso de pago para completar una reserva, incluyendo la elección del método de pago y la confirmación de la transacción."""
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


def historialReservas(reservas, lista_usuarios, usuario_actual):
    """Esta funcion muestra un historial de reservas realizadas por el usuario, incluyendo reservas anteriores y pagos.(antiguas y actuales) Recibe reservas actuales"""
    os.system('cls' if os.name=='nt' else 'clear')
    bandera = True

    # Validacion de existencia de usuario
    # usuario = int(input("Ingrese su número de usuario: \n"))
    # while bandera:
    #     if usuario not in lista_usuarios:
    #         print("Usuario no existente\n")
    #         usuario = int(input("Ingrese su número de usuario: \n"))
    #     else:
    #         bandera = False

    print("\nHistorial de reservas del usuario:")
    reservas_usuario = [reserva for reserva in reservas if reserva[0] == usuario_actual]

    if not reservas_usuario:
        print("No tiene reservas registradas.\n")
        return

    for i, reserva in enumerate(reservas_usuario):
        vuelo = reserva[1]
        print('-' * 80)
        print(f"{i+1}. | Origen: {vuelo[0]}, {vuelo[1]} -> Destino: {vuelo[2]}, {vuelo[3]}")
    print('-' * 80) 


def hacerReservaDeVuelos(vuelos,lista_usuarios, reservas, usuario_actual):
    """Esta funcion Facilita la reserva de un vuelo seleccionado, solicitando la información del usuario y confirmando la reserva. Recibe la matriz de Vuelos, la lista de usuarios existentes y las reservas actuales"""
    os.system('cls' if os.name=='nt' else 'clear')

    bandera = True
    ancho_pais = 20
    ancho_capital = 20
    
    # Validacion de existencia de usuario
    # usuario = int(input("Ingrese su número de usuario: \n"))
    # while bandera:
    #     if usuario not in lista_usuarios:
    #         print("Usuario no existente\n")
    #         usuario = int(input("Ingrese su número de usuario: \n"))
    #     else:
    #         print("Usuario válido\n")
    #         bandera = False

    # Muestreo de prueba
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
        reservas.append((usuario_actual, vuelo_seleccionado))
        print("\nReserva realizada con ÉXITO\n")
        print(f"Vuelo reservado: Origen: {vuelo_seleccionado[0]}, {vuelo_seleccionado[1]} -> Destino: {vuelo_seleccionado[2]}, {vuelo_seleccionado[3]}\n")
        
        #print(f"PRUEBA matriz muetro vuelo seleccionado {vuelo_seleccionado}/n")
        #consultarStatusDeVuelo(vuelo_seleccionado) --> PROXIMO ENTREGABLE: funcion consultar status 
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
diccionario_usuarios = {0000:"admin"}

salir = True
salir2 = True

vuelos = generarVuelos(matrizPaisesCapitales)
while salir:
    seleccion = menuInicial()

    if seleccion == 1:
        lista_usuarios = registrarUsuario(lista_usuarios, diccionario_usuarios)

    elif seleccion == 2:
        Vexit=0
        os.system('cls' if os.name == 'nt' else 'clear')
        Vexit, usuario_actual = iniciarSesion(lista_usuarios,diccionario_usuarios, Vexit)

        # Prueba - Chequeo de usuarios activos 
        #print("Prueba Lista Usuarios existentes: ",lista_usuarios)
        print("Prueba Lista Usuarios existentes: ",lista_usuarios)
        print("Prueba Diccionario Usuarios existentes: ",diccionario_usuarios)


        salir2 = True

        while salir2:
            
            if Vexit==1:
                Vexit=0
                seleccion=5
            else:
                seleccion = menuVuelos()

            if seleccion == 1:
                # Buscar vuelos               
                imprimirMatrizOrdenada(vuelos)
            elif seleccion == 2:
                # Hacer reserva y pagar
                hacerReservaDeVuelos(vuelos, lista_usuarios, reservas, usuario_actual)
            elif seleccion == 3:
                # Historial de reservas
                historialReservas(reservas, lista_usuarios, usuario_actual)  
            elif seleccion == 4:
                # Cancelar reservas
                cancelarReserva(lista_usuarios, reservas, usuario_actual)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n   ¡¡¡¡Gracias por utilizar nuestro Sistema de Vuelos!!!!")
                print("\n\t\t***** ADIOS *****\n")
                salir2 = False
    else:
        print("\n   ¡¡¡¡Gracias por utilizar nuestro Sistema de Vuelos!!!!")
        print("\n\t\t***** ADIOS *****\n")
        salir = False