# Programa de sistemas de reserva de Vuelos
import time
import random 
import os
import json
import re
from datetime import datetime, timedelta
from Escalas import vuelos_escalas
from colorama import Fore, Back, Style, init

init(autoreset=True)


""" ********************** MENUES *********************"""

def menuInicial():
    """Funcion que permite seleccionar una opcion de accion de sesion de usuario."""
    ok = True
    while ok:
        print(Style.BRIGHT + Fore.CYAN + "*" * 45)
        print(Fore.CYAN + Style.BRIGHT + "*           ✈️  Sistema de Vuelos ✈️          *")
        print(Fore.CYAN + Style.BRIGHT + "*" * 45)
        print(Fore.CYAN + Style.BRIGHT + "*                                           *")
        print(Fore.CYAN + Style.BRIGHT + "*   1️⃣  Registro de Usuarios                 *")
        print(Fore.CYAN + Style.BRIGHT + "*   2️⃣  Iniciar Sesión                       *")
        print(Fore.CYAN + Style.BRIGHT + "*   3️⃣  Salir                                *")
        print(Fore.CYAN + Style.BRIGHT + "*                                           *")
        print(Style.BRIGHT + Fore.CYAN + "*" * 45)
        
        try:
            opcion = int(input("Seleccionar una opción: "))
            if opcion >= 1 and opcion < 4:
                ok = False
                return opcion
            else:
                print("Por favor, elige una opción válida (1-3).")
        except ValueError:
            print("Error: Debes ingresar un número.")

    return -1

def menuVuelos():
    """Funcion que permite seleccionar una opcion de accion relacionada a los vuelos segun el usuario ingresado."""
    ok=True
    while ok:
        print(Style.BRIGHT + Fore.CYAN + "*******************************************************")
        print(Style.BRIGHT + Fore.CYAN + "*       ✈️  Menú Principal de Selección Vuelos ✈️       *")
        print(Style.BRIGHT + Fore.CYAN + "*******************************************************")
        print(Style.BRIGHT + Fore.CYAN + "*                                                     *")
        print(Style.BRIGHT + Fore.CYAN + "*              1️⃣  Búsqueda de Vuelos                  *")
        print(Style.BRIGHT + Fore.CYAN + "*              2️⃣  Reserva de Vuelos                   *")
        print(Style.BRIGHT + Fore.CYAN + "*              3️⃣  Historial de Vuelos                 *")
        print(Style.BRIGHT + Fore.CYAN + "*              4️⃣  Vuelos con Escalas                  *")
        print(Style.BRIGHT + Fore.CYAN + "*              5️⃣  Cancelar Reservas                   *")
        print(Style.BRIGHT + Fore.CYAN + "*              6️⃣  Cerrar Sesión                       *")
        print(Style.BRIGHT + Fore.CYAN + "*                                                     *")
        print(Style.BRIGHT + Fore.CYAN + "*******************************************************")

        try:
            opcion = int(input("\nSeleccionar una opción: "))
            
            if opcion >= 1 and opcion < 7:
                ok = False
                return opcion
            else:
                print("Por favor, elige una opción válida (1-6)")
        except ValueError:
            print("Error: Debes ingresar un número.")

    return -1

""" ********************** GENERACION DE VUELOS Y ARCHIVOS *********************"""

# Funciones
def generar_fecha_hora():
    """Genera una fecha y hora aleatoria dentro de los próximos 30 días."""
    # Obtener la fecha actual
    fecha_actual = datetime.now()
    # Generar un número aleatorio de días y horas
    dias_adelante = random.randint(1, 30)
    horas = random.randint(0, 23)
    minutos = random.randint(0, 59)
    
    # Calcular la fecha y hora programada
    fecha_programada = fecha_actual + timedelta(days=dias_adelante, hours=horas, minutes=minutos)
    return fecha_programada.strftime("%Y-%m-%d"), fecha_programada.strftime("%H:%M")


