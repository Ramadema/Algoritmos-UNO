def pagarReserva():
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
        return pagarReserva()
    
# Codigo de Login de usuarios con listas 
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
