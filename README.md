# README - Sistema de Reserva de Vuelos

## Introducción
Este programa es un sistema de reserva de vuelos diseñado para facilitar la gestión de viajes de los usuarios. Permite registrar nuevos usuarios, iniciar sesión, buscar vuelos, realizar reservas, cancelar reservas y consultar el historial de vuelos. El sistema está enfocado en vuelos entre países de América del Norte, Centro y Sur.

Al iniciar el programa, se presenta un menú inicial con tres opciones principales: registro de usuarios, inicio de sesión y salida del sistema. Una vez autenticado, el usuario accede a un menú adicional donde puede realizar distintas acciones relacionadas con los vuelos. El sistema también incluye funcionalidades avanzadas como la generación aleatoria de vuelos y validaciones de seguridad para el manejo de contraseñas.

## Descripción
Este sistema permite a los usuarios:
- Registrarse y gestionar sus credenciales de acceso.
- Buscar vuelos disponibles por origen y destino.
- Reservar vuelos y seleccionar asientos.
- Consultar su historial de reservas.
- Cancelar reservas de vuelos.
- Ver el estado de los vuelos en tiempo real.

## Características
- Generación aleatoria de vuelos con estados (a tiempo, retrasado, cancelado).
- Validación de contraseñas con expresiones regulares.
- Almacenamiento de datos en formato JSON.
- Interfaz interactiva y fácil de usar.

## Requisitos
- Python 3.x
- Biblioteca `json` (incluida en la librería estándar de Python)
- Biblioteca `random` (incluida en la librería estándar de Python)

## Instalación
1. Clonar este repositorio:
   ```sh
   git clone https://github.com/usuario/repo.git
   ```
2. Navegar al directorio del proyecto:
   ```sh
   cd repo
   ```
3. Ejecutar el programa:
   ```sh
   python script.py
   ```

## Uso
Al ejecutar el programa, se mostrará un menú con las siguientes opciones:
1. Registrar usuario.
2. Iniciar sesión.
3. Buscar vuelos.
4. Reservar un vuelo.
5. Consultar historial de reservas.
6. Cancelar una reserva.
7. Ver estado de un vuelo.
8. Salir.

El usuario puede interactuar con el menú seleccionando una opción numérica.

## Funcionalidades Principales
- `menuInicial`: Muestra el menú principal con las opciones de registro, inicio de sesión o salida.
- `menuVuelos`: Presenta un menú adicional para usuarios autenticados con opciones de búsqueda, reserva y cancelación de vuelos.
- `generar_fecha_hora`: Genera una fecha y hora aleatoria dentro de los próximos 30 días.
- `generarVuelos`: Crea una lista de vuelos aleatorios entre países de América del Norte, Centro y Sur.
- `guardarVuelosEnJson`: Guarda los datos de los vuelos en un archivo JSON.
- `imprimirMatrizOrdenada`: Muestra los vuelos en un formato estructurado.
- `registrarUsuario`: Permite a nuevos usuarios registrarse validando su PIN y contraseña.
- `iniciarSesion`: Autentica a los usuarios mediante PIN y contraseña.
- `mostrar_filtro_vuelos`: Filtra vuelos según el país de origen y destino.
- `cancelarReserva`: Permite a los usuarios cancelar reservas existentes.
- `consultarStatusDeVuelo`: Muestra el estado actual de un vuelo seleccionado.
- `pagarReserva`: Gestiona el proceso de pago para completar una reserva.
- `historialReservas`: Muestra el historial de reservas de un usuario.
- `hacerReservaDeVuelos`: Gestiona la selección y confirmación de una reserva de vuelo.
- `imprimirTicket`: Genera un pase de abordaje con los detalles de la reserva.
- `main`: Punto de entrada del programa.

## Funcionalidades Adicionales
- `crearAvion`: Genera la disposición inicial del avión con filas y asientos disponibles.
- `mostrarAvion`: Muestra gráficamente la disponibilidad de los asientos.
- `seleccionarAsiento`: Permite a los usuarios elegir y reservar un asiento.
- `leerArchivoRegiones`: Carga los datos de las regiones desde archivos JSON.
- `gestionarEscalas`: Divide vuelos en tramos con escalas automáticas.
- `incrementar_hora`: Ajusta los horarios de los vuelos con escalas.


---

# README - Flight Booking System

## Introduction
This program is a flight booking system designed to help users manage their trips efficiently. It allows users to register, log in, search for flights, make reservations, cancel bookings, and check their booking history. The system focuses on flights between countries in North, Central, and South America.

When the program starts, an initial menu is presented with three main options: user registration, login, and system exit. Once logged in, users can access additional options related to flight management. The system also includes advanced features such as random flight generation and password security validations.

## Description
This system allows users to:
- Register and manage login credentials.
- Search for available flights by origin and destination.
- Book flights and select seats.
- Check their booking history.
- Cancel flight reservations.
- View flight status in real time.

## Features
- Random flight generation with status (on time, delayed, canceled).
- Password validation using regular expressions.
- Data storage in JSON format.
- Interactive and user-friendly interface.

## Requirements
- Python 3.x
- `json` library (included in Python standard library)
- `random` library (included in Python standard library)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/user/repo.git
   ```
2. Navigate to the project directory:
   ```sh
   cd repo
   ```
3. Run the program:
   ```sh
   python script.py
   ```

## Usage
When running the program, a menu will be displayed with the following options:
1. Register user.
2. Log in.
3. Search flights.
4. Book a flight.
5. Check booking history.
6. Cancel a booking.
7. View flight status.
8. Exit.

Users can interact with the menu by selecting a numeric option.