def generarVuelos(matriz):
    """Genera una cantidad establecida de vuelos entre países de Sudamérica y América del Norte o combinación de ambas."""
    vuelosJson = []
    vuelos = []
    estados = ["A tiempo"] * 7 + ["Retrasado"] * 2 + ["Cancelado"]
    
    for i in range(len(matriz)):
        random.shuffle(matriz)
        for j in range(i + 1, len(matriz)):
            # Se limita a 50 vuelos para realizar prueba
            if len(vuelos) < 50:
                random.shuffle(matriz)
                origen_pais, origen_capital = matriz[i]
                destino_pais, destino_capital = matriz[j]
                fecha, hora = generar_fecha_hora()
                estado_vuelo = random.choice(estados)
                vuelos.append((origen_pais, origen_capital, destino_pais, destino_capital, fecha, hora, estado_vuelo))

                vuelosJson.append({
                    "origen_pais": origen_pais,
                    "origen_capital": origen_capital,
                    "destino_pais": destino_pais,
                    "destino_capital": destino_capital,
                    "fecha": fecha,
                    "hora": hora,
                    "estado_vuelo": estado_vuelo
                })

    guardarVuelosEnJson(vuelosJson,'vuelos.json')
    
    return vuelos



def guardarVuelosEnJson(vuelos, nombre_archivo):
    """Guarda la lista de vuelos en un archivo JSON dentro de la carpeta 'vuelos'."""
    os.makedirs('BDvuelos', exist_ok=True)
    
    # Ruta completa del archivo apuntando a la carpeta BDvuelos/vuelos.json
    ruta_archivo = os.path.join('BDvuelos', nombre_archivo)
    
    # se utiliza [encoding='utf-8'] y [ensure_ascii=False] para evitar que los caracteres especiales sean codificados en el archivo
    with open(ruta_archivo, 'wt', encoding='utf-8') as archivo_json:
        json.dump(vuelos, archivo_json, indent=4, ensure_ascii=False) 


def imprimirMatrizOrdenada(matriz):
    """Funcion que permite la prueba rápida de matriz y datos"""
    os.system('cls' if os.name == 'nt' else 'clear')
    ancho_pais = 20
    ancho_capital = 20
    
    print("\n")
    print('-' * 118)
    print("\t    Ubicación de Origen\t\t\t    Ubicación de Llegada\t\t          Fecha\t\tHora")
    print('-' * 118)
    
    imprimir_vuelo = lambda vuelo: print(f"{vuelo[0]:<{ancho_pais}},{vuelo[1]:<{ancho_capital}}-->   {vuelo[2]:<{ancho_pais}},{vuelo[3]:<{ancho_capital}}\t{vuelo[4]}\t{vuelo[5]}")
    
    for vuelo in matriz:
        imprimir_vuelo(vuelo)
        print('-' * 118)
    
    print('-' * (ancho_pais + ancho_capital + ancho_pais + ancho_capital + 38))
    


