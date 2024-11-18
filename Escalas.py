import json
import random
from datetime import datetime, timedelta

def leerArchivoRegiones(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding='utf-8') as archivo:
        return json.load(archivo)

def incrementar_hora(vuelo):
    # Convierto la hora del vuelo a un objeto datetime
    hora_vuelo = datetime.strptime(vuelo['hora'], "%H:%M")
    
    # numero random para hacer mas creible la diferencia de salida de los vuelos con escalas
    incremento_hora = random.randint(8, 13)
    nueva_hora = hora_vuelo + timedelta(hours=incremento_hora)

    # Verifico si la hora supera las 24 horas y ajustar el día si es necesario
    if nueva_hora.day > hora_vuelo.day:
        nueva_fecha = datetime.strptime(vuelo['fecha'], "%Y-%m-%d") + timedelta(days=1)
        vuelo['fecha'] = nueva_fecha.strftime("%Y-%m-%d")
    
    vuelo['hora'] = nueva_hora.strftime("%H:%M")
    return vuelo

def gestionarEscalas(vuelos):
    suramerica = leerArchivoRegiones("Regiones/suramerica.json")
    norteamerica = leerArchivoRegiones("Regiones/norteamerica.json")
    centroamerica = leerArchivoRegiones("Regiones/centroamerica.json")
    
    # Creo listas de países
    paises_suramerica = {pais['pais'] for pais in suramerica}
    paises_norteamerica = {pais['pais'] for pais in norteamerica}
    paises_centroamerica = [pais['pais'] for pais in centroamerica]  

    # Lista para almacenar los nuevos vuelos con escalas
    vuelos_sin_escalas = []
    vuelos_escalas = []

    for vuelo in vuelos:
        pais_salida = vuelo['origen_pais']
        pais_llegada = vuelo['destino_pais']

        if (pais_salida in paises_suramerica and pais_llegada in paises_norteamerica) or (pais_salida in paises_norteamerica and pais_llegada in paises_suramerica):
            # print(f"Vuelo de {pais_salida} a {pais_llegada}: es necesario hacer una escala.")
            # Se elige un país aleatorio de Centroamérica
            pais_random_centroamerica = random.choice(paises_centroamerica)            
            # Se crean los dos vuelos de escalas
            vuelo_1 = {
                'origen_pais': pais_salida,
                'origen_capital': vuelo['origen_capital'],
                'destino_pais': pais_random_centroamerica,
                'destino_capital': 'Escala',
                'fecha': vuelo['fecha'],
                'hora': vuelo['hora'],
                'estado_vuelo': vuelo['estado_vuelo']
            }
            vuelo_2 = {
                'origen_pais': pais_random_centroamerica,
                'origen_capital': 'Escala',
                'destino_pais': pais_llegada,
                'destino_capital': vuelo['destino_capital'],
                'fecha': vuelo['fecha'],
                'hora': vuelo['hora'],
                'estado_vuelo': vuelo['estado_vuelo']
            }

            # Se agregan los vuelos de escala a la lista de vuelos escalas
            vuelos_escalas.append(vuelo_1)
            vuelos_escalas.append(vuelo_2)
        else:
            # Se agrega vuelo directo sin cambios a la lista de vuelos directos
            vuelos_sin_escalas.append(vuelo)

    # Modificar las horas de los vuelos en posiciones impares de vuelos_escalas
    for i in range(1, len(vuelos_escalas), 2):  # Solo posiciones impares
        vuelos_escalas[i] = incrementar_hora(vuelos_escalas[i])

    return vuelos_sin_escalas, vuelos_escalas

vuelos = leerArchivoRegiones("BDvuelos/vuelos.json")

vuelos_sin_escalas, vuelos_escalas = gestionarEscalas(vuelos)

# # Imprimir los resultados si es necesario
# print("\nVuelos directos:")
# for vuelo in vuelos_con_escalas:
#     print(vuelo)

# print("\nVuelos con escalas:")
# for vuelo in vuelos_escalas:
#     print(vuelo)
