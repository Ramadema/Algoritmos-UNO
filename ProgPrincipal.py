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