def ImprimirVuelosEscalas(vuelos_escalas):
    """Función que permite la prueba rápida de matriz y datos"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    ancho_pais = 20
    ancho_capital = 20

    print("\nEscalas disponibles:\n")
 
    print('-' * 130)
    print("\t    Ubicación de Origen\t\t\t    Ubicación de Llegada\t\t          Fecha\t\tHora")
    print('-' * 130)

    imprimir_vuelo = lambda vuelo: print(
        f"{vuelo['origen_pais']:<{ancho_pais}},{vuelo['origen_capital']:<{ancho_capital}} -->   "
        f"{vuelo['destino_pais']:<{ancho_pais}},{vuelo['destino_capital']:<{ancho_capital}}\t"
        f"{vuelo['fecha']}\t{vuelo['hora']}"
    )
    
    vuelo_num = 1


    for i in range(0, len(vuelos_escalas) - 1, 2):
        # Imprimir la etiqueta de vuelo con el número y los países
        print(f"\nVuelo {vuelo_num}   {vuelos_escalas[i]['origen_pais']}  ==>  {vuelos_escalas[i + 1]['destino_pais']}:")
        print('*' * 130)

        # Imprimir el primer vuelo
        imprimir_vuelo(vuelos_escalas[i])
        
        # Imprimir el segundo vuelo
        imprimir_vuelo(vuelos_escalas[i + 1])
        print('-' * 130)
        
        # Incrementar el número del vuelo
        vuelo_num += 1
    
    print("\n\n")


""" ********************** REGISTRO E INICIO DE SESION DE USUARIO ********************* """


def registrarUsuario(diccionario_usuarios, intentos): 
    """Funcion que permite a nuevos usuarios crear una cuenta en el sistema de reservas. Recibe la lista de usuarios existente"""
    ok=True
    bandera = True
    okey=True
    intentos=0
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    while ok:
        nombre_apellido=input("\nIngrese su nombre y apellido: \n")
        intentos+=1
        if all(('a' <= char <= 'z' or 'A' <= char <= 'Z' or char == ' ') for char in nombre_apellido):
            intentos=0
            ok=False
        else:
            print("\nError: Solo se permiten letras. Intenta nuevamente.")
            if intentos==4:
                intentos==1
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nDemasiados intentos fallidos. Vuelva a comenzar.\n\n")
                time.sleep(2)
                menuInicial()
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    while bandera:
        try:
            nuevo_usuario = int(input("\nIngrese un pin de 4 dígitos que lo identificará como nuevo usuario: \n"))
            intentos+=1
            if nuevo_usuario < 1000 or nuevo_usuario > 9999 or nuevo_usuario in diccionario_usuarios:
                print("\nNúmero de usuario inválido o ya existente\n")
                if intentos==4:
                    intentos==1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nDemasiados intentos fallidos. Vuelva a comenzar.\n\n")
                    time.sleep(2)
                    registrarUsuario(diccionario_usuarios, intentos)
            else:
                intentos=0
                bandera = False
        except ValueError:
            print("\nError: Debes ingresar solo números.")

    os.system('cls' if os.name == 'nt' else 'clear')

    while okey:
        nueva_contraseña = input("\nIngrese una contraseña de al menos 8 caracteres con al menos un número, una letra minúscula y una letra mayúscula: \n")
        intentos+=1
        # Expresión regular para validar la contraseña
        patron = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$')
        if patron.match(nueva_contraseña):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Style.BRIGHT + Fore.GREEN + "=" * 50)
            print(Fore.GREEN + Style.BRIGHT + "\n     ¡USUARIO REGISTRADO CON ÉXITO! 🎉 \n")
            print(Fore.GREEN + "=" * 50)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            intentos=0
            okey = False
        else:
            print("Contraseña inválida. Debe tener al menos:\n")
            print(". 8 caracteres\n. 1 letra mayúscula\n. 1 letra minúscula\n. 1 número")
            if intentos==4:
                intentos==1
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nDemasiados intentos fallidos. Vuelva a comenzar.\n\n")
                time.sleep(2)
                registrarUsuario(diccionario_usuarios, intentos)

    diccionario_usuarios[nuevo_usuario] = {
                                            'nombre_apellido': nombre_apellido,
                                            'contrasena': nueva_contraseña
                                            }

    return intentos

def iniciarSesion(diccionario_usuarios, intentos): 
    """Funcion que permite a los usuarios existentes iniciar sesión en el sistema para acceder a sus reservas y realizar nuevas transacciones."""
    usuario_actual = 0
    bandera = True
    ok = True
    intentos = 0

    os.system('cls' if os.name == 'nt' else 'clear')

    while bandera:
        try:
            inicioSesion = int(input("\nIngrese su número de usuario: \n"))
            if inicioSesion not in diccionario_usuarios:
                print("Usuario no existente\n")
                intentos += 1
                if intentos == 4:
                    intentos = 1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nDemasiados intentos fallidos. Vuelva a comenzar.\n\n")
                    time.sleep(2)
                    menuInicial()
            else:
                bandera=False
        except ValueError:
            print("\nError: Debes ingresar solo números.")

    os.system('cls' if os.name == 'nt' else 'clear')

    while ok:
        # Solicitar la contraseña
        contrasena = input("\nIngrese su contraseña: \n")
        if diccionario_usuarios[inicioSesion] ["contrasena"] == contrasena:
            os.system('cls' if os.name == 'nt' else 'clear')   
            print(Style.BRIGHT + Fore.GREEN + "=" * 40)
            print(Fore.GREEN + Style.BRIGHT + "        ¡LOGIN EXITOSO! 🎉")
            print(Fore.WHITE + "    Bienvenido al sistema, usuario.")
            print(Fore.GREEN + "=" * 40)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear') 
            intentos = 0
            usuario_actual = inicioSesion
            ok = False
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            # el abs unicamente me da el numero absuloto de intentos, el cual debe ser siempre positivo
            print(f"Contraseña incorrecta. Tiene {abs(intentos-3)} intentos para poder logearse. \n")
            intentos += 1
            if intentos == 4:
                intentos = 1
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nDemasiados intentos fallidos. Vuelva a comenzar.\n\n")
                time.sleep(2)
                iniciarSesion(diccionario_usuarios,intentos)
                
    return intentos, usuario_actual


def sacar_tildes(texto):
    """Funcion que se encarga de reemplazar la variable q entra por la palabra sin tilde"""
    tildes = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'ñ': 'n', 'Ñ': 'N'
    }
    for acento, sin_acento in tildes.items():
        texto = texto.replace(acento, sin_acento)

    return texto


def mostrar_filtro_vuelos(vuelos):
    pais_origen, pais_llegada = obtener_paises()
    if pais_origen == "-1" or pais_llegada == "-1": 
        return  
    
    os.system('cls' if os.name == 'nt' else 'clear')
    # Buscar vuelos
    resultados = buscar_vuelos(vuelos, pais_origen, pais_llegada)

    print(f"\nVuelos encontrados para ir desde {pais_origen} hasta {pais_llegada}\n")
    if resultados:
        for index, vuelo in resultados:
            print(f"{index}) {vuelo[0]}, {vuelo[1]} --> {vuelo[2]}, {vuelo[3]}   ==>   {vuelo[4]}\t{vuelo[5]}")
            print('-' * 85)
        print("\n\n")
    else:
        print("No se encontraron vuelos que coincidan.")


""" ********************** FILTRO VUELOS ********************* """


def buscar_vuelos(vuelos, pais_origen, pais_llegada):
    # Filtrar la matriz según el país de origen y país de llegada
    resultados = []
    
    pais_origen_sin_tildes = sacar_tildes(pais_origen)
    pais_llegada_sin_tildes = sacar_tildes(pais_llegada)

    for index, vuelo in enumerate(vuelos):  
        if sacar_tildes(vuelo[0]) == pais_origen_sin_tildes and sacar_tildes(vuelo[2]) == pais_llegada_sin_tildes:
            # Añadir tupla (index, vuelo), guardo index para posteriormente poder seleccionar la opcion del vuelo que quiero reservar
            resultados.append((index+1, vuelo)) 
            
    return resultados


def obtener_paises():
    bandera = True
    ok = True
    while bandera:
        pais_origen = input("\nIngrese el país de origen (o -1 para salir): ").title().strip() 
        if pais_origen == "-1": 
            return "-1", "-1" 
        if all(('a' <= char <= 'z' or 'A' <= char <= 'Z' or char == ' ') for char in pais_origen):
            bandera = False
        else:
            print("Error: Solo se permiten letras. Intenta nuevamente.")
    
    while ok:
        pais_llegada = input("Ingrese el país de llegada (o -1 para salir): ").title().strip() 
        if pais_llegada == "-1": 
            return "-1", "-1" 
        if all(('a' <= char <= 'z' or 'A' <= char <= 'Z' or char == ' ') for char in pais_llegada):
            ok = False
        else:
            print("Error: Solo se permiten letras. Intenta nuevamente.")
    
    return pais_origen, pais_llegada


""" ********************** RESERVAS E HISTORIALES *********************"""



def cancelarReserva(reservas, usuario_actual):
    """Función que permite al usuario cancelar una reserva existente, gestionando el reembolso o cambios según las políticas del sistema. Recibe lista de usuarios y lista de reservas existentes."""
    os.system('cls' if os.name == 'nt' else 'clear')
    bandera = True

    print("\nReservas del usuario:")
    reservas_usuario = list(filter(lambda reserva: reserva[0] == usuario_actual, reservas))

    if not reservas_usuario:
        print("No tiene reservas para cancelar.\n")
        return

    for i, reserva in enumerate(reservas_usuario):
        vuelo = reserva[1]
        print(f"{i + 1}. Origen: {vuelo[0]}, {vuelo[1]} -> Destino: {vuelo[2]}, {vuelo[3]} == {vuelo[4]}\t{vuelo[5]}")

    # Función lambda para validar la selección de reserva
    validar_seleccion = lambda seleccion: 1 <= seleccion <= len(reservas_usuario)

    while bandera:
        try:
            seleccion = int(input("\nSeleccione el número de la reserva que desea cancelar: \n"))
            if not validar_seleccion(seleccion):
                print("Selección de reserva inválida\n")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                bandera = False
        except ValueError:
            print("Error: Debes ingresar un número.")

    reserva_seleccionada = reservas_usuario[seleccion - 1]
    reservas.remove(reserva_seleccionada)

    print(f"\nReserva cancelada con éxito. Vuelo cancelado: Origen: {reserva_seleccionada[1][0]}, {reserva_seleccionada[1][1]} -> Destino: {reserva_seleccionada[1][2]}, {reserva_seleccionada[1][3]} == {reserva_seleccionada[1][4]}\t{reserva_seleccionada[1][5]}\n")

    # Verificar si la carpeta 'historiales' existe, si no, crearla
    carpeta_historiales = "historiales"
    if not os.path.exists(carpeta_historiales):
        os.makedirs(carpeta_historiales)

    # Crear o sobrescribir el archivo del historial en la carpeta
    nombre_archivo = os.path.join(carpeta_historiales, f"historial_reservas_{usuario_actual}.txt")
    

    
    # Reescribir el historial del usuario después de la cancelación
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(f"Historial de reservas del usuario: {usuario_actual}\n")
        archivo.write('-' * 80 + '\n')

        # Reescribir solo las reservas que quedan (después de la cancelación)
        reservas_usuario_actualizadas = list(filter(lambda reserva: reserva[0] == usuario_actual, reservas))  # Actualizar reservas del usuario
        for i, reserva in enumerate(reservas_usuario_actualizadas):
            vuelo = reserva[1]
            linea = f"{i+1}. | Origen: {vuelo[0]}, {vuelo[1]} -> Destino: {vuelo[2]}, {vuelo[3]}  == {vuelo[4]}\t{vuelo[5]}"
            archivo.write(linea + '\n')
            archivo.write('-' * 80 + '\n')
    
    # Leer el archivo actualizado para verificar
    with open(nombre_archivo, 'r') as archivo:
       
        print(archivo.read())



# Consultas Vuelos
def consultarStatusDeVuelo(vuelo_seleccionado):
    """Consulta y muestra el estado actual del vuelo seleccionado, proporcionando razones aleatorias si está cancelado."""

    origen_pais, origen_capital, destino_pais, destino_capital, fecha, hora, estado_vuelo = vuelo_seleccionado
    razones_cancelacion = ["Tormenta", "Vientos fuertes", "Problemas técnicos", "Falta de personal"]
    
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"Estado del vuelo seleccionado: Origen: {origen_pais}, {origen_capital} -> Destino: {destino_pais}, {destino_capital}")
    print(f"Fecha: {fecha} Hora: {hora}")
    
    if estado_vuelo == "Retrasado":
        razon = random.choice(razones_cancelacion)
        print(f"Estado actual del vuelo: {estado_vuelo}. Razón: {razon}.\n")
    elif estado_vuelo == "Cancelado":
        razon = random.choice(razones_cancelacion)
        print(f"Estado actual del vuelo: {estado_vuelo}. Razón: {razon}.\n")
    else:
        print(f"Estado actual del vuelo: {estado_vuelo}\n")
    
    return estado_vuelo


def pagarReserva():
    """Esta funcion gestiona el proceso de pago para completar una reserva, incluyendo la elección del método de pago y la confirmación de la transacción."""
    metodos_pago = {
        1: "Tarjeta de crédito",
        2: "Tarjeta de débito",
        3: "QR Mercado Pago"
    }
    print("\nProceso de pago iniciado.\n")
    print("Opciones de método de pago:")
    for clave, valor in metodos_pago.items():
        print(f"{clave}. {valor}")
    print("Ingrese -1 para cancelar el proceso de pago.") 

    bandera = True  
    while bandera:
        try:
            metodo_pago = input("\nSelecciona un método de pago: ") 
            if metodo_pago == "-1":  
                return False  
            metodo_pago = int(metodo_pago)
            if metodo_pago in metodos_pago:
                print(f"Método de pago seleccionado: {metodos_pago[metodo_pago]}.")
                bandera = False  
            else:
                print("\nMétodo de pago inválido. Intenta de nuevo.")
        except ValueError:
            print("Error: Debe ingresar solo números.")

    print("Espere un momento, su pago se está procesando...")
    transaccion_exitosa = random.choice([True, False, True, True])

    if transaccion_exitosa:
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("\nPago completado con éxito.")
        return True
    else:
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("\nError en la transacción. Vuelve a intentarlo.")
        return False



def historialReservas(usuario_actual):
    """Esta función muestra un historial de reservas realizadas por el usuario, incluyendo reservas anteriores y pagos.(antiguas y actuales) Recibe reservas actuales."""
    os.system('cls' if os.name == 'nt' else 'clear')

    # Verificar la carpeta y el archivo
    carpeta_historiales = "historiales"
    nombre_archivo = os.path.join(carpeta_historiales, f"historial_reservas_{usuario_actual}.txt")

    if not os.path.exists(nombre_archivo):
        print("No se encontró un historial de reservas para este usuario.\n")
        return

    # Leer y mostrar el contenido del archivo
    print("-" * 80)
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
    print("-" * 80)
                
    

def hacerReservaDeVuelos(vuelos, reservas, usuario_actual):
    """Esta funcion Facilita la reserva de un vuelo seleccionado, solicitando la información del usuario y confirmando la reserva. Recibe la matriz de Vuelos, la lista de usuarios existentes y las reservas actuales"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nIngrese -1 en cualquier momento para regresar al menú de vuelos.") 
    ok = True
    bandera = True
    ancho_pais = 20
    ancho_capital = 20

    print("\n")
    print('-' * 118)
    print("\t    Ubicación de Origen\t\t\t        Ubicación de Llegada\t\t          Fecha\t\tHora")
    print('-' * 118)
    for i, vuelo in enumerate(vuelos):
        origen_pais, origen_capital, destino_pais, destino_capital, fecha, hora, estado = vuelo
        print(f"{i+1}. | {origen_pais:<{ancho_pais}},{origen_capital:<{ancho_capital}}-->   {destino_pais:<{ancho_pais}},{destino_capital:<{ancho_capital}}\t{fecha}\t{hora}")
        print('-' * (ancho_pais + ancho_capital + ancho_pais + ancho_capital + 38))

    while bandera:
        try:
            seleccion = input("\nSeleccione el número del vuelo que desea reservar o '-1' para salir: \n") 
            if seleccion == "-1":  
                return  
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(vuelos):
                vuelo_seleccionado = vuelos[seleccion - 1]
                bandera = False
            else:
                print("Selección de vuelo inválida\n")
        except ValueError:
            print("Error: Debes ingresar solo números.")

    total_asientos = reservarAsientos() 
      

    estado = consultarStatusDeVuelo(vuelo_seleccionado)
    if estado == "Cancelado":
        print("No puedes reservar este vuelo porque está cancelado. Selecciona otro vuelo.\n")
        return
    print("-" * 50)

    if not pagarReserva():  
        print("\nLa reserva ha sido cancelada por el usuario.")  
        return

    os.system('cls' if os.name == 'nt' else 'clear')
    reservas.append((usuario_actual, vuelo_seleccionado))
    print("\nReserva realizada con ÉXITO\n")
    print(f"Vuelo reservado: Origen: {vuelo_seleccionado[0]}, {vuelo_seleccionado[1]} -> Destino: {vuelo_seleccionado[2]}, {vuelo_seleccionado[3]}  ==  {vuelo_seleccionado[4]}\t{vuelo_seleccionado[5]}\n")
    
    reservas_usuario = list(filter(lambda reserva: reserva[0] == usuario_actual, reservas))


    # Verificar si la carpeta 'historiales' existe, si no, crearla
    carpeta_historiales = "historiales"
    if not os.path.exists(carpeta_historiales): 
        os.makedirs(carpeta_historiales)

    # Crear o sobrescribir el archivo del historial en la carpeta
    nombre_archivo = os.path.join(carpeta_historiales, f"historial_reservas_{usuario_actual}.txt")
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(f"Historial de reservas del usuario: {usuario_actual}\n")
        archivo.write('-' * 80 + '\n')

        for i, reserva in enumerate(reservas_usuario):
            vuelo = reserva[1]
            linea = f"{i+1}. | Origen: {vuelo[0]}, {vuelo[1]} -> Destino: {vuelo[2]}, {vuelo[3]}  == {vuelo[4]}\t{vuelo[5]}"
            archivo.write(linea + '\n')
            archivo.write('-' * 80 + '\n')

    print(f"La informacion de sus reservas ha sido actualizada en su historial con numero de usuario {usuario_actual}\n\n")

    imprimirTicket(usuario_actual, vuelo_seleccionado, total_asientos)



