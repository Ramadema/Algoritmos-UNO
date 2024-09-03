# Proyecto_SistVuelos_G1

Introduccion al proyecto de Sitema de Reserva de Vuelos


El programa de búsqueda de vuelos del Sistema de Reserva de Vuelos permite a los usuarios encontrar opciones de vuelo adecuadas según sus preferencias, como el lugar de salida, el destino y las fechas deseadas. Por ejemplo, un usuario puede buscar vuelos desde Buenos Aires a Madrid, o de Nueva York a Tokio. Al ingresar estos detalles, el programa revisa todas las opciones disponibles y muestra los vuelos que cumplen con los criterios especificados. En caso de que no se encuentren vuelos disponibles o surjan problemas durante la búsqueda, el sistema proporciona mensajes claros para informar al usuario. Además, el programa asegura que la información de los vuelos se mantenga actualizada y evita mostrar resultados repetidos, ofreciendo así una experiencia de búsqueda precisa y fácil de usar.


Integrantes 

Ramiro De Marco
Juan Olobardi 
Tomas Schiabone


Preview Modularización

FUNCIONES

def MenuInicial --> rama
"Esta Funcion actúa como el punto central de navegación para el usuario. Primero, muestra un listado de opciones disponibles, como buscar vuelos, hacer una reserva o ver reservas existentes. Luego, captura la selección del usuario y dirige la acción correspondiente: llama a la función adecuada para realizar la tarea elegida. Finalmente, después de completar la acción, el menú se vuelve a mostrar para permitir nuevas opciones o salir del programa. En resumen, la función menu organiza y facilita la interacción del usuario con el sistema, manteniendo el flujo de operaciones sencillo y accesible."


#Usuario
def registrarUsuario --> juan
"Funcion que permite a nuevos usuarios crear una cuenta en el sistema de reservas."

def iniciarSesion --> juan
"Funcion que permite a los usuarios existentes iniciar sesión en el sistema para acceder a sus reservas y realizar nuevas transacciones."

def cerrarSesion --> juan
"Funcion que cierra la sesión del usuario actual, asegurando que la información personal y las reservas estén protegidas."


#Vuelos
def generarVuelos --> rama
"La funcion permite generar una cantidad establecida de vuelos entre paises de sudamerica y america del norte o combinacion de ambas.

def BusquedaDeVuelos --> juan
"Esta funcion permite al usuario buscar vuelos disponibles según los criterios especificados, como destino, fecha y número de pasajeros."


#Reservas
def hacerReservaDeVuelos --> tomi
"Esta funcion Facilita la reserva de un vuelo seleccionado, solicitando la información del usuario y confirmando la reserva."

def cancelarReserva --> tomi
"Esta funcion permite al usuario cancelar una reserva existente, gestionando el reembolso o cambios según las políticas del sistema."

def consultarStatusDeVuelo --> tomi
"Esta funcion proporciona información actualizada sobre el estado de un vuelo, como retrasos o cambios en la programación"

def pagarReserva --> rama
"Esta funcion gestiona el proceso de pago para completar una reserva, incluyendo la elección del método de pago y la confirmación de la transacción"

def historialReservas --> rama
"Esta funcion muestra un historial de reservas realizadas por el usuario, incluyendo reservas anteriores y pagos.(antiguas y actuales)"


PROGRAMA PRINCIPAL
printeo 
llamadas a funciones

