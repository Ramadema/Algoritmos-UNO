import json
import random

def leerArchivoRegiones(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding='utf-8') as archivo:
        return json.load(archivo)

def gestionarEscalas(vuelos):
    suramerica = leerArchivoRegiones("Regiones/suramerica.json")
    norteamerica = leerArchivoRegiones("Regiones/norteamerica.json")
    centroamerica = leerArchivoRegiones("Regiones/centroamerica.json")
    
    # Crear listas de países
    paises_suramerica = {pais['pais'] for pais in suramerica}
    paises_norteamerica = {pais['pais'] for pais in norteamerica}
    paises_centroamerica = [pais['pais'] for pais in centroamerica]  

    # Lista para almacenar los nuevos vuelos con escalas
    vuelos_con_escalas = []
    vuelos_escalas = []

    for vuelo in vuelos:
        pais_salida = vuelo['origen_pais']
        pais_llegada = vuelo['destino_pais']

        if (pais_salida in paises_suramerica and pais_llegada in paises_norteamerica) or (pais_salida in paises_norteamerica and pais_llegada in paises_suramerica):
            print(f"Vuelo de {pais_salida} a {pais_llegada}: es necesario hacer una escala.")
            # Se elije un país aleatorio de Centroamérica cualquiera
            pais_random_centroamerica = random.choice(paises_centroamerica)

            # Se crean los dos vuelos de escalas
            vuelo_1 = {
                'origen_pais': pais_salida,
                'origen_capital': vuelo['origen_capital'],
                'destino_pais': pais_random_centroamerica,
                'destino_capital': 'Escala',  # Podemos poner cualquier cosa
                'fecha': vuelo['fecha'],
                'hora': vuelo['hora'],
                'estado_vuelo': vuelo['estado_vuelo']
            }
            vuelo_2 = {
                'origen_pais': pais_random_centroamerica,
                'origen_capital': 'Escala',  # Podemos poner cualquier cosa
                'destino_pais': pais_llegada,
                'destino_capital': vuelo['destino_capital'],
                'fecha': vuelo['fecha'],
                'hora': vuelo['hora'],
                'estado_vuelo': vuelo['estado_vuelo']
            }

            # Se agrega los vuelos de escala a la lista de vuelos escalas
            vuelos_escalas.append(vuelo_1)
            vuelos_escalas.append(vuelo_2)
        else:
            # Se agrega vuelo directo sin cambios a la lista de vuelos directos
            vuelos_con_escalas.append(vuelo)

    return vuelos_con_escalas, vuelos_escalas

vuelos = leerArchivoRegiones("BDvuelos/vuelos.json")

vuelos_con_escalas, vuelos_escalas = gestionarEscalas(vuelos)

print("\nVuelos directos:")
for vuelo in vuelos_con_escalas:
    print(vuelo)

print("\nVuelos con escalas:")
for vuelo in vuelos_escalas:
    print(vuelo)