""" ********************** SELECCION DE ASIENTOS Y ESTRUCTURA DE AVION *********************"""


def crearAvion(filas, columnas):
    asientos = [['O' for _ in range(columnas)] for _ in range(filas)]
    return asientos


def ocuparAsientosAleatorios(asientos, cantidad):
    filas = len(asientos)
    columnas = len(asientos[0])
    total_asientos = filas * columnas

    if cantidad > total_asientos:
        cantidad = total_asientos  # No se puede ocupar más asientos de los disponibles.

    # Generar posiciones únicas al azar
    posiciones = random.sample(range(total_asientos), cantidad)
    for pos in posiciones:
        fila = pos // columnas
        columna = pos % columnas
        asientos[fila][columna] = 'X'


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

def seleccionarAsiento(asientos, seleccionados, total_asientos):
    bandera = True
    # Mapeo de letras a índices
    columnas_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5} 

    while bandera:
        if seleccionados >=8:
            print("Se ha alcanzado el limite de asientos seleccionados.")
            bandera = False
            continue

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
                    total_asientos.append(seleccion)
                    asientos[fila][columna] = 'X'
                    mostrarAvion(asientos)
                    print(f"Asiento {seleccion} reservado con éxito.")
                    seleccionados +=1

            except ValueError:
                print("Entrada no válida, intenta de nuevo.")
    return seleccionados ,total_asientos

