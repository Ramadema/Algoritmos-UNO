# Proyecto_SistVuelos_G1                    
    # UADE
    # Profesora: Maria Julia Monasterio
    # Materia: Algoritmos y estructuras de datos I
    # Integrantes: Ramiro De Marco / Juan Olobardi / Tomas Schiabone



- Introduccion al proyecto de Sitema de Reserva de Vuelos:

Este programa es un sistema de reserva de vuelos diseñado para facilitar a los usuarios la gestión de sus viajes. Permite registrar nuevos usuarios, iniciar sesión, buscar vuelos, realizar reservas, cancelar reservas y consultar el historial de vuelos. El enfoque principal del sistema son los vuelos entre países de América del Norte, central y del Sur.

Al iniciar el programa, se presenta un menú inicial que ofrece tres opciones: registro de usuarios, inicio de sesión y salida del sistema. 
Una vez que un usuario inicia sesión, accede a un menú adicional donde puede buscar vuelos disponibles, reservar un vuelo, consultar su historial de reservas o cancelar una reserva existente. El sistema proporciona una experiencia interactiva y fácil de usar, asegurando que los usuarios puedan gestionar sus necesidades de viaje de manera eficiente.

El sistema también incluye funcionalidades adicionales como la generación aleatoria de vuelos y estados (a tiempo, retrasado, cancelado), así como validaciones de entrada para asegurar que los datos proporcionados sean correctos. Las contraseñas se validan utilizando expresiones regulares para garantizar que cumplan con los requisitos de seguridad.


- FUNCIONES:

menuInicial: Muestra el menú principal donde los usuarios pueden elegir entre registrarse, iniciar sesión o salir del sistema.

menuVuelos: Presenta un menú adicional para usuarios autenticados, permitiendo seleccionar acciones relacionadas con los vuelos, como búsqueda, reserva, historial, cancelación y cierre de sesión.

generar_fecha_hora: Crea una fecha y hora aleatoria dentro de los próximos 30 días, utilizada para asignar horarios a los vuelos.

generarVuelos: Genera una lista de vuelos aleatorios entre países de América del Norte y del Sur, incluyendo detalles como origen, destino, fecha, hora y estado del vuelo.

imprimirMatrizOrdenada: Imprime una tabla con la información de los vuelos en un formato ordenado y legible.

registrarUsuario: Permite a nuevos usuarios crear una cuenta en el sistema, validando el PIN y la contraseña según criterios específicos.

iniciarSesion: Permite a los usuarios existentes acceder al sistema mediante su PIN y contraseña, con controles de seguridad para limitar intentos fallidos.

sacar_tildes: Elimina acentos de los nombres de países para facilitar las búsquedas sin errores de acentuación.

mostrar_filtro_vuelos: Permite a los usuarios buscar vuelos basándose en el país de origen y destino ingresado.

cancelarReserva: Facilita la cancelación de reservas existentes por parte del usuario, mostrando las reservas disponibles para cancelar.

consultarStatusDeVuelo: Muestra el estado actual de un vuelo seleccionado y proporciona razones aleatorias en caso de que esté cancelado.

pagarReserva: Gestiona el proceso de pago para completar una reserva, permitiendo a los usuarios seleccionar un método de pago y confirmando la transacción.

historialReservas: Muestra un historial de reservas realizadas por el usuario, incluyendo detalles de vuelos anteriores y pagos.

hacerReservaDeVuelos: Facilita la selección y reserva de un vuelo, incluyendo la verificación del estado del vuelo y el proceso de pago.

main: Es el punto de entrada del programa y se encarga de gestionar el flujo general del sistema de reserva de vuelos.

