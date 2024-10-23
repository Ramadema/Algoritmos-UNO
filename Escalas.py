import json
import random

def leerAchivoRegiones(nombre_archivo):
    with open(nombre_archivo, 'rt') as archivo:
        return json.load(archivo)

def gestionarEscalas(vuelos):
    suramerica = leerAchivoRegiones('Regiones/suramerica.json')
    norteamerica = leerAchivoRegiones('Regiones/norteamerica.json')
    centroamerica = leerAchivoRegiones('Regiones/centroamerica.json')

    # Crear listas de países
    paises_suramerica = {pais['pais'] for pais in suramerica}
    paises_norteamerica = {pais['pais'] for pais in norteamerica}
    paises_centroamerica = [pais['pais'] for pais in centroamerica]  

    # Lista para almacenar los nuevos vuelos con escalas
    vuelos_con_escalas = []
    vuelos_escalas = []

    for vuelo in vuelos:
        pais_salida = vuelo[0]
        pais_llegada = vuelo[2]

        if (pais_salida in paises_suramerica and pais_llegada in paises_norteamerica) or \
            (pais_salida in paises_norteamerica and pais_llegada in paises_suramerica):
                print(f"Vuelo de {pais_salida} a {pais_llegada}: es necesario hacer una escala.")
        else:
            print(f"Vuelo de {pais_salida} a {pais_llegada}: el vuelo es directo.")
    print("\n")
    # Iterar sobre la matriz de vuelos
    for vuelo in vuelos:
        pais_salida = vuelo[0]
        pais_llegada = vuelo[2]

        if (pais_salida in paises_suramerica and pais_llegada in paises_norteamerica) or \
           (pais_salida in paises_norteamerica and pais_llegada in paises_suramerica):
            # Elegir un país aleatorio de Centroamérica
            pais_random_centroamerica = random.choice(paises_centroamerica)

            # Crear los dos vuelos
            vuelo_1 = (pais_salida, vuelo[1], pais_random_centroamerica, 'Escala', vuelo[4], vuelo[5], vuelo[6])
            vuelo_2 = (pais_random_centroamerica, 'Escala', pais_llegada, vuelo[3], vuelo[4], vuelo[5], vuelo[6])

            # Agregar los vuelos de escala a la lista de vuelos escalas
            vuelos_escalas.append(vuelo_1)
            vuelos_escalas.append(vuelo_2)
        else:
            # Agregar vuelo directo sin cambios
            vuelos_con_escalas.append(vuelo)

    return vuelos_con_escalas, vuelos_escalas

# Ejemplo de matriz de vuelos (lista de tuplas)
vuelos = [
    ('Nicaragua', 'Managua', 'Uruguay', 'Montevideo', '2024-10-31', '01:54', 'A tiempo'),
    ('Chile', 'Santiago', 'Ecuador', 'Quito', '2024-11-12', '23:36', 'A tiempo'),
    ('Estados Unidos', 'Washington, D.C.', 'Colombia', 'Bogotá', '2024-11-18', '00:54', 'A tiempo'),
    ('Paraguay', 'Asunción', 'Canadá', 'Ottawa', '2024-11-12', '09:02', 'A tiempo'),
    ('Estados Unidos', 'Washington, D.C.', 'Chile', 'Santiago', '2024-11-20', '18:28', 'A tiempo')
]

# Llamar a la función y mostrar los resultados
vuelos_con_escalas, vuelos_escalas = gestionarEscalas(vuelos)

print("Vuelos directos:")
for vuelo in vuelos_con_escalas:
    print(vuelo)

print("\nVuelos con escalas:")
for vuelo in vuelos_escalas:
    print(vuelo)