def reservarAsientos(): 
    total_asientos = []                                          
    filas = 20  
    columnas = 6  
    asientos = crearAvion(filas, columnas)

    numrandom = random.randint(30, 60)

    ocuparAsientosAleatorios(asientos, numrandom)

    seleccionados = 0 
    bandera = True

    while bandera:
        print("\n" + "-" * 40)
        print("   Boing 737 - Selección de Asientos")
        print("-" * 40)
        mostrarAvion(asientos)
        seleccionados, total_asientos = seleccionarAsiento(asientos, seleccionados, total_asientos)
        print("-" * 40 + "\n")

        bandera = False

    return total_asientos

def imprimirTicket(usuario_actual, vuelo, total_asientos):
    origen_pais, origen_capital, destino_pais, destino_capital, fecha, hora, estado = vuelo
    
    numero_vuelo=random.randint(1000,9999)
    

    for numero_asiento in total_asientos:
        ticket = f"""

            ****************************************************************************************
                                                BOARDING PASS                                                                          
            ****************************************************************************************
            
                N° Usuario: {usuario_actual}                    Fecha: {fecha}
            
            Desde/From: {origen_pais}, {origen_capital}         Vuelo n°/Flight nr:{numero_vuelo}
            Asiento/Seat: {numero_asiento}                      A/To: {destino_pais}, {destino_capital} 
            
                Puerta/Gate: E01                                Hora: {hora}

            ****************************************************************************************
                                        ¡Gracias por viajar con nosotros!
            ****************************************************************************************    
        
       
        """
        print(ticket)
    
    input("Presione la tecla ENTER para continuar.")
    os.system('cls' if os.name == 'nt' else 'clear')



def main():
    reservas = []
    diccionario_usuarios = {0000:
                            {"nombre y apellido":"Administrador",
                            "contrasena":"admin"}
                            }

    salir = True
    salir2 = True

    vuelos = generarVuelos(matrizPaisesCapitales)
    while salir:
        seleccion = menuInicial()

        if seleccion == 1:
            intentos=0
            intentos=registrarUsuario(diccionario_usuarios,intentos)

        elif seleccion == 2:
            intentos=0
            os.system('cls' if os.name == 'nt' else 'clear')
            intentos, usuario_actual = iniciarSesion(diccionario_usuarios, intentos)

            salir2 = True

            while salir2:
                
                seleccion = menuVuelos()

                if seleccion == 1:
                    # Buscar vuelos               
                    imprimirMatrizOrdenada(vuelos)
                    # Seleccionar segun pais de origen y llegada
                    mostrar_filtro_vuelos(vuelos)
                elif seleccion == 2:
                    # Hacer reserva y pagar
                    hacerReservaDeVuelos(vuelos, reservas, usuario_actual)
                elif seleccion == 3:
                    # Historial de reservas
                    historialReservas(usuario_actual)  
                elif seleccion == 4:
                    # Imprimir escalas
                    ImprimirVuelosEscalas(vuelos_escalas)                    
                elif seleccion == 5:
                    # Cancelar reservas
                    cancelarReserva(reservas, usuario_actual)
                elif seleccion==6:
                    # Cerrar sesion
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(Style.BRIGHT + Fore.RED + "=" * 40)
                    print(Fore.RED + Style.BRIGHT + "        ¡SESION CERRADA! 🔒")
                    print(Fore.WHITE + "    Gracias por usar el sistema.")
                    print(Fore.RED + "=" * 40)
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')    

                    salir2 = False
        else:
            print(Style.BRIGHT + Fore.GREEN + "=" * 70)
            print(Fore.GREEN + Style.BRIGHT + "   ✈️  ¡¡¡¡Gracias por utilizar nuestro Sistema de Vuelos!!!! ✈️")
            print(Fore.RED + "\n\t\t       🛑 ADIOS 🛑 \n")
            print(Fore.GREEN + "=" * 70)
            salir = False

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
main()

